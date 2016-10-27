
$(document).ready(function() {
    $("#loginForm").submit(function(event) {
    event.preventDefault();
    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/login";
    $.ajax({
        type: "POST", 
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify({
            "username": document.getElementById("login_username_input").value,
            "password": document.getElementById("login_password_input").value
        }), 
        url: url,
        success : function(data) {
            
            var query = window.location.href.indexOf('url=');
            var link = "";
            if (query == -1){
                window.location.replace("http://localhost:3000/gu4wdnfe/p3")
            }
            else{
                link = window.location.href.split('url=')[1];
                window.location.replace(link);
            }

    
            
            },
        error : function(response) {
            var response2 = JSON.parse(response.responseText);
            alert(response2);
            var my_errors = response2['errors'];
            var error_message = "";
            var page = document.getElementById("content").value;

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
