import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { useAuth } from '../contexts/AuthContext';

const Header = () => {
  const { user, logout } = useAuth();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Species Detection
        </Typography>
        {user ? (
          <Box>
            <Typography variant="body1" sx={{ mr: 2 }}>
              {user.username}
            </Typography>
            <Button color="inherit" onClick={logout}>
              Déconnexion
            </Button>
          </Box>
        ) : (
          <Typography variant="body1">Non connecté</Typography>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Header;