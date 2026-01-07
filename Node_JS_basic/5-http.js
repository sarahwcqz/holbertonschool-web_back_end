const http = require('node:http');
const countStudents = require('./3-read_file_async');
const db = process.argv[2];

const app = http.createServer((request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain');

    if (request.url === '/') {
        response.end('Hello Holberton School!');
    } else if (request.url === '/students') {
        response.write('This is the list of our students');

        countStudents(db)
            .then(data => response.end(data))
            .catch(() => response.end('Cannot load the database'));
    }
});

app.listen(1245);

module.exports = app;
