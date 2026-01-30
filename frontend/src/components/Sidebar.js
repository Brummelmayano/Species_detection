import React from 'react';
import { Drawer, List, ListItem, ListItemIcon, ListItemText, Divider } from '@mui/material';
import { Dashboard, CloudUpload, PhotoLibrary, Image, Assessment } from '@mui/icons-material';
import { Link, useLocation } from 'react-router-dom';

const drawerWidth = 240;

const Sidebar = () => {
  const location = useLocation();

  const menuItems = [
    { text: 'Dashboard', icon: <Dashboard />, path: '/' },
    { text: 'Upload', icon: <CloudUpload />, path: '/upload' },
    { text: 'Gallery', icon: <PhotoLibrary />, path: '/gallery' },
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
          <ListItem
            button
            key={item.text}
            component={Link}
            to={item.path}
            selected={location.pathname === item.path}
          >
            <ListItemIcon>
              {item.icon}
            </ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
};

export default Sidebar;