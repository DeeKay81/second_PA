export let dataHandler = {
    get_: async function() {
        return await apiGet(`/api/get-.../`);
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