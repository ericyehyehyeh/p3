$(document).ready(function() {
    //window.alert("function worked");
    $("#loginForm").submit(function(event) {
    //window.alert("2");
    var formData = $("#loginForm").serialize();
    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/login";
    $.ajax({
        data : formData,
        type : "POST",
        url : url,
        success : function(data) {
            var obj = JSON.parse(data);
            var username = obj.username;
            console.log("username " + username + " has been logged in");
                if (username) {
                    location.assign("http://localhost:3000/gu4wdnfe/p3/");
                }


        },
            error : function() {
                window.alert("error with login");
            }
        });

        event.preventDefault();
    });    
});