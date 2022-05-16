import {Pagination} from "/static/js/main.js";
import {dataHandler} from "/static/js/data/dataHandler.js";

export {initStart};


async function initStart() {
    const shows = await loadShows();
    const pagination = new Pagination(shows);
    pagination.initPagination();
}

async function loadShows(){
    return await dataHandler.getMostRatedShows();
}

initStart();