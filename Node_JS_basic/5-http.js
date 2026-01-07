const http = require('node:http');
const fs = require('fs');

const app = http.createServer((request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain');

    if (request.url === '/') {
        response.end('Hello Holberton School!');
    } else if (request.url === '/students') {
        response.write('This is the list of our students\n');

        fs.readFile(process.argv[2], 'utf8', (err, data) => {
            if (err) {
                response.statusCode = 500;
                response.end('Cannot load the database');
                return;
            }

            const lines = data.trim().split('\n');
            const numberOfStudents = lines.length - 1;
            response.write(`Number of students: ${numberOfStudents}`);

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
                    response.write(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`);
                }
            }
            response.end();
        });
    } else {
        response.end('Hello Holberton School!');
    }
});

app.listen(1245);

module.exports = app;
