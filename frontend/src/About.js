import React from 'react';
import './About.css';

function About({ setShowAbout }) {  // Recibe setShowAbout como prop
  return (
    <div className="about">
      <h2>About This App</h2>
      <p>
        This is a text summarization and simplification application. You can enter an article,
        choose the desired summary length, and the app will generate a simplified version
        of the article for you. This simplification is done using NLP models.
      </p>
      <button className="b1" onClick={() => setShowAbout(false)}>
        Go Back
      </button>
    </div>
  );
}

export default About;
