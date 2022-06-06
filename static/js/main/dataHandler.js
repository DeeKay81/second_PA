export let dataHandler = {
    getOverview: async function(show_id){
        return await apiGet(`/api/get-overview/${show_id}`)
    }
};

async function apiGet(url) {
    let response = await fetch(url, {
        method: "GET",
    });
    // console.log(response.statusText);
    if (response.status === 200) {
        return response.json()
    }
}