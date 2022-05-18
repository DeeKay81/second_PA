import {dataHandler} from "static/js/data/dataHandler.js";
import {createTable} from "static/js/genreDetail.js";

const allData = await dataHandler.getGenres();

async function getAllData() {
    const card = document.querySelector('ul');
    for (let genre of allData) {
        const li = document.createElement('li')
        li.innerHTML = `${genre["genre"]}`;
        li.addEventListener("click", ev => {
            createTable(genre.id)
        })
        card.appendChild(li);
    }

}

await getAllData();
