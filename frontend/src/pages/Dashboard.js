import React, { useState, useEffect } from 'react';
import { Grid, Card, CardContent, Typography, Button, Box, List, ListItem, ListItemText, CircularProgress, Alert } from '@mui/material';
import { Link } from 'react-router-dom';
import apiClient from '../config/api';

const Dashboard = () => {
  const [stats, setStats] = useState({
    imagesProcessed: 0,
    speciesDetected: 0,
    activeProjects: 0,
  });
  const [recentProjects, setRecentProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        setLoading(true);
        const response = await apiClient.get('/projects');
        const projects = Array.isArray(response.data) ? response.data : [];

        // Trier les projets par created_at décroissant
        const sortedProjects = projects
          .slice()
          .sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

        // Calculer les statistiques globales
        const imagesProcessed = projects.reduce((sum, p) => sum + (p.image_count || 0), 0);
        const detectionsCount = projects.reduce((sum, p) => sum + (p.detection_count || 0), 0);
        const activeProjects = projects.length;

        setStats({
          imagesProcessed,
          speciesDetected: detectionsCount,
          activeProjects,
        });

        // Prendre les 3 premiers projets triés comme récents
        setRecentProjects(
          sortedProjects.slice(0, 3).map((p) => ({
            id: p.id,
            name: p.name,
            imageCount: p.image_count || 0,
          }))
        );
        setError(null);
      } catch (err) {
        console.error('Dashboard error:', err);
        setError('Erreur lors du chargement du dashboard');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  if (loading) {
    return <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '400px' }}><CircularProgress /></Box>;
  }

  if (error) {
    return <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>;
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* Statistiques Clés */}
        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>
                Images traitées
              </Typography>
              <Typography variant="h5">
                {stats.imagesProcessed}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>
                Espèces détectées
              </Typography>
              <Typography variant="h5">
                {stats.speciesDetected}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>
                Projets actifs
              </Typography>
              <Typography variant="h5">
                {stats.activeProjects}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        {/* Actions Rapides */}
        <Grid size={{ xs: 12, md: 6 }}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Actions Rapides
              </Typography>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                <Button variant="contained" component={Link} to="/upload">
                  Upload Images
                </Button>
                <Button variant="outlined" component={Link} to="/gallery">
                  Voir Gallery
                </Button>
                <Button variant="outlined" component={Link} to="/reports">
                  Générer Rapport
                </Button>
              </Box>
            </CardContent>
          </Card>
        </Grid>

        {/* Projets Récents */}
        <Grid size={{ xs: 12, md: 6 }}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Projets Récents
              </Typography>
              <List>
                {recentProjects.map((project) => (
                  <ListItem key={project.id}>
                    <ListItemText
                      primary={project.name}
                      secondary={`${project.imageCount} images`}
                    />
                  </ListItem>
                ))}
              </List>
            </CardContent>
          </Card>
        </Grid>

        {/* Notifications */}
        <Grid xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Résumé
              </Typography>
              <Typography variant="body2">
                {stats.imagesProcessed} images traitées dans {stats.activeProjects} projets actifs
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard;