export {sort};

function sort(arr, columnName, order) {
    for (let index = 0; index < arr.length; index++) {
        for (let nextIndex = 0; nextIndex < (arr.length - index - 1); nextIndex++) {
            const ordering = order === 'asc' ? arr[nextIndex][columnName] >
                arr[nextIndex + 1][columnName] :
                arr[nextIndex][columnName] <
                arr[nextIndex + 1][columnName];
            if (ordering) {
                let temp = arr[nextIndex];
                arr[nextIndex] = arr[nextIndex + 1];
                arr[nextIndex + 1] = temp;
            }
        }
    }
}