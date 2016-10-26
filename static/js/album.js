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
        error : function(response, status, error) {
            //SOME WORK TO DO WITH ERROR CHECKING
            //ALSO HAVE TO WORK ON REPRESENTING ERROR IN LOGIN.HTML, SHOULD ONLY HAVE TO DO AN APPEND FUNCTION TO A <P> TAG

            /*var responseArray = JSON.parse(response.responseText);
            var firstMessageJSON = reponseArray[0];
            alert(firstMessageJSON);
            var responseMessage = JSON.parse(reponseArray.errors[0]);
            //var obj = responseMessage.message;
            //alert(reponse);
            //alert(response);
            alert(response.responseText);*/
        }
        });

        event.preventDefault();
    });    
});