import React, { useState, useEffect } from 'react';
import { Grid, Box, Typography, Button, Card, CardContent, TextField, CircularProgress, Alert } from '@mui/material';
import { useParams } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import apiClient, { API_BASE_URL } from '../config/api';

const ImageViewer = () => {
  const { id } = useParams();
  const [image, setImage] = useState(null);
  const [detections, setDetections] = useState([]);
  const [editing, setEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { user } = useAuth();

  // Helper function to normalize image URL
  const normalizeImageUrl = (url) => {
    if (!url) return 'https://via.placeholder.com/600x400';
    if (url.startsWith('/')) {
      return `${API_BASE_URL}${url}`;
    }
    return url;
  };

  useEffect(() => {
    const fetchImageData = async () => {
      try {
        setLoading(true);
        // Récupérer l'image
        const imageResponse = await apiClient.get(`/images/${id}`);
        setImage(imageResponse.data);

        // Récupérer les détections
        const detectionsResponse = await apiClient.get(`/images/${id}/detections`);
        setDetections(detectionsResponse.data);
        setError(null);
      } catch (err) {
        setError('Erreur lors du chargement de l\'image');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    if (user && id) {
      fetchImageData();
    }
  }, [id, user]);

  const handleSave = () => {
    // Sauvegarder les modifications (à implémenter avec PUT)
    setEditing(false);
  };

  if (!user) {
    return <Alert severity="info">Veuillez vous connecter pour accéder à cette page</Alert>;
  }

  if (loading) {
    return <Box display="flex" justifyContent="center" mt={4}><CircularProgress /></Box>;
  }

  if (error) {
    return <Alert severity="error">{error}</Alert>;
  }

  if (!image) {
    return <Alert severity="warning">Image non trouvée</Alert>;
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Visualiseur d'Image
      </Typography>

      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 8 }}>
          <Box sx={{ position: 'relative', display: 'inline-block', width: '100%' }}>
            <img
              src={normalizeImageUrl(image.url)}
              alt={image.filename || `#${image.id}`}
              style={{ width: '100%', height: 'auto', display: 'block' }}
            />
            {/* Bounding boxes des détections */}
            {detections.map((detection) => {
              const leftPercent = (detection.bbox_x_min / (image.width || 600)) * 100;
              const topPercent = (detection.bbox_y_min / (image.height || 400)) * 100;
              const widthPercent = ((detection.bbox_x_max - detection.bbox_x_min) / (image.width || 600)) * 100;
              const heightPercent = ((detection.bbox_y_max - detection.bbox_y_min) / (image.height || 400)) * 100;
              const borderColor = detection.validated === 'validated' ? 'green' : 'red';

              return (
                <Box
                  key={detection.id}
                  sx={{
                    position: 'absolute',
                    border: `2px solid ${borderColor}`,
                    left: `${leftPercent}%`,
                    top: `${topPercent}%`,
                    width: `${widthPercent}%`,
                    height: `${heightPercent}%`,
                  }}
                >
                  <Typography
                    variant="caption"
                    sx={{
                      bgcolor: borderColor,
                      color: 'white',
                      p: 0.5,
                      display: 'block',
                    }}
                  >
                    {detection.species_name} ({Math.round(detection.confidence_score * 100)}%)
                  </Typography>
                </Box>
              );
            })}
          </Box>
        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Détails
              </Typography>
              <Typography>Projet ID: {image.project_id}</Typography>
              <Typography>Dimensions: {image.width}x{image.height}</Typography>

              <Box sx={{ mt: 2 }}>
                <Typography variant="h6" gutterBottom>
                  Détections ({detections.length})
                </Typography>
                {detections.map((detection) => (
                  <Box key={detection.id} sx={{ mb: 1 }}>
                    {editing ? (
                      <TextField
                        fullWidth
                        label="Espèce"
                        defaultValue={detection.species_name}
                        size="small"
                      />
                    ) : (
                      <>
                        <Typography variant="body2">{detection.species_name}</Typography>
                        <Typography variant="caption" color="textSecondary">
                          Confiance: {Math.round(detection.confidence_score * 100)}%
                        </Typography>
                      </>
                    )}
                  </Box>
                ))}
              </Box>

              <Box sx={{ mt: 2 }}>
                {editing ? (
                  <>
                    <Button variant="contained" onClick={handleSave} sx={{ mr: 1 }}>
                      Sauvegarder
                    </Button>
                    <Button onClick={() => setEditing(false)}>
                      Annuler
                    </Button>
                  </>
                ) : (
                  <Button variant="outlined" onClick={() => setEditing(true)}>
                    Éditer
                  </Button>
                )}
              </Box>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default ImageViewer;