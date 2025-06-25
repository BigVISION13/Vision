import React, { useState } from 'react';
import axios from 'axios';

const styles = [
  'Consultative Selling',
  'Challenger Sale',
  'Solution Selling',
  'Social Selling',
];

function SalesResponseGenerator() {
  const [context, setContext] = useState('');
  const [style, setStyle] = useState(styles[0]);
  const [response, setResponse] = useState('');

  const handleGenerate = async () => {
    try {
      const res = await axios.post('http://localhost:5000/generate-response', {
        context,
        style,
      });
      setResponse(res.data.response);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>AI Response Generator</h2>
      <textarea
        value={context}
        onChange={(e) => setContext(e.target.value)}
        placeholder="Enter prospect info or context"
      />
      <select value={style} onChange={(e) => setStyle(e.target.value)}>
        {styles.map((s) => (
          <option key={s} value={s}>
            {s}
          </option>
        ))}
      </select>
      <button onClick={handleGenerate}>Generate Response</button>
      {response && (
        <p>
          <strong>Generated Response:</strong> {response}
        </p>
      )}
    </div>
  );
}

export default SalesResponseGenerator;
