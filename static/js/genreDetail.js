import {dataHandler} from "/static/js/data/dataHandler.js";

export async function createTable(genre_id) {
     const allData = await getData(genre_id);
     createTableHeader();
     await createTableBody(allData);
}

function createTableHeader() {
        const headers = ["Title", "Rating", "Year", "Genres", "Actor Count"];
        const tableHead = document.querySelector("table.details thead");
        const tableRow = document.createElement('tr');
        for (let header of headers) {
            const headerCell = document.createElement('th');
                headerCell.innerHTML = header;
                tableRow.appendChild(headerCell);
        }
        tableHead.appendChild(tableRow);
    }

async function createTableBody(allData) {
        const tableBody = document.querySelector('tbody');
        for (let data of allData) {
            const tableRow = document.createElement('tr');
            tableRow.innerHTML =   `<td>${data.title}</td>
                                    <td>${data.rating}</td>
                                    <td>${data.year}</td>
                                    <td>${data.genre}</td>
                                    <td>${data.actor_count}</td>`;
            tableBody.appendChild(tableRow);
        }
}

async function getData(genre_id){
    // console.log(allData)
    return await dataHandler.getGenresDetail(genre_id)
}
