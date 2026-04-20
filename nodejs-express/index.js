const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.get('/healthz', (req, res) => {
  res.send('OK');
});

app.get('/', (req, res) => {
  const logLevel = process.env.LOG_LEVEL || 'info';
  res.send(`Hello from Node.js Express! (Log Level: ${logLevel})`);
});

app.listen(port, () => {
  console.log(`Server starting on port ${port}...`);
});
