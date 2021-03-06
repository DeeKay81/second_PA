import {dataHandler} from "./data/dataHandler.js";
import {createTable} from "./genreDetail.js";

const allData = await dataHandler.getGenres();

async function getAllData() {
    console.log(allData)
    const card = document.querySelector('ul');
    for (let genre of allData) {
        const li = document.createElement('li')
        console.log(genre)
        li.innerHTML=`${genre["genre"]}`;
        li.addEventListener("click", ev => {
            createTable(genre.id)
        })
        card.appendChild(li);
    }

}

getAllData()


