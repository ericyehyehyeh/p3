$(document).ready(function() {


    //EDIT ROUTE
    $("#edit_submit").submit(function(event) {
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";

        $.ajax({
            type: "GET",
            contentType: "application/json; charset=UTF-8",
            data: JSON.stringify(),
            url: url,

            success : function(data) {
                var firstname = document.getElementById("update_firstname_input");
                var lastname = document.getElementById("update_lastname_input");
                var email = document.getElementById("update_email_input");
                var password1 = document.getElementById("update_password1_input");
                var password2 = document.getElementById("update_password2_input");


                var page = document.getElementById("content");
                var error_para = document.createElement("p");
                error_para.setAttribute("class", "error");
                var error = "";


                var re_underscore = /^[a-zA-Z0-9_]+$/;
                if (password1.length < 8){
                    error = document.createTextNode("Passwords must be at least 8 characters long");
                    error_para.appendChild(error);
                }
                var re_letternum = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/;
                if (!re_letternum.text(password1)){
                    error = document.createTextNode("Passwords must contain at least one letter and one number");
                    error_para.appendChild(error);
                }
                if (!re_underscore.test(password1)){
                    error = document.createTextNode("Passwords may only contain letters, digits, and underscores");
                    error_para.appendChild(error);
                }
                if (password1 != password2){
                    error = document.createTextNode("Passwords do not match");
                    error_para.appendChild(error);
                }
                var re_email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                if (!re_email.text(email)){
                    error = document.createTextNode("Email address must be valid");
                    error_para.appendChild(error);
                }
                if (firstname.length > 20){
                    error = document.createTextNode("Firstname must be no longer than 20 characters");
                    error_para.appendChild(error);
                }
                if (lastname.length > 20){
                    error = document.createTextNode("Lastname must be no longer than 20 characters");
                    error_para.appendChild(error);
                }
                if (email.length > 40){
                    error = document.createTextNode("Email must be no longer than 40 characters");
                    error_para.appendChild(error);
                }


                page.appendChild(error_para);

                $.ajax({
                    type: "PUT", 
                    contentType: "application/json; charset=UTF-8",
                    data: JSON.stringify({
                        "username" : document.getElementById("update_username_input"),
                        "firstname" : document.getElementById("update_firstname_input"),
                        "lastname" :  document.getElementById("update_lastname_input"),
                        "email" : document.getElementById("update_email_input"),
                        "password1" : document.getElementById("update_password1_input"),
                        "password2" : document.getElementById("update_password2_input")
                    }), 
                    url: url,

                    success : function(data) {
                        console.log("it worked! put");
                        console.log(data);
                        console.log("Successfully updated user information!")
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
    }); 



    //NEW USER ROUTE
    $("#new_submit").submit(function(event) {
        event.preventDefault();
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";

        var username = document.getElementById("new_username_input");
        var firstname = document.getElementById("new_firstname_input");
        var lastname = document.getElementById("new_lastname_input");
        var email = document.getElementById("new_email_input");
        var password1 = document.getElementById("new_password1_input");
        var password2 = document.getElementById("new_password2_input");


        var page = document.getElementById("content");
        var error_para = document.createElement("p");
        error_para.setAttribute("class", "error");
        var error = "";


        if (username.length < 3) {
            error = document.createTextNode("Usernames must be at least 3 characters long");
            error_para.appendChild(error);
        }
        var re_underscore = /^[a-zA-Z0-9_]+$/;
        if (!re_underscore.test(username)){
            error = document.createTextNode("Usernames may only contain letters, digits, and underscores");
            error_para.appendChild(error);
        }
        if (password1.length < 8){
            error = document.createTextNode("Passwords must be at least 8 characters long");
            error_para.appendChild(error);
        }
        var re_letternum = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/;
        if (!re_letternum.text(password1)){
            error = document.createTextNode("Passwords must contain at least one letter and one number");
            error_para.appendChild(error);
        }
        if (!re_underscore.test(password1)){
            error = document.createTextNode("Passwords may only contain letters, digits, and underscores");
            error_para.appendChild(error);
        }
        if (password1 != password2){
            error = document.createTextNode("Passwords do not match");
            error_para.appendChild(error);
        }
        var re_email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!re_email.text(email)){
            error = document.createTextNode("Email address must be valid");
            error_para.appendChild(error);
        }
        if (username.length > 20){
            error = document.createTextNode("Username must be no longer than 20 characters");
            error_para.appendChild(error);
        }
        if (firstname.length > 20){
            error = document.createTextNode("Firstname must be no longer than 20 characters");
            error_para.appendChild(error);
        }
        if (lastname.length > 20){
            error = document.createTextNode("Lastname must be no longer than 20 characters");
            error_para.appendChild(error);
        }
        if (email.length > 40){
            error = document.createTextNode("Email must be no longer than 40 characters");
            error_para.appendChild(error);
        }
        

        page.appendChild(error_para);


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
         });
    event.preventDefault();
});