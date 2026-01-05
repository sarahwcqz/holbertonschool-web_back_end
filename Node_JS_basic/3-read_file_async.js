const fs = require('node:fs/promises');

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    const lines = data.trim().split('\n');
    const numberOfStudents = lines.length - 1;
    console.log(`Number of students: ${numberOfStudents}`);

    // all students + removing header (ie first line)
    const students = lines.slice(1);

    const fields = {};

    students.forEach((line) => {
      // eslint-disable-next-line no-unused-vars
      const [firstname, lastname, age, field] = line.split(',');
      // if field not already in fields
      if (!fields[field]) {
        fields[field] = [];
      }
      // adding name to field
      fields[field].push(firstname);
    });

    // display msg for each field
    for (const field in fields) {
      if (Object.hasOwn(fields, field)) {
        const list = fields[field];
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
