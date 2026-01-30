import React, { useState, useEffect } from 'react';
import { Grid, Card, CardContent, Typography, Button, Box, List, ListItem, ListItemText } from '@mui/material';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Dashboard = () => {
  const [stats, setStats] = useState({
    imagesProcessed: 0,
    speciesDetected: 0,
    activeProjects: 0,
  });
  const [recentProjects, setRecentProjects] = useState([]);
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    // Simuler la récupération des données (remplacer par appels API réels)
    setStats({
      imagesProcessed: 1234,
      speciesDetected: 56,
      activeProjects: 3,
    });
    setRecentProjects([
      { id: 1, name: 'Projet A', imageCount: 50 },
      { id: 2, name: 'Projet B', imageCount: 120 },
      { id: 3, name: 'Projet C', imageCount: 75 },
    ]);
    setNotifications([
      'Traitement terminé pour batch XYZ',
      'Nouvelle espèce détectée',
    ]);
  }, []);

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* Statistiques Clés */}
        <Grid item xs={12} md={4}>
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
        <Grid item xs={12} md={4}>
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
        <Grid item xs={12} md={4}>
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
        <Grid item xs={12} md={6}>
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
        <Grid item xs={12} md={6}>
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
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Notifications
              </Typography>
              <List>
                {notifications.map((notification, index) => (
                  <ListItem key={index}>
                    <ListItemText primary={notification} />
                  </ListItem>
                ))}
              </List>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard;