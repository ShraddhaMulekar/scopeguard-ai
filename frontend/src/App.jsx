// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import AnalyzePage from './pages/AnalyzePage'

function App() {
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<AnalyzePage />} />
    </Routes>
  </BrowserRouter>
}

export default App
