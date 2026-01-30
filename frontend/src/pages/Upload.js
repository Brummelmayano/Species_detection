import React, { useState, useCallback } from 'react';
import { Box, Typography, Button, TextField, FormControl, InputLabel, Select, MenuItem, Paper, Grid } from '@mui/material';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const Upload = () => {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [projectId, setProjectId] = useState('');
  const [metadata, setMetadata] = useState({
    date: '',
    location: '',
  });
  const [projects, setProjects] = useState([]);

  // Simuler récupération des projets
  React.useEffect(() => {
    setProjects([
      { id: 1, name: 'Projet A' },
      { id: 2, name: 'Projet B' },
    ]);
  }, []);

  const onDrop = useCallback((acceptedFiles) => {
    setSelectedFiles(acceptedFiles);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: 'image/*',
    multiple: true,
  });

  const handleUpload = async () => {
    if (!projectId || selectedFiles.length === 0) {
      alert('Veuillez sélectionner un projet et des fichiers');
      return;
    }

    const formData = new FormData();
    selectedFiles.forEach((file) => {
      formData.append('file', file);
    });
    formData.append('project_id', projectId);
    formData.append('metadata', JSON.stringify(metadata));

    try {
      await axios.post('http://localhost:8000/images/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      alert('Upload réussi');
      setSelectedFiles([]);
    } catch (error) {
      alert('Erreur lors de l\'upload');
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Upload d'Images
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <FormControl fullWidth margin="normal">
            <InputLabel>Sélectionner un Projet</InputLabel>
            <Select
              value={projectId}
              onChange={(e) => setProjectId(e.target.value)}
            >
              {projects.map((project) => (
                <MenuItem key={project.id} value={project.id}>
                  {project.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Grid>

        <Grid item xs={12}>
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

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Date"
            type="date"
            value={metadata.date}
            onChange={(e) => setMetadata({ ...metadata, date: e.target.value })}
            InputLabelProps={{ shrink: true }}
            margin="normal"
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Localisation GPS"
            value={metadata.location}
            onChange={(e) => setMetadata({ ...metadata, location: e.target.value })}
            margin="normal"
          />
        </Grid>

        <Grid item xs={12}>
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
    </Box>
  );
};

export default Upload;