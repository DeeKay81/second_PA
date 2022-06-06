import {dataHandler} from '/static/js/main/dataHandler.js';

function getActorData(){
    return dataHandler.getActors();
}

let allData = await getActorData();

async function getAllData() {
    const card = document.querySelector('ol');
    let actor = '';
    allData.forEach(allData => {
        actor = allData.firstname;
        card.innerHTML += `<li class="firstname">${actor}</li>`;
    })
    document.querySelectorAll('.firstname').forEach( element => {
        listShows(element);
        element.addEventListener('click', event => {
            let allElements = document.querySelectorAll('.firstname');
            allElements.forEach(show => {
                show.firstElementChild.classList.add('hidden');
            })
            let childElement = element.firstElementChild;
            childElement.classList.toggle('hidden');
        });

    });
}

function listShows(element) {
    let name = element.innerText;
    allData.forEach(allData => {
        let firstName = allData.firstname;
        if (firstName === name) {
            element.innerHTML += `<ul class="shows hidden"></ul>`
            allData.shows.forEach(show =>{
                let listElement = document.createElement('li');
                listElement.innerText = show;
                element.firstElementChild.appendChild(listElement);
            });
        }
    });
}

await getAllData();