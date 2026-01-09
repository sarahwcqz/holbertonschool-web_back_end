import readDatabase from '../utils.js';

class StudentsController {
    static async getAllStudents(request, response) {
        const db = process.argv[2];

        try {
            const fields = await readDatabase(db);
            response.status(200).set('Content-Type', 'text/plain')
            response.write('This is the list of our students\n');

            const fieldNames = Object.keys(fields).sort((a, b) =>
                a.toLowerCase().localeCompare(b.toLowerCase())
            );

            fieldNames.forEach((field, index) => {
                const names = fields[field];
                const numberOfStudents = names.length;
                let line = `Number of students in ${field}: ${numberOfStudents}. List: ${names.join(', ')}`;

                if (index !== fieldNames.length - 1) {
                    line += '\n';
                }

                response.write(line);
            });

            response.end();
        } catch (err) {
            response.status(500).send('Cannot load the database');
        }
    }


    static async getAllStudentsByMajor(request, response) {
        const db = process.argv[2];

        // puisqu'on def la route comme app.get('/students/:major', getAllStudentsByMajor);
        const specificField = request.params.major

        // verif param
        if (specificField !== 'CS' && specificField !== 'SWE') {
            return response.status(500).send('Major parameter must be CS or SWE')
        }

        try {
            const fields = await readDatabase(db);

            const names = fields[specificField];
            response.status(200).set('Content-Type', 'text/plain');
            response.send(`List: ${names.join(', ')}`)

        } catch (err) {
            response.status(500).send('Cannot load the database');
        }
    }
}

export default StudentsController;
