export let dataHandler = {
    getTrailer: async function(show_id) {
        return await apiGet(`/api/get-trailer/${show_id}`);
    }
};

async function apiGet(url) {
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.status === 200) {
        return response.json()
    }
}