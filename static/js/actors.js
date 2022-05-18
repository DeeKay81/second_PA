import {dataHandler} from "/static/js/data/dataHandler.js";
import {initPopup} from "/static/js/actorPopup.js";

const allData = await dataHandler.getActors();
const data = await dataHandler.getShowsByTitle();

export async function getAllData() {
    const card = document.querySelector('ul');
    for (let actor of allData) {
        const li = document.createElement('li')
        li.setAttribute('class', 'firstname')
        li.innerHTML=`<a href="${'/actors/' + (actor["firstname"])}"  onclick="initPopup()">${actor["firstname"]}</a>`;
        card.appendChild(li);
    }
    document.querySelectorAll('.firstname').forEach( item => {
        listShowsBy(item);
          item.addEventListener('click', event => {
              let allItems = document.querySelectorAll(".firstname")
              allItems.forEach(show => {
                  show.firstElementChild.classList.add("hidden");
              })
              let childElement = item.firstElementChild;
              childElement.classList.toggle("hidden");
          });
    });
}

async function getDetails(){
    const firstname = document.querySelectorAll('.firstname')

}

function listShowsBy(item) {
    let name = item.innerText;
    data.forEach(data => {
        let firstName = data.actors.substring(0, data.actors.indexOf(' '));
        if (firstName === name) {
            item.innerHTML += `
            <ul class="shows hidden">
            </ul>
            `
            data.shows.forEach(show => {
                let listItem = document.createElement('li');
                listItem.innerText = show;
                item.firstElementChild.appendChild(listItem);
            });
        }
    });
}

await getAllData();