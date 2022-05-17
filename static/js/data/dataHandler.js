export let dataHandler={
    getMostRatedShows: async function(){
        return await apiGet("/api/get-most-rated-shows")
    },

    getShowsByTitle: async function(name) {
        return await apiGet(`/api/get-shows-by-title/${name}`);
    }
};

async function apiGet(url){
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.status === 200){
        return response.json()
    }
}