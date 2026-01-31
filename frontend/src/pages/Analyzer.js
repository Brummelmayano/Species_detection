import React, { useState, useEffect } from 'react';
import {
  Grid,
  Box,
  Container,
  Typography,
  Paper,
  Card,
  CardMedia,
  CardContent,
  Chip,
  Button,
  Alert,
  CircularProgress,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import apiClient, { API_BASE_URL } from '../config/api';

const Analyzer = () => {
  const [projects, setProjects] = useState([]);
  const [loadingProjects, setLoadingProjects] = useState(false);
  const [selectedProject, setSelectedProject] = useState(null);
  const [images, setImages] = useState([]);
  const [loadingImages, setLoadingImages] = useState(false);
  const [selectedImage, setSelectedImage] = useState(null);
  const [detections, setDetections] = useState([]);
  const [loadingDetections, setLoadingDetections] = useState(false);
  const [analyzing, setAnalyzing] = useState(false);
  const [error, setError] = useState(null);

  const normalizeImageUrl = (url, id) => {
    if (!url) return `https://via.placeholder.com/300x200?text=Image+${id || 'Apercu'}`;
    if (url.startsWith('/')) return `${API_BASE_URL}${url}`;
    return url;
  };

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        setLoadingProjects(true);
        const response = await apiClient.get('/projects');
        setProjects(Array.isArray(response.data) ? response.data : []);
        setError(null);
      } catch (err) {
        setError('Erreur lors du chargement des projets');
        console.error(err);
      } finally {
        setLoadingProjects(false);
      }
    };
    fetchProjects();
  }, []);

  useEffect(() => {
    const fetchImages = async () => {
      if (!selectedProject) {
        setImages([]);
        return;
      }
      try {
        setLoadingImages(true);
        const response = await apiClient.get('/images/', {
          params: { project_id: selectedProject.id, limit: 100 },
        });
        setImages(response.data);
        setError(null);
      } catch (err) {
        setError('Erreur lors du chargement des images');
        console.error(err);
      } finally {
        setLoadingImages(false);
      }
    };
    fetchImages();
  }, [selectedProject]);

  useEffect(() => {
    const fetchDetections = async () => {
      if (!selectedImage) {
        setDetections([]);
        return;
      }
      try {
        setLoadingDetections(true);
        const response = await apiClient.get(`/images/${selectedImage.id}/detections`);
        setDetections(response.data);
        setError(null);
      } catch (err) {
        setError('Erreur lors du chargement des détections');
        console.error(err);
      } finally {
        setLoadingDetections(false);
      }
    };
    fetchDetections();
  }, [selectedImage]);

  const handleAnalyzeImage = async () => {
    if (!selectedImage) return;
    try {
      setAnalyzing(true);
      const response = await apiClient.get(`/images/${selectedImage.id}/detections`);
      setDetections(response.data);
      setError(null);
    } catch (err) {
      setError("Erreur lors de l'analyse");
      console.error(err);
    } finally {
      setAnalyzing(false);
    }
  };

  const stats = {
    totalProjects: projects.length,
    totalImages: projects.reduce((sum, p) => sum + (p.image_count || 0), 0),
    totalDetections: projects.reduce((sum, p) => sum + (p.detection_count || 0), 0),
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

      <Grid container spacing={2} sx={{ mb: 4 }}>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="textSecondary">Projets</Typography>
            <Typography variant="h3" color="primary">{stats.totalProjects}</Typography>
          </Paper>
        </Grid>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="textSecondary">Images</Typography>
            <Typography variant="h3" color="primary">{stats.totalImages}</Typography>
          </Paper>
        </Grid>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="textSecondary">Détections</Typography>
            <Typography variant="h3" color="primary">{stats.totalDetections}</Typography>
          </Paper>
        </Grid>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="textSecondary">Précision moyenne</Typography>
            <Typography variant="h3" color="primary">
              {detections.length > 0
                ? (
                    detections.reduce((sum, d) => sum + (d.confidence_score || 0), 0) / detections.length * 100
                  ).toFixed(1)
                : '0'}%
            </Typography>
          </Paper>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        <Grid xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>Projets</Typography>
            {loadingProjects ? (
              <Box sx={{ display: 'flex', justifyContent: 'center', p: 2 }}><CircularProgress size={30} /></Box>
            ) : projects.length === 0 ? (
              <Typography color="textSecondary">Aucun projet</Typography>
            ) : (
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                {projects.map((project) => (
                  <Card
                    key={project.id}
                    onClick={() => setSelectedProject(project)}
                    sx={{
                      cursor: 'pointer',
                      bgcolor: selectedProject?.id === project.id ? '#e3f2fd' : 'transparent',
                      border: selectedProject?.id === project.id ? '2px solid #1976d2' : '1px solid #ddd',
                      transition: 'all 0.2s',
                      '&:hover': { boxShadow: 2 },
                    }}
                  >
                    <CardContent sx={{ py: 1, px: 2, '&:last-child': { pb: 1 } }}>
                      <Typography variant="subtitle2" fontWeight="bold">{project.name}</Typography>
                      <Typography variant="caption" color="textSecondary">{project.image_count || 0} images • {project.detection_count || 0} détections</Typography>
                    </CardContent>
                  </Card>
                ))}
              </Box>
            )}
          </Paper>
        </Grid>

        <Grid xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>Images {selectedProject && `- ${selectedProject.name}`}</Typography>
            {!selectedProject ? (
              <Typography color="textSecondary">Sélectionnez un projet</Typography>
            ) : loadingImages ? (
              <Box sx={{ display: 'flex', justifyContent: 'center', p: 2 }}><CircularProgress size={30} /></Box>
            ) : images.length === 0 ? (
              <Typography color="textSecondary">Aucune image dans ce projet</Typography>
            ) : (
              <Grid container spacing={2}>
                {images.map((image) => (
                  <Grid xs={12} sm={6} md={4} key={image.id}>
                    <Card
                      onClick={() => setSelectedImage(image)}
                      sx={{
                        cursor: 'pointer',
                        border: selectedImage?.id === image.id ? '3px solid #1976d2' : '1px solid #ddd',
                        transition: 'all 0.2s',
                        '&:hover': { boxShadow: 3 },
                      }}
                    >
                      <CardMedia
                        component="img"
                        height="140"
                        image={normalizeImageUrl(image.url, image.id)}
                        alt={image.filename}
                        onError={(e) => { e.target.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="200" height="140"%3E%3Crect fill="%23ddd" width="200" height="140"/%3E%3Ctext x="50%" y="50%" text-anchor="middle" dy=".3em" fill="%23999"%3EImage non disponible%3C/text%3E%3C/svg%3E'; }}
                      />
                      <CardContent sx={{ py: 1, px: 2 }}>
                        <Typography variant="caption" noWrap>{image.filename}</Typography>
                        <Chip label={`${image.detection_count || 0} détections`} size="small" color="primary" variant="outlined" sx={{ mt: 1 }} />
                      </CardContent>
                    </Card>
                  </Grid>
                ))}
              </Grid>
            )}
          </Paper>
        </Grid>

        {selectedImage && (
          <Grid xs={12}>
            <Paper sx={{ p: 2 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                <Typography variant="h6">Détections - {selectedImage.filename}</Typography>
                <Button variant="contained" color="primary" onClick={handleAnalyzeImage} disabled={analyzing} size="small">
                  {analyzing ? <CircularProgress size={20} /> : 'Ré-analyser'}
                </Button>
              </Box>

              <Box sx={{ mb: 2, overflow: 'hidden', borderRadius: 1, border: '1px solid #ddd', maxHeight: '400px', display: 'flex' }}>
                <img src={normalizeImageUrl(selectedImage.url, selectedImage.id)} alt={selectedImage.filename} style={{ width: '100%', objectFit: 'contain' }} onError={(e) => { e.target.style.display = 'none'; }} />
              </Box>

              {loadingDetections ? (
                <Box sx={{ display: 'flex', justifyContent: 'center', p: 2 }}><CircularProgress size={30} /></Box>
              ) : detections.length === 0 ? (
                <Typography color="textSecondary">Aucune détection</Typography>
              ) : (
                <TableContainer>
                  <Table size="small">
                    <TableHead>
                      <TableRow sx={{ bgcolor: '#f5f5f5' }}>
                        <TableCell>Espèce</TableCell>
                        <TableCell align="right">Confiance</TableCell>
                        <TableCell align="right">Bounding Box</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {detections.map((detection, idx) => (
                        <TableRow key={idx}>
                          <TableCell>
                            <Typography variant="body2" fontWeight="bold">{detection.species_name || 'Inconnu'}</Typography>
                          </TableCell>
                          <TableCell align="right">
                            <Chip label={`${(detection.confidence_score * 100).toFixed(1)}%`} color={detection.confidence_score > 0.8 ? 'success' : detection.confidence_score > 0.6 ? 'warning' : 'error'} size="small" />
                          </TableCell>
                          <TableCell align="right">
                            <Typography variant="caption">({detection.bbox_x_min?.toFixed(1)}, {detection.bbox_y_min?.toFixed(1)}) - ({detection.bbox_x_max?.toFixed(1)}, {detection.bbox_y_max?.toFixed(1)})</Typography>
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </TableContainer>
              )}
            </Paper>
          </Grid>
        )}
      </Grid>
    </Container>
  );
};

export default Analyzer;
