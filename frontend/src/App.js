import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import IntroText from './IntroText';
import OutText from './OutText';
import About from './About';

function App() {
  const [formData, setFormData] = useState({
    articulo: '',
    resumen: '',
    longitud: '100'
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [showAbout, setShowAbout] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await axios.post('/api/data', formData);
      setFormData({ ...formData, resumen: res.data.resumen });
    } catch (error) {
      console.error('Error sending data:', error);
      if (error.response && error.response.data.error) {
        setError(error.response.data.error);  // Mostrar el error si viene del backend
      }
      else if (error.request) {
        setError('Could not connect to the server. Please try again later.');
      }   
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="App">
      <header className="App-header">
        <div className='titulo-container'>
          <h1>Summary App</h1>
          <p>Text summary and simplification application</p>
        </div>
        <div className="button-container">
          <button className="b2" onClick={() => setShowAbout(true)}>
            About this app
          </button>
        </div>
      </header>
      <main>
        {showAbout ? (
          <About setShowAbout={setShowAbout} />  
        ) : (
          formData.resumen ? (
            <OutText
              formData={formData}
              setFormData={setFormData}
              loading={loading}
              handleSubmit={handleSubmit}
            />
          ) : (
            <IntroText
              formData={formData}
              setFormData={setFormData}
              loading={loading}
              handleSubmit={handleSubmit}
            />
          )
        )}
        {error && <p className="error">{error}</p>}
      </main>
    </div>
  );
}

export default App;
