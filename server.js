const express = require('express');
const axios = require('axios');
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');
require('dotenv').config();

const app = express();
const port = 3000;
const base_url = "https://xbl.io/api/v2/";

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.get('/', (req, res) => {
    res.redirect('/api-docs');
});

app.get('/get-xbox-account-info', async (req, res) => {
    const public_key = process.env.PUBLIC_KEY || 'default_public_key';
    const headers = {'X-Authorization': public_key};

    try {
        const response = await axios.get(`${base_url}account`, {headers});
        res.json(response.data);
    } catch (error) {
        res.json({"error": `Failed to retrieve data: Status code ${error.response.status}`});
    }
});

app.get('/player-summary', async (req, res) => {
    const public_key = process.env.PUBLIC_KEY || 'default_public_key';
    const headers = {'X-Authorization': public_key};

    try {
        const response = await axios.get(`${base_url}player/summary`, {headers});
        res.json(response.data);
    } catch (error) {
        res.json({"error": `Failed to retrieve data: Status code ${error.response.status}`});
    }
});

app.get('/friends', async (req, res) => {
    const public_key = process.env.PUBLIC_KEY || 'default_public_key';
    const headers = {'X-Authorization': public_key};

    try {
        const response = await axios.get(`${base_url}friends`, {headers});
        res.json(response.data);
    } catch (error) {
        res.json({"error": `Failed to retrieve data: Status code ${error.response.status}`});
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});