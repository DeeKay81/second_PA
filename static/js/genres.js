import {dataHandler} from "/static/js/data/dataHandler.js";
import {createTable} from "/static/js/genreDetail.js";

const allData = await dataHandler.getGenres();

async function getAllData() {
    console.log(allData)
    const card = document.querySelector('ul');
    for (let genre of allData) {
        const li = document.createElement('li')
        console.log(genre)
        li.innerHTML=`<a href="${'/shows/genres/' + (genre["id"])}" onclick="createTable(${genre.id})">${genre["genre"]}</a>`;
        card.appendChild(li);
    }

}

getAllData();