import React, { useState, useEffect } from 'react';
import { Grid, Box, Typography, Card, CardContent, FormControl, InputLabel, Select, MenuItem, TextField, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Alert, CircularProgress } from '@mui/material';
import apiClient from '../config/api';

const Reports = () => {
  const [reportType, setReportType] = useState('species');
  const [projectId, setProjectId] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [reportData, setReportData] = useState(null);
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await apiClient.get('/projects');
        setProjects(Array.isArray(response.data) ? response.data : []);
      } catch (err) {
        console.error('Error loading projects:', err);
      }
    };
    fetchProjects();
  }, []);

  const handleGenerateReport = () => {
    if (!reportType || !projectId) {
      setError('Veuillez sélectionner un type de rapport et un projet');
      return;
    }
    setLoading(true);
    setError(null);
    
    // Simuler génération de rapport
    setTimeout(() => {
      setReportData({
        species: [
          { name: 'Lion', count: 10 },
          { name: 'Éléphant', count: 5 },
          { name: 'Girafe', count: 3 },
        ],
        totalImages: 50,
        period: startDate && endDate ? `${startDate} - ${endDate}` : 'Toute la période',
      });
      setLoading(false);
    }, 1000);
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Rapports
      </Typography>

      {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

      <Grid container spacing={3}>
        <Grid size={{ xs: 12 }}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Générer un Rapport
              </Typography>
              <Grid container spacing={2}>
                <Grid size={{ xs: 12, md: 3 }}>
                  <FormControl fullWidth>
                    <InputLabel>Type de Rapport</InputLabel>
                    <Select
                      value={reportType}
                      onChange={(e) => setReportType(e.target.value)}
                    >
                      <MenuItem value="species">Par Espèces</MenuItem>
                      <MenuItem value="temporal">Tendances Temporelles</MenuItem>
                      <MenuItem value="distribution">Distribution Géographique</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>
                <Grid size={{ xs: 12, md: 3 }}>
                  <FormControl fullWidth>
                    <InputLabel>Projet</InputLabel>
                    <Select
                      value={projectId}
                      onChange={(e) => setProjectId(e.target.value)}
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
                    label="Date de début"
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                  />
                </Grid>
                <Grid size={{ xs: 12, md: 3 }}>
                  <TextField
                    fullWidth
                    label="Date de fin"
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                  />
                </Grid>
                <Grid size={{ xs: 12 }}>
                  <Button variant="contained" onClick={handleGenerateReport} disabled={loading}>
                    {loading ? <CircularProgress size={20} color="inherit" /> : 'Générer Rapport'}
                  </Button>
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>

        {reportData && (
          <>
            <Grid size={{ xs: 12, md: 6 }}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Statistiques
                  </Typography>
                  <Typography>Total d'images: {reportData.totalImages}</Typography>
                  <Typography>Période: {reportData.period}</Typography>
                </CardContent>
              </Card>
            </Grid>

            <Grid size={{ xs: 12, md: 6 }}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Espèces Détectées
                  </Typography>
                  <TableContainer component={Paper}>
                    <Table>
                      <TableHead>
                        <TableRow>
                          <TableCell>Espèce</TableCell>
                          <TableCell align="right">Nombre</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {reportData.species.map((row) => (
                          <TableRow key={row.name}>
                            <TableCell>{row.name}</TableCell>
                            <TableCell align="right">{row.count}</TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </CardContent>
              </Card>
            </Grid>
          </>
        )}
      </Grid>
    </Box>
  );
};

export default Reports;