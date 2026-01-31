import React from 'react';
import { Drawer, List, ListItem, ListItemIcon, ListItemText, Divider, ListItemButton } from '@mui/material';
import { Dashboard, CloudUpload, PhotoLibrary, Assessment, AutoAwesome } from '@mui/icons-material';
import { Link, useLocation } from 'react-router-dom';

const drawerWidth = 240;

const Sidebar = () => {
  const location = useLocation();

  const menuItems = [
    { text: 'Dashboard', icon: <Dashboard />, path: '/' },
    { text: 'Upload', icon: <CloudUpload />, path: '/upload' },
    { text: 'Gallery', icon: <PhotoLibrary />, path: '/gallery' },
    { text: 'Analyzer', icon: <AutoAwesome />, path: '/analyzer' },
    { text: 'Reports', icon: <Assessment />, path: '/reports' },
  ];

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          boxSizing: 'border-box',
        },
      }}
    >
      <Divider />
      <List>
        {menuItems.map((item) => (
          <ListItem key={item.text} selected={location.pathname === item.path}>
            <ListItemButton component={Link} to={item.path}>
              <ListItemIcon>
                {item.icon}
              </ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
};

export default Sidebar;