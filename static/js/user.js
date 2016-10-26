$(document).ready(function() {


    //EDIT ROUTE
    $("#edit_submit").submit(function(event) {
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user/edit";

        $.ajax({
            type: "GET",
            contentType: "application/json; charset=UTF-8",
            data: JSON.stringify(),
            url: url,

            success : function(data) {
                console.log("it worked! get");
                console.log(data);
                username = data['username'];

                $.ajax({
                    type: "PUT", 
                    contentType: "application/json; charset=UTF-8",
                    data: JSON.stringify({
                        "username" : document.getElementById("new_username_input"),
                        "firstname" : document.getElementById("new_firstname_input"),
                        "lastname" :  document.getElementById("new_lastname_input"),
                        "email" : document.getElementById("new_email_input"),
                        "password1" : document.getElementById("new_password1_input"),
                        "password2" : document.getElementById("new_password2_input")
                    }), 
                    url: url,

                    success : function(data) {
                        console.log("it worked! put");
                        console.log(data);
                        console.log("Successfully updated user information!")
                    },

                    error: function(error){
                    //*******ERRORS********//
                    }
                });

                    //var page_title = document.createElement("h3");
                    //var album_title = document.createTextNode(title);
                    //page_title.appendChild(album_title);
                    //var element = document.getElementById("content");
                    //element.appendChild(page_title);
                },
            error : function(error) {
            //*******ERRORS********//
                }
            });
      }); 



    //NEW USER ROUTE
    $("#new_submit").submit(function(event) {
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";

        $.ajax({
            type: "POST", 
            contentType: "application/json; charset=UTF-8",
            data: JSON.stringify({
                "username" : document.getElementById("new_username_input"),
                "firstname" : document.getElementById("new_firstname_input"),
                "lastname" :  document.getElementById("new_lastname_input"),
                "email" : document.getElementById("new_email_input"),
                "password1" : document.getElementById("new_password1_input"),
                "password2" : document.getElementById("new_password2_input")
            }), 
            url : url,

            success : function(data) {
                console.log("it worked! post");
                console.log(data);
                window.location.replace("http://localhost:3000/gu4wdnfe/p3/api/v1")
                },
            error : function(response, status, error) {
               //*******ERRORS********//
                }
            });
         });
    event.preventDefault();
});