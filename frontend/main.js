window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const apiGateway = 'https://crc-functionapp.azurewebsites.net/api/HttpTrigger1?code=VJu7cxKVJWsXIbqy-PTy4UEEzL8onzXvK2IOyMpX_s33AzFuxFpHGA==';

const getVisitCount = () => {
    let count = 0;
    fetch(apiGateway, {
        mode: 'cors',
    })
    .then(response => {
        return response.json()
    })
    .then(res => {
        const count = res.Attributes.visitcount;
        document.getElementById("counter").innerText = count;
        document.getElementById("visitorElem").style.display = 'block';
    })    
    return count;
}