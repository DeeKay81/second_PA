import {dataHandler} from "/static/js/data/dataHandler.js";

let allData = await getData();

function getData(){
    const allData = dataHandler.getActorsNshows();
    console.log(allData)
    return allData

}


async function getAllData() {
    const card = document.querySelector('ul');
    let actor = "";
    allData.forEach(allData => {
        actor = allData.firstname;
        console.log(actor);
        card.innerHTML += `<li class="firstname">${actor}</li>`;
    })
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



function listShowsBy(item) {
    let name = item.innerText;

    allData.forEach(allData => {
        let firstName = allData.firstname;
        console.log(firstName)
        if (firstName === name) {
            item.innerHTML += `
            <ul class="shows hidden">
            </ul>
            `
            allData.shows.forEach(show =>{
                let listItem = document.createElement('li');
                listItem.innerText = show;
                item.firstElementChild.appendChild(listItem);
            });
        }
    });
}

await getAllData();