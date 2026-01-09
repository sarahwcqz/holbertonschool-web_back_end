import fs from 'node:fs/promises';

async function readDatabase(path) {
    try {
        const data = await fs.readFile(path, 'utf-8');
        
        const lines = data.trim().split('\n').slice(1);
        const fields = {};

        lines.forEach((line) =>{
            const [firstname, , , field] = line.split(',');

            if (!fields[field]) fields[field] = [];

            fields[field].push(firstname);
        });
        return fields;

    } catch (err) {
        throw err;
    }
}

export default readDatabase;
