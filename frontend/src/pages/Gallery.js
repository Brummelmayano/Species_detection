import React, { useState, useEffect } from 'react';
import { Grid, Box, Typography, Card, CardMedia, CardContent, TextField, FormControl, InputLabel, Select, MenuItem, Button, Pagination, CircularProgress, Alert } from '@mui/material';
import { Link } from 'react-router-dom';
import apiClient, { API_BASE_URL } from '../config/api';

const Gallery = () => {
  const [images, setImages] = useState([]);
  const [filters, setFilters] = useState({
    projectId: '',
    species: '',
    date: '',
  });
  const [projects, setProjects] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const LIMIT = 20;

  // Helper function to normalize image URL
  const normalizeImageUrl = (url) => {
    if (!url) return 'https://via.placeholder.com/200';
    if (url.startsWith('/')) {
      return `${API_BASE_URL}${url}`;
    }
    return url;
  };

  useEffect(() => {
    const fetchGalleryData = async () => {
      try {
        setLoading(true);
        // Récupérer les projets pour le filtre
        const projectsResponse = await apiClient.get('/projects/');
        setProjects(projectsResponse.data);

        // Récupérer les images avec pagination
        const params = {
          skip: (page - 1) * LIMIT,
          limit: LIMIT,
        };
        if (filters.projectId) {
          params.project_id = filters.projectId;
        }

        const imagesResponse = await apiClient.get('/images/', { params });
        setImages(imagesResponse.data);

        // Améliorer le calcul de totalPages
        // Si la réponse retourne le nombre exact ou si on a reçu LIMIT éléments, on peut estimer qu'il y a plus
        setTotalPages((prev) => {
          if (imagesResponse.data.length === LIMIT) {
            return Math.max(prev, page + 1);
          }
          return Math.max(prev, page);
        });
        setError(null);
      } catch (err) {
        console.error('Gallery error:', err);
        setError('Erreur lors du chargement de la galerie');
      } finally {
        setLoading(false);
      }
    };

    fetchGalleryData();
  }, [page, filters.projectId]);

  if (loading) {
    return <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '400px' }}><CircularProgress /></Box>;
  }

  const handleFilterChange = (field, value) => {
    setFilters({ ...filters, [field]: value });
    setPage(1);
  };

  const handleSearch = () => {
    // Les filtres sont appliqués automatiquement via useEffect
    console.log('Recherche avec filtres:', filters);
  };

  if (error) {
    return <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>;
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Galerie d'Images
      </Typography>

      {/* Filtres */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid size={{ xs: 12, md: 3 }}>
          <FormControl fullWidth>
            <InputLabel>Projet</InputLabel>
            <Select
              value={filters.projectId}
              onChange={(e) => handleFilterChange('projectId', e.target.value)}
            >
              <MenuItem value="">Tous</MenuItem>
              {projects.map((project) => (
                <MenuItem key={project.id} value={project.id}>
                  {project.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Grid>
        <Grid size={{ xs: 12, md: 3 }}>
          <TextField
            fullWidth
            label="Espèce"
            value={filters.species}
            onChange={(e) => handleFilterChange('species', e.target.value)}
          />
        </Grid>
        <Grid size={{ xs: 12, md: 3 }}>
          <TextField
            fullWidth
            label="Date"
            type="date"
            value={filters.date}
            onChange={(e) => handleFilterChange('date', e.target.value)}
            InputLabelProps={{ shrink: true }}
          />
        </Grid>
        <Grid size={{ xs: 12, md: 3 }}>
          <Button variant="contained" onClick={handleSearch} fullWidth>
            Rechercher
          </Button>
        </Grid>
      </Grid>

      {/* Grille d'images */}
      <Grid container spacing={2}>
        {images.map((image) => (
          <Grid size={{ xs: 12, sm: 6, md: 4, lg: 3 }} key={image.id}>
            <Card component={Link} to={`/image/${image.id}`} sx={{ textDecoration: 'none' }}>
              <CardMedia
                component="img"
                height="200"
                image={normalizeImageUrl(image.url)}
                alt={`Image ${image.id}`}
              />
              <CardContent>
                <Typography variant="body2" color="text.secondary">
                  {image.detection_count || 0} détections
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* Pagination */}
      <Box sx={{ display: 'flex', justifyContent: 'center', mt: 3 }}>
        <Pagination
          count={totalPages}
          page={page}
          onChange={(event, value) => setPage(value)}
        />
      </Box>
    </Box>
  );
};

export default Gallery;