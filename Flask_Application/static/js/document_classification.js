// Created by Amandeep at 6/15/2019
// "We are drowning in information, while starving for wisdom - E. O. Wilson"

function predict_category() {
    content = $('#text').val()
    if(content != ""){
      data = {
        method : 'POST',
        body : content
       }
      fetch("/predict", data).then(response => {
          return response.json();
        }).then(data => {
            $('#cat_type').html(data['prediction'] + ", Confidence : " + data['confidence']+"%")
        }).catch(err => {
        });
    }
    else{
        $('#cat_type').html("--[WARN] : Content cannot be empty--")
    }
}