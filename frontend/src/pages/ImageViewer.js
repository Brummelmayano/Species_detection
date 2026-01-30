import React, { useState, useEffect } from 'react';
import { Box, Typography, Button, Grid, Card, CardContent, TextField } from '@mui/material';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ImageViewer = () => {
  const { id } = useParams();
  const [image, setImage] = useState(null);
  const [detections, setDetections] = useState([]);
  const [editing, setEditing] = useState(false);

  useEffect(() => {
    // Simuler récupération de l'image et détections
    setImage({
      id: id,
      url: 'https://via.placeholder.com/600x400',
      species: 'Lion',
      projectId: 1,
    });
    setDetections([
      { id: 1, species: 'Lion', confidence: 0.95, bbox: [10, 20, 100, 150] },
    ]);
  }, [id]);

  const handleSave = () => {
    // Sauvegarder les modifications
    setEditing(false);
  };

  if (!image) return <Typography>Chargement...</Typography>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Visualiseur d'Image
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Box sx={{ position: 'relative' }}>
            <img
              src={image.url}
              alt={image.species}
              style={{ width: '100%', height: 'auto' }}
            />
            {/* Simuler boîtes de délimitation */}
            {detections.map((detection) => (
              <Box
                key={detection.id}
                sx={{
                  position: 'absolute',
                  border: '2px solid red',
                  left: `${detection.bbox[0]}px`,
                  top: `${detection.bbox[1]}px`,
                  width: `${detection.bbox[2] - detection.bbox[0]}px`,
                  height: `${detection.bbox[3] - detection.bbox[1]}px`,
                }}
              >
                <Typography
                  variant="caption"
                  sx={{
                    bgcolor: 'red',
                    color: 'white',
                    p: 0.5,
                  }}
                >
                  {detection.species} ({Math.round(detection.confidence * 100)}%)
                </Typography>
              </Box>
            ))}
          </Box>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Détails
              </Typography>
              <Typography>Espèce: {image.species}</Typography>
              <Typography>Projet: {image.projectId}</Typography>

              <Box sx={{ mt: 2 }}>
                <Typography variant="h6" gutterBottom>
                  Détections
                </Typography>
                {detections.map((detection) => (
                  <Box key={detection.id} sx={{ mb: 1 }}>
                    {editing ? (
                      <TextField
                        fullWidth
                        label="Espèce"
                        defaultValue={detection.species}
                      />
                    ) : (
                      <Typography>{detection.species}</Typography>
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