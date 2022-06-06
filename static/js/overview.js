import {dataHandler} from "/static/js/main/dataHandler.js";

// async function showOverview(){
//     const btn = document.querySelector('.overview');
//     let show_id = btn.getAttribute('id');
//     const data = await dataHandler.getOverview(show_id);
//     btn.addEventListener('click', event =>{
//         const card = document.querySelector('.card_overview')
//         card.classList.toggle('hidden');
//         card.innerHTML = `<li src="${ data.overview }}"></li>`;
//     });
// }
//
// await showOverview();

async function openOverview() {
    const data = await dataHandler.getOverview();
    let listItems = document.querySelectorAll('ol');
    for (const element of listItems) {
        element.addEventListener('click', function(){
            this.classList.remove('hidden');
        });
    }

    // let list = document.getElementById('overview')
    // const data = await dataHandler.getOverview();
    // list.addEventListener('click', event => {
    //     list.classList.toggle('hidden');
    // })
    // list.classList.remove('hidden');

    // if (list.style.display === 'none') {
    //     list.style.display = 'block';
    // }
    // else {
    //     list.style.display = 'none';
    // }
}

await openOverview();