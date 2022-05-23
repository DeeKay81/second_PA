import {dataHandler} from "./data/dataHandler.js";


async function showTrailer(){
    const btn = document.querySelector('.trailer');
    let show_id = btn.getAttribute('id');
    const data = await dataHandler.getTrailer(show_id);
    btn.addEventListener('click', event =>{
        const card = document.querySelector('.card_trailer')
        card.classList.toggle("hidden");
        card.innerHTML = `<iframe src="${ data.trailer.replace('watch', 'embed').replace('?v=', '/') + '?autoplay=1&mute=1' }}" allow="autoplay"></iframe>`;
    });
}

await showTrailer()



