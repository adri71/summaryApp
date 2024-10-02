import React from 'react';
import './About.css';

function About({ setShowAbout }) {  // Recibe setShowAbout como prop
  return (
    <div className="about">
      <h2>About This App</h2>
      <p>
        This is a text summarization and simplification application. You can enter an article,
        choose the desired summary length, and the app will generate a simplified version
        of the article for you. This simplification is done using NLP models. You can upload the article 
        you want to summarize by copying the text directly or uploading a PDF containing the text.  
        You can find the code for this application in the following GitHub directory: <a href="https://github.com/adri71/summaryApp" target="_blank">GitHub page with code</a>

      </p>
      <button className="b1" onClick={() => setShowAbout(false)}>
        Go Back
      </button>
    </div>
  );
}

export default About;
