import {dataHandler} from "/static/js/main/dataHandler.js";

async function showOverview(){
    const btn = document.querySelector('.overview');
    let show_id = btn.getAttribute('id');
    const data = await dataHandler.getOverview(show_id);
    btn.addEventListener('click', event =>{
        const card = document.querySelector('.card_overview')
        card.classList.toggle('hidden');
        card.innerHTML = `<li src="${ data.overview }}"></li>`;
    });
}

await showOverview();
