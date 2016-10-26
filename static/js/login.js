
$(document).ready(function() {
    $("#loginForm").submit(function(event) {
    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/login";
    $.ajax({
        type: "POST", 
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify({
            "username": document.getElementById("login_username_input"),
            "password": document.getElementById("login_password_input")
        }), 
        url: url,
        success : function(data) {
            //***If there is a url query parameter (for example: /login?url=/the/prev/url) then redirect to the URL.
            window.location.replace("http://localhost:3000/gu4wdnfe/p3/api/v1/")
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
