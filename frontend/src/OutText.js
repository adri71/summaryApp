import React from 'react';
import './OutText.css';
import * as pdfjsLib from 'pdfjs-dist/legacy/build/pdf';
import pdfjsWorker from 'pdfjs-dist/legacy/build/pdf.worker.entry'; // Necesario para que PDF.js funcione en React

function OutText({ formData, setFormData, loading, handleSubmit }) {
  // Maneja el cambio de valores manualmente
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Lee el archivo PDF y actualiza el textarea
  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = async function () {
        const typedArray = new Uint8Array(this.result);
        const pdf = await pdfjsLib.getDocument({ data: typedArray }).promise;
        let extractedText = '';
        for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
          const page = await pdf.getPage(pageNum);
          const textContent = await page.getTextContent();
          const pageText = textContent.items.map((item) => item.str).join(' ');
          extractedText += pageText + '\n';
        }
        // Actualiza el texto extraído en el textarea
        setFormData({ ...formData, articulo: extractedText });
      };
      reader.readAsArrayBuffer(file);
    }
  };

  const onSubmit = (e) => {
    e.preventDefault();
    handleSubmit();
  };

  return (
    <div className='comp2'>
      <form onSubmit={onSubmit}>
        <div className='texto'>
          <div className='c1'>
            <label><b>Original article</b></label>
            <textarea
              className='ta'
              name="articulo"
              value={formData.articulo}
              onChange={handleChange}
              rows="20"
              cols="60"
            />
          </div>
          <div className='c2'>
            <label><b>Simplified summary</b></label>
            {loading ? <p>Generating the summary, please wait...</p> : <p>{formData.resumen}</p>}
          </div>
        </div>
        <div className='cargarPDF'>
            <label><b>Upload the article in PDF format: </b></label>
            <input type="file" accept="application/pdf" onChange={handleFileChange} />
        </div>
        <label><b>Approximate word length of summary:</b></label>
        <input
          type="number"
          name="longitud"
          value={formData.longitud}
          onChange={handleChange}
          min="100"
          max="1000"
        />
        <br/>
        <button className="b1" type="submit" disabled={loading}>
          {loading ? 'Simplifying...' : 'Simplify'}
        </button>
      </form>
    </div>
  );
}

export default OutText;
