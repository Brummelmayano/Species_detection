import React, { useState, useEffect } from 'react';
import { Box, Typography, Grid, Card, CardMedia, CardContent, TextField, FormControl, InputLabel, Select, MenuItem, Button, Pagination } from '@mui/material';
import { Link } from 'react-router-dom';
import axios from 'axios';

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

  useEffect(() => {
    // Simuler récupération des projets et images
    setProjects([
      { id: 1, name: 'Projet A' },
      { id: 2, name: 'Projet B' },
    ]);
    setImages([
      { id: 1, url: 'https://via.placeholder.com/200', species: 'Espèce A', projectId: 1 },
      { id: 2, url: 'https://via.placeholder.com/200', species: 'Espèce B', projectId: 2 },
      // Ajouter plus d'images simulées
    ]);
    setTotalPages(5);
  }, [filters, page]);

  const handleFilterChange = (field, value) => {
    setFilters({ ...filters, [field]: value });
    setPage(1);
  };

  const handleSearch = () => {
    // Appliquer les filtres
    console.log('Recherche avec filtres:', filters);
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Galerie d'Images
      </Typography>

      {/* Filtres */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={12} md={3}>
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
        <Grid item xs={12} md={3}>
          <TextField
            fullWidth
            label="Espèce"
            value={filters.species}
            onChange={(e) => handleFilterChange('species', e.target.value)}
          />
        </Grid>
        <Grid item xs={12} md={3}>
          <TextField
            fullWidth
            label="Date"
            type="date"
            value={filters.date}
            onChange={(e) => handleFilterChange('date', e.target.value)}
            InputLabelProps={{ shrink: true }}
          />
        </Grid>
        <Grid item xs={12} md={3}>
          <Button variant="contained" onClick={handleSearch} fullWidth>
            Rechercher
          </Button>
        </Grid>
      </Grid>

      {/* Grille d'images */}
      <Grid container spacing={2}>
        {images.map((image) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={image.id}>
            <Card component={Link} to={`/image/${image.id}`} sx={{ textDecoration: 'none' }}>
              <CardMedia
                component="img"
                height="200"
                image={image.url}
                alt={image.species}
              />
              <CardContent>
                <Typography variant="body2" color="text.secondary">
                  {image.species}
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