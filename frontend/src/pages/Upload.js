import React, { useState, useCallback } from 'react';
import { Grid, Box, Typography, Button, TextField, FormControl, InputLabel, Select, MenuItem, Paper, Dialog, DialogTitle, DialogContent, DialogActions, Alert, Snackbar, CircularProgress } from '@mui/material';
import { useDropzone } from 'react-dropzone';
import apiClient from '../config/api';

const Upload = () => {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [projectId, setProjectId] = useState('');
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [capturedAt, setCapturedAt] = useState('');
  const [projects, setProjects] = useState([]);
  const [loadingProjects, setLoadingProjects] = useState(false);
  const [error, setError] = useState(null);
  const [openCreateDialog, setOpenCreateDialog] = useState(false);
  const [newProjectName, setNewProjectName] = useState('');
  const [newProjectDescription, setNewProjectDescription] = useState('');
  const [newProjectIsPublic, setNewProjectIsPublic] = useState(false);
  const [snackbar, setSnackbar] = useState({ open: false, message: '', severity: 'success' });

  // Récupération réelle des projets
  React.useEffect(() => {
    const fetchProjects = async () => {
      try {
        setLoadingProjects(true);
        const response = await apiClient.get('/projects');
        setProjects(response.data);
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

  const onDrop = useCallback((acceptedFiles) => {
    setSelectedFiles(acceptedFiles);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'image/*': [] },
    multiple: true,
  });

  const handleUpload = async () => {
    if (!projectId || selectedFiles.length === 0) {
      setSnackbar({ open: true, message: 'Veuillez sélectionner un projet et des fichiers', severity: 'error' });
      return;
    }

    const formData = new FormData();
    const isBulk = selectedFiles.length > 1;
    const endpoint = isBulk ? '/images/bulk-upload' : '/images/upload';
    const fileField = isBulk ? 'files' : 'file';

    selectedFiles.forEach((file) => {
      formData.append(fileField, file);
    });
    formData.append('project_id', projectId);
    if (latitude.trim()) {
      formData.append('latitude', latitude);
    }
    if (longitude.trim()) {
      formData.append('longitude', longitude);
    }
    if (capturedAt) {
      formData.append('captured_at', capturedAt);
    }

    try {
      await apiClient.post(endpoint, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setSnackbar({ open: true, message: 'Upload réussi', severity: 'success' });
      setSelectedFiles([]);
      setCapturedAt('');
      setLatitude('');
      setLongitude('');
      // Recharger les projets pour voir le nombre d'images mis à jour
      const response = await apiClient.get('/projects');
      setProjects(response.data);
    } catch (error) {
      setSnackbar({ open: true, message: 'Erreur lors de l\'upload', severity: 'error' });
      console.error(error);
    }
  };

  const handleCreateProject = async () => {
    if (!newProjectName.trim()) {
      setSnackbar({ open: true, message: 'Le nom du projet est requis', severity: 'error' });
      return;
    }
    try {
      const response = await apiClient.post('/projects', {
        name: newProjectName,
        description: newProjectDescription || null,
        is_public: newProjectIsPublic,
      });
      setProjects([...projects, response.data]);
      setSnackbar({ open: true, message: 'Projet créé avec succès', severity: 'success' });
      setOpenCreateDialog(false);
      setNewProjectName('');
      setNewProjectDescription('');
      setNewProjectIsPublic(false);
    } catch (err) {
      setSnackbar({ open: true, message: 'Erreur lors de la création du projet', severity: 'error' });
      console.error(err);
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Upload d'Images
      </Typography>
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 6 }}>
          <Box sx={{ display: 'flex', gap: 2, alignItems: 'flex-start' }}>
            <FormControl fullWidth margin="normal">
              <InputLabel>Sélectionner un Projet</InputLabel>
              <Select
                value={projectId}
                onChange={(e) => setProjectId(e.target.value)}
                disabled={loadingProjects}
              >
                {loadingProjects ? (
                  <MenuItem disabled>
                    <CircularProgress size={20} /> Chargement...
                  </MenuItem>
                ) : projects.length === 0 ? (
                  <MenuItem disabled>Aucun projet disponible</MenuItem>
                ) : (
                  projects.map((project) => (
                    <MenuItem key={project.id} value={project.id}>
                      {project.name} ({project.image_count ?? 0} images)
                    </MenuItem>
                  ))
                )}
              </Select>
            </FormControl>
            <Button
              variant="outlined"
              onClick={() => setOpenCreateDialog(true)}
              sx={{ mt: 2, minWidth: '150px' }}
            >
              Nouveau Projet
            </Button>
          </Box>
        </Grid>

        <Grid xs={12}>
          <Paper
            {...getRootProps()}
            sx={{
              p: 3,
              textAlign: 'center',
              border: '2px dashed #ccc',
              cursor: 'pointer',
              bgcolor: isDragActive ? '#f0f0f0' : 'transparent',
            }}
          >
            <input {...getInputProps()} />
            {isDragActive ? (
              <Typography>Déposez les fichiers ici...</Typography>
            ) : (
              <Typography>
                Glissez-déposez vos images ici, ou cliquez pour parcourir
              </Typography>
            )}
          </Paper>
          {selectedFiles.length > 0 && (
            <Typography variant="body2" sx={{ mt: 1 }}>
              {selectedFiles.length} fichier(s) sélectionné(s)
            </Typography>
          )}
        </Grid>

        <Grid xs={12} md={6}>
          <TextField
            fullWidth
            label="Latitude"
            type="number"
            value={latitude}
            onChange={(e) => setLatitude(e.target.value)}
            margin="normal"
          />
        </Grid>
        <Grid xs={12} md={6}>
          <TextField
            fullWidth
            label="Longitude"
            type="number"
            value={longitude}
            onChange={(e) => setLongitude(e.target.value)}
            margin="normal"
          />
        </Grid>
        <Grid xs={12} md={6}>
          <TextField
            fullWidth
            label="Date de capture"
            type="datetime-local"
            value={capturedAt}
            onChange={(e) => setCapturedAt(e.target.value)}
            InputLabelProps={{ shrink: true }}
            margin="normal"
          />
        </Grid>

        <Grid xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleUpload}
            disabled={!projectId || selectedFiles.length === 0}
          >
            Uploader
          </Button>
        </Grid>
      </Grid>

      {/* Dialog de création de projet */}
      <Dialog open={openCreateDialog} onClose={() => setOpenCreateDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Créer un Nouveau Projet</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Nom du Projet"
            fullWidth
            required
            value={newProjectName}
            onChange={(e) => setNewProjectName(e.target.value)}
          />
          <TextField
            margin="dense"
            label="Description"
            fullWidth
            multiline
            rows={3}
            value={newProjectDescription}
            onChange={(e) => setNewProjectDescription(e.target.value)}
          />
          <FormControl fullWidth margin="dense">
            <InputLabel>Visibilité</InputLabel>
            <Select
              value={newProjectIsPublic}
              onChange={(e) => setNewProjectIsPublic(e.target.value)}
            >
              <MenuItem value={false}>Privé</MenuItem>
              <MenuItem value={true}>Public</MenuItem>
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenCreateDialog(false)}>Annuler</Button>
          <Button onClick={handleCreateProject} variant="contained" color="primary">
            Créer
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar
        open={snackbar.open}
        autoHideDuration={6000}
        onClose={() => setSnackbar({ ...snackbar, open: false })}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert onClose={() => setSnackbar({ ...snackbar, open: false })} severity={snackbar.severity}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default Upload;