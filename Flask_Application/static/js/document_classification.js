// Created by Amandeep at 6/15/2019
// "We are drowning in information, while starving for wisdom - E. O. Wilson"

function predict_category() {
    content = $('#text').val()
    if(content != ""){
      data = {
        method : 'POST',
        body : {'words':content}
       }
      fetch("/predict", data).then(response => {
          return response.json();
        }).then(data => {
            if('prediction' in data){
                $('#cat_type').html(data['prediction'] + ", Confidence : " + data['confidence']+"%")
            }
        }).catch(err => {
            $('#cat_type').html("--[ERROR] " + err)
        });
    }
    else{
        $('#cat_type').html("--[WARN] : Content cannot be empty--")
    }
}