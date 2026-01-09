import routes from './routes/index.js'
import express from 'express';

const app = express();

// using a middleware: all routes that start with / go through routes (imported from index)
app.use('/', routes)

app.listen(1245);

export default app;
