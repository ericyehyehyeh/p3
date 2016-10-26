
$(document).ready(function() {
    $("#logoutForm").submit(function(event) {
    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/logout";
    $.ajax({
        type: "POST", 
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify(),
        url: url,
        success : function(data) {
            window.location.replace("http://localhost:3000/gu4wdnfe/p3/api/v1/")
            },
        error : function(response, status, error) {
        }
        });
        event.preventDefault();
    });    
});
