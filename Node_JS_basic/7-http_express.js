const express = require('express');
const fs = require('fs');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const dbFile = process.argv[2];

  let output = 'This is the list of our students\n';

  fs.readFile(dbFile, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('Cannot load the database');
      return;
    }

    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.trim() !== '');
    output += `Number of students: ${students.length}\n`;

    const fields = {};

    students.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
    });

    const fieldNames = Object.keys(fields);
    fieldNames.forEach((field, index) => {
      output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      if (index !== fieldNames.length - 1) {
        output += '\n';
      }
    });

    res.send(output);
  });
});

app.listen(1245);

module.exports = app;
