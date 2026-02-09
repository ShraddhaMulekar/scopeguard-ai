import React from 'react'
import { useLocation } from 'react-router-dom';

const DebugLocation = () => {
  const location = useLocation();
  // console.log("Current path:", location.pathname);
  return null;
}

export default DebugLocation