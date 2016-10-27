$(document).ready(function() {

    $("#logoutForm").submit(function(event) {
    event.preventDefault();
    var url = "http://class3.eecs.umich.edu:4550/gu4wdnfe/p3/api/v1/logout";
    $.ajax({
        type: "POST", 
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify(),
        url: url,
        success : function(data) {
            window.location.replace("http://class3.eecs.umich.edu:4550/gu4wdnfe/p3");
            },
        error : function(response) {
            var response = JSON.parse(response);
            var my_errors = response['errors'];
            var error_message = "";
            var page = document.getElementById("content");

            for (i = 0; i < my_errors.length; i++){
                error_message = my_errors[i]['message'];

                var error_para = document.createElement("p");
                error_para.setAttribute("class", "error");
                var error = document.createTextNode(error_message);
                error_para.appendChild(error);
                page.appendChild(error_para);
            }         
        }
        });
        event.preventDefault();
    });    
});
