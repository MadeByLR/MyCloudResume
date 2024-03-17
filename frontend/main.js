window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const functionApiUrl = 'https://lrgetresumecounter.azurewebsites.net/api/GetResumeCounter?code=jjAyp-wbTvXj0X9EMGSbpAD2ZClHg7Fv8Zln28zrYMHYAzFusDR6Qw==';
const localfunctionApi = 'http://localhost:7071/api/GetResumeCounter';

const getVisitCount = () => {
    let count = 0;
    fetch(functionApiUrl).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called fucntion API.");
        count = response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });  
    return count;
}