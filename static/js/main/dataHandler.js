export let dataHandler = {
    getOverview: async function(){
        return await apiGet(`/api/get-overview`)
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