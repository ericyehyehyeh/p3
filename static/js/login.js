$(document).ready(function() {
    $("#loginForm").submit(function(event) {
    var formData = $("#loginForm").serialize();
    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/login";
    $.ajax({
        data : formData,
        type : "POST",
        url : url,
        success : function(data) {
            var obj = JSON.parse(data);
            var username = obj.username;
            var error = obj.error;
            console.log("username " + username + " has been logged in");
                if (username) {
                    location.assign("http://localhost:3000/gu4wdnfe/p3/");
                }
                else if (error) {
                    alert(error)
                }
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