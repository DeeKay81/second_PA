import {dataHandler} from "/static/js/main/dataHandler.js";
import {createTable} from "/static/js/genreDetail.js";

function getGenresData(){
    return dataHandler.getGenres();
}

let allData = await dataHandler.getGenres();

async function getAllData() {
    // console.log(allData)
    const card = document.querySelector('ul');
    for (let genre of allData) {
        const li = document.createElement('li');
        // console.log(genre)
        li.innerHTML=`${genre['genre']}`;
        li.addEventListener("click", eve => {
            createTable(genre.id);
        })
        card.appendChild(li);
    }

}

await getAllData();