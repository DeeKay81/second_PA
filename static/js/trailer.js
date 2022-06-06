import {dataHandler} from "/static/js/main/dataHandler.js";

async function showTrailer() {
    const clickMe = document.querySelector('.trailer');
    let show_id = clickMe.getAttribute('id');
    const data = await dataHandler.getTrailer(show_id);

    clickMe.addEventListener('click', event => {
        const cardTrailer = document.querySelector('.card_trailer');
        cardTrailer.classList.toggle('hidden');
        cardTrailer.innerHTML = `<iframe src="${ data.trailer.replace('watch', 'embed').replace('?v=', '/') + '?autoplay=1&mute=1' }}" allow="autoplay"></iframe>`;
    })
}

await showTrailer();
