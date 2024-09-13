import React from 'react';
import './OutText.css';

function OutText({ formData, setFormData, loading, handleSubmit }) {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
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
            <br/>
          </div>
          <div className='c2'>
            <label><b>Simplified summary</b></label>
            {loading ? <p>Generating the summary, please wait...</p> : <p>{formData.resumen}</p>}
          </div>
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
