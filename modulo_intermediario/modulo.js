const fs = require('fs');
const path = require('path');

require('cross-fetch/polyfill');

pessoas= [
    {nome: 'Ana', idade: 20},
    {nome: 'Bia', idade: 25},
    {nome: 'Carlos', idade: 30}
]

const saveTo = path.resolve(__dirname, "aquivo-javascript.json")
fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => res.json())
    .then((json)=>{
        fs.writeFileSync(saveTo, JSON.stringify(json, null, 2));
    });