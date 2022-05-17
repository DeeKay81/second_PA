import {dataHandler} from "/static/js/data/dataHandler.js";

class popupWindow {
    constructor() {
        this.popupWindowUp = false;
    }

    init() {
        this.addEventOnAllFirstname();
    }

    addEventOnCloseBtn() {
        const popupDiv = document.querySelector('.popup');
        const closeButton = document.querySelector('.close-btn');
        const listItems = document.querySelectorAll('li');
        const cardDiv = document.querySelector('.card');
        closeButton.addEventListener('click', () => {
            listItems.forEach(listItem => listItem.remove());
            cardDiv.classList.remove('visibility');
            popupDiv.classList.add('hidden');
            this.popupWindowUp = false;
        });
    }

    addEventOnAllFirstname() {
        const popupDiv = document.querySelector('.popup');
        const firstnames = document.querySelectorAll('.firstname');
        const cardDiv = document.querySelector('.card');
        firstnames.forEach(firstname => firstname.addEventListener('click', async (event) => {
            const shows = await dataHandler.getShowsByTitle(event.currentTarget.innerText);
            if (this.popupWindowUp === false) {
                this.popupWindowUp = true;
                cardDiv.classList.add('visibility');
                popupDiv.classList.remove('hidden');
                this.createList(shows);
                this.addEventOnCloseBtn();
            } else if (this.popupWindowUp === true) {
                const listItems = document.querySelectorAll('li');
                listItems.forEach(listItem => listItem.remove());
                this.createList(shows);
                this.addEventOnCloseBtn();
            }
        }));
    }

    createList(shows) {
        const popupList = document.querySelector('.popup-list');
        for (let show of shows) {
            const listItem = document.createElement('li');
            listItem.innerText = show.title;
            popupList.appendChild(listItem);
        }
    }
}

function initPopup() {
    const popup = new popupWindow();
    popup.init();
}

initPopup();