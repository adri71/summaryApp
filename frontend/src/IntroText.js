import React from 'react';
import './IntroText.css';

function IntroText({formData, setFormData, loading, handleSubmit  }) {
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
      };    

      const onSubmit = (e) => {
        e.preventDefault();
        handleSubmit();
      };

    return (
        <div className='comp1'>
        <form onSubmit={onSubmit}>
            <label><b>Enter the article to be summarized</b></label>
            <textarea
                name="articulo"
                placeholder="Copy the article here"
                value={formData.articulo}
                onChange={handleChange}
                rows="20"
                cols="110"
            />
            <br/>
            <label><b>Approximate word length of summary: </b></label>
            <input
                type="number"
                name="longitud"
                value={formData.longitud}
                onChange={handleChange}
                min="100"
                max="1000"
                placeholder="longitud"
            />
            <br/>
            <button className="b1" type="submit" disabled={loading}>
                {loading ? 'Simplifying...' : 'Simplify'}
            </button>
        </form>
        </div>
    );
    }

export default IntroText;
