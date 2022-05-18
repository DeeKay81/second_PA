import {mainTable} from "/static/js/main/main.js";
import {dataHandler} from "/static/js/data/dataHandler.js";

export {initStart};


async function initStart() {
    const shows = await loadShows();
    const table = new mainTable(shows);
    table.initTable();
}

async function loadShows() {
    return await dataHandler.getMostRatedShows();
}

await initStart();