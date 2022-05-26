import {sort} from "/static/js/main/sorting.js";

export {mainTable};

class mainTable {
    constructor(shows) {
        this.shows = shows;
        this.currentPage = 1;
        this.numberPerPage = 15;
        this.currentShows = this.loadActualShows();
    }

    initTable() {
        this.createTableHeader();
        this.createTableBody();
        this.addEventOnColumn();
    }

    loadActualShows() {
        let begin = ((this.currentPage - 1) * this.numberPerPage);
        let end = begin + this.numberPerPage;
        return this.shows.slice(begin, end);
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
            tableRow.innerHTML =
                `<td><a href="${'/show/' + (show["id"])}">${show.title}</a></td>
                <td>${show.year}</td>
                <td>${show.runtime}</td>
                <td>${show.rating}</td>
                <td>${show.genres}</td>
                ${(show.trailer == null) ? 
                    `<td>No URL</td>` : 
                    `<td><a target="_blank" rel="noopener noreferrer" href="${show.trailer}">${show.trailer}</a></td>`}
                ${(show.homepage != null) ? `
                <td><a target="_blank" rel="noopener noreferrer" href="${show.homepage}">${show.homepage}</a></td>` : `
                <td>No URL</td>`}`;
            tableBody.appendChild(tableRow);
        }
    }

    sortHeader(arr, event) {
        const column = event.currentTarget;
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
            this.currentShows = this.sortHeader(this.currentShows, event);
            const tableBodyChildren = document.querySelectorAll('tbody tr');
            this.removeTableBodyChildren(tableBodyChildren);
            this.createTableBody();
        }));
    }

    removeTableBodyChildren(parent) {
        parent.forEach(children => children.remove());
    }
}
