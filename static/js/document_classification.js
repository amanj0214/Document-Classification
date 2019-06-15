// Created by Amandeep at 6/15/2019
// "We are drowning in information, while starving for wisdom - E. O. Wilson"

var rootURL = 'http://127.0.0.1:4444/'

function predict_category() {
    content = $('#text').val()
    if(content != ""){
    fetch_details_url = rootURL + "predict"
      data = {
        method : 'POST',
        body : content
       }
      fetch(fetch_details_url, data).then(response => {
          return response.json();
        }).then(data => {
          alert(data)
        }).catch(err => {
        });
    }
    else{
        alert("Content is empty!")
    }
}