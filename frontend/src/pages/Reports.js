import React, { useState } from 'react';
import { Box, Typography, Grid, Card, CardContent, FormControl, InputLabel, Select, MenuItem, TextField, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const Reports = () => {
  const [reportType, setReportType] = useState('');
  const [projectId, setProjectId] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [reportData, setReportData] = useState(null);
  const [projects] = useState([
    { id: 1, name: 'Projet A' },
    { id: 2, name: 'Projet B' },
  ]);

  const handleGenerateReport = () => {
    // Simuler génération de rapport
    setReportData({
      species: [
        { name: 'Lion', count: 10 },
        { name: 'Éléphant', count: 5 },
        { name: 'Girafe', count: 3 },
      ],
      totalImages: 50,
      period: `${startDate} - ${endDate}`,
    });
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Rapports
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Générer un Rapport
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} md={3}>
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
                <Grid item xs={12} md={3}>
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
                <Grid item xs={12} md={3}>
                  <TextField
                    fullWidth
                    label="Date de début"
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                  />
                </Grid>
                <Grid item xs={12} md={3}>
                  <TextField
                    fullWidth
                    label="Date de fin"
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                  />
                </Grid>
                <Grid item xs={12}>
                  <Button variant="contained" onClick={handleGenerateReport}>
                    Générer Rapport
                  </Button>
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>

        {reportData && (
          <>
            <Grid item xs={12} md={6}>
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

            <Grid item xs={12} md={6}>
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