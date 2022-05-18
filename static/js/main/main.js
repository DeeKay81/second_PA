import {dataHandler} from "../data/dataHandler.js";
import {sort} from "./sorting.js"

export {Pagination};

class Pagination {
    constructor(shows) {
        this.previousPage = this.previousPage.bind(this);
        this.shows = shows;
        this.currentPage = 1;
        this.numberPerPage = 15;
        this.numberOfPages = this.getNumberOfPages();
        this.currentShows = this.loadActualShows();
    }

    initPagination() {
        this.createTableHeader();
        this.createTableBody();
        this.addEventOnButtons();
        this.addEventOnColumn();
    }

    loadActualShows() {
        let begin = ((this.currentPage - 1) * this.numberPerPage);
        let end = begin + this.numberPerPage;
        return this.shows.slice(begin, end);
    }

    async getNumberOfPages() {
        const showsData = await dataHandler.getMostRatedShows();
        return Math.ceil(showsData.length / this.numberPerPage);
    }

    createTableHeader() {
        const headers = ["Title", "Year", "Runtime", "Rating", "Genres", "Trailer", "Homepage"];
        const sortableColumns = ["Title", "Year", "Runtime", "Rating"];
        const tableHead = document.querySelector("table.details thead");
        const tableRow = document.createElement('tr');
        for (let header of headers) {
            const headerCell = document.createElement('th');
            if (sortableColumns.includes(header)) {
                headerCell.classList.add('sortable');
                headerCell.innerHTML = header;
                tableRow.appendChild(headerCell);
            } else {
                headerCell.innerHTML = header;
                tableRow.appendChild(headerCell);
            }
        }
        tableHead.appendChild(tableRow);
    }

    createTableBody() {
        const tableBody = document.querySelector('tbody');
        for (let show of this.currentShows) {
            const tableRow = document.createElement('tr');
            tableRow.innerHTML = `<td><a href="${'/show/' + (show["id"])}">${show.title}</a></td>
                    <td>${show.year}</td>
                    <td>${show.runtime}</td>
                    <td>${show.rating}</td>
                    <td>${show.genres}</td>
                    ${(show.trailer == null) ? `<td>No URL</td>` : `<td><a target="_blank" rel="noopener noreferrer" href="${show.trailer}">${show.trailer}</a>
                       </td>`}
                    ${(show.homepage != null) ? `
                    <td><a target="_blank" rel="noopener noreferrer" href="${show.homepage}">${show.homepage}</a></td>` : `
                    <td>No URL</td>`}`;
            tableBody.appendChild(tableRow);
        }
        this.check();
    }

    bblSort(arr, event) {
        const column = event.currentTarget;
        /*Mit queryselctor all abfragen welche class auf sortable desc or asc gesetzt ist und remove*/
        const columnName = column.innerText.toLowerCase();
        if (column.classList.contains('desc')) {
            sort(arr, columnName, 'asc');
            column.classList.remove('desc');
            column.classList.add('asc');
            return arr;
        } else {
            sort(arr, columnName, 'desc');
            column.classList.remove('asc');
            column.classList.add('desc');
            return arr;
        }
    }

    addEventOnColumn() {
        const columns = document.querySelectorAll('.sortable');
        columns.forEach(column => column.addEventListener('click', (event) => {
            this.currentShows = this.bblSort(this.currentShows, event);
            const tableBodyChildren = document.querySelectorAll('tbody tr');
            this.removeTableBodyChildren(tableBodyChildren);
            this.createTableBody();
        }));
    }

    check() {
        document.querySelector(".next").disabled = this.currentPage === this.numberOfPages;
        document.querySelector(".previous").disabled = this.currentPage === 1;
    }

    nextPage = () => {
        this.currentPage += 1;
        const tableBodyChildren = document.querySelectorAll('tbody tr');
        this.removeTableBodyChildren(tableBodyChildren);
        this.currentShows = this.loadActualShows();
        this.createTableBody();
    };

    previousPage() {
        this.currentPage -= 1;
        const tableBodyChildren = document.querySelectorAll('tbody tr');
        this.removeTableBodyChildren(tableBodyChildren);
        this.currentShows = this.loadActualShows();
        this.createTableBody();
    }

    addEventOnButtons() {
        document.querySelector(".next").addEventListener('click', this.nextPage);
        document.querySelector(".previous").addEventListener('click', this.previousPage);
    }

    removeTableBodyChildren(parent) {
        parent.forEach(children => children.remove());
    }
}
