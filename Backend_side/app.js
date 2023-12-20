const express = require('express')
const app = express()
const fs = require('fs')
const axios = require('axios')

const PORT = 3000

app.use(express.static('/public'))

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
