$(document).ready(function() {


    //EDIT ROUTE
    $("#update_user").submit(function(event) {
        event.preventDefault();
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";
        $( ".error" ).remove();


        $.ajax({

            type: "GET",
            contentType: "application/json; charset=UTF-8",
            data: JSON.stringify(),
            url: url,

            success : function(data) {
                var firstname = document.getElementById("update_firstname_input").value;
                var lastname = document.getElementById("update_lastname_input").value;
                var email = document.getElementById("update_email_input").value;
                var password1 = document.getElementById("update_password1_input").value;
                var password2 = document.getElementById("update_password2_input").value;
                document.getElementById("update_firstname_input").value = "";
                document.getElementById("update_lastname_input").value = "";
                document.getElementById("update_email_input").value = "";
                document.getElementById("update_password1_input").value = "";
                document.getElementById("update_password2_input").value = "";


                var page = document.getElementById("content");
                var error_para = document.createElement("p");
                error_para.setAttribute("class", "error");
                var error = "";

                var password_error = true;
                if ((password1.length == 0) && (password2.length == 0)){
                    password_error = false;
                }
                var errors = false;

                var re_underscore = /^[a-zA-Z0-9_]+$/;
                if (password_error == true){
                    if (password1.length < 8){
                        error = document.createTextNode("Passwords must be at least 8 characters long");
                        error_para.appendChild(error);
                        linebreak = document.createElement("br");
                        error_para.appendChild(linebreak);
                        errors = true;
                    }
                }
                var re_letternum = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/;
                if (password_error == true){
                    if (!re_letternum.test(password1)){
                        error = document.createTextNode("Passwords must contain at least one letter and one number");
                        error_para.appendChild(error);
                        linebreak = document.createElement("br");
                        error_para.appendChild(linebreak);
                        errors = true;
                    }
                    if (!re_underscore.test(password1)){
                        error = document.createTextNode("Passwords may only contain letters, digits, and underscores");
                        error_para.appendChild(error);
                        linebreak = document.createElement("br");
                        error_para.appendChild(linebreak);
                        errors = true;
                    }
                    if (password1 != password2){
                        error = document.createTextNode("Passwords do not match");
                        error_para.appendChild(error);
                        linebreak = document.createElement("br");
                        error_para.appendChild(linebreak);
                        errors = true;
                    }
                }
                var re_email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                if (!re_email.test(email)){
                    error = document.createTextNode("Email address must be valid");
                    error_para.appendChild(error);
                    linebreak = document.createElement("br");
                    error_para.appendChild(linebreak);
                    errors = true;
                }
                if (firstname.length > 20){
                    error = document.createTextNode("Firstname must be no longer than 20 characters");
                    error_para.appendChild(error);
                    linebreak = document.createElement("br");
                    error_para.appendChild(linebreak);
                    errors = true;
                }
                if (lastname.length > 20){
                    error = document.createTextNode("Lastname must be no longer than 20 characters");
                    error_para.appendChild(error);
                    linebreak = document.createElement("br");
                    error_para.appendChild(linebreak);
                    errors = true;
                }
                if (email.length > 40){
                    error = document.createTextNode("Email must be no longer than 40 characters");
                    error_para.appendChild(error);
                    linebreak = document.createElement("br");
                    error_para.appendChild(linebreak);
                    errors = true;
                }


                page.appendChild(error_para);

                if (errors == false){
                    console.log("no errors");
                    $.ajax({
                        type: "PUT", 
                        contentType: "application/json; charset=UTF-8",
                        data: JSON.stringify({
                            "firstname" : document.getElementById("update_firstname_input").value,
                            "lastname" :  document.getElementById("update_lastname_input").value,
                            "email" : document.getElementById("update_email_input").value,
                            "password1" : document.getElementById("update_password1_input").value,
                            "password2" : document.getElementById("update_password2_input").value
                        }), 
                        url: url,

                        success : function(data) {
                            console.log("it worked! put");
                            console.log(data);
                            console.log("Successfully updated user information!")
                            window.location.replace("http://localhost:3000/gu4wdnfe/p3/login");
                        },

                        error : function(response) {
                            console.log("errors in second ajax function");
                            var page = document.getElementById("error");


                            var response2 = JSON.parse(response.responseText);
                            var my_errors = response2['errors'];
                            var error_message = "";


                            for (i = 0; i < my_errors.length; i++){
                                console.log(i);
                                error_message = my_errors[i]['message'];

                                var error_para = document.createElement("p");
                                error_para.setAttribute("class", "error");
                                var error = document.createTextNode(error_message);
                                error_para.appendChild(error);
                                page.appendChild(error_para);

                                linebreak = document.createElement("br");
                                error_para.appendChild(linebreak);
                                }         
                            }
                    });
                }

                
                },
            error : function(response) {
                console.log("errors in first ajax function");
                var page = document.getElementById("error");

                var response2 = JSON.parse(response.responseText);
                var my_errors = response2['errors'];
                var error_message = "";

                //Put page up at top and every time you submit now it clears the content

                for (i = 0; i < my_errors.length; i++){
                    error_message = my_errors[i]['message'];
                    var error_para = document.createElement("p");
                    error_para.setAttribute("class", "error");
                    var error = document.createTextNode(error_message);
                    error_para.appendChild(error);
                    page.appendChild(error_para);

                    linebreak = document.createElement("br");
                    error_para.appendChild(linebreak);
                }         
            }
        });
    }); 



    //NEW USER ROUTE
    $("#new_user").submit(function(event) {

        event.preventDefault();
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";
        $( ".error" ).remove();

        var username = document.getElementById("new_username_input").value;
        var firstname = document.getElementById("new_firstname_input").value;
        var lastname = document.getElementById("new_lastname_input").value;
        var email = document.getElementById("new_email_input").value;
        var password1 = document.getElementById("new_password1_input").value;
        var password2 = document.getElementById("new_password2_input").value;

        document.getElementById("new_username_input").value ="";
        document.getElementById("new_firstname_input").value = "";
        document.getElementById("new_lastname_input").value = "";
        document.getElementById("new_email_input").value = "";
        document.getElementById("new_password1_input").value = "";
        document.getElementById("new_password2_input").value = "";


        var page = document.getElementById("content");
        var error_para = document.createElement("p");
        error_para.setAttribute("class", "error");
        var error = "";

        var errors = false;

        if (username.length < 3) {
            error = document.createTextNode("Usernames must be at least 3 characters long");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        var re_underscore = /^[a-zA-Z0-9_]+$/;
        if (!re_underscore.test(username)){
            error = document.createTextNode("Usernames may only contain letters, digits, and underscores");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (password1.length < 8){
            error = document.createTextNode("Passwords must be at least 8 characters long");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        var re_letternum = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/;
        if (!re_letternum.test(password1)){
            error = document.createTextNode("Passwords must contain at least one letter and one number");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (!re_underscore.test(password1)){
            error = document.createTextNode("Passwords may only contain letters, digits, and underscores");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (password1 != password2){
            error = document.createTextNode("Passwords do not match");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        var re_email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!re_email.test(email)){
            error = document.createTextNode("Email address must be valid");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (username.length > 20){
            error = document.createTextNode("Username must be no longer than 20 characters");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (firstname.length > 20){
            error = document.createTextNode("Firstname must be no longer than 20 characters");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (lastname.length > 20){
            error = document.createTextNode("Lastname must be no longer than 20 characters");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        if (email.length > 40){
            error = document.createTextNode("Email must be no longer than 40 characters");
            error_para.appendChild(error);
            linebreak = document.createElement("br");
            error_para.appendChild(linebreak);
            errors = true;
        }
        

        page.appendChild(error_para);

        if (errors == false){
            $.ajax({
                type: "POST", 
                contentType: "application/json; charset=UTF-8",
                data: JSON.stringify({
                    "username" : document.getElementById("new_username_input").value,
                    "firstname" : document.getElementById("new_firstname_input").value,
                    "lastname" :  document.getElementById("new_lastname_input").value,
                    "email" : document.getElementById("new_email_input").value,
                    "password1" : document.getElementById("new_password1_input").value,
                    "password2" : document.getElementById("new_password2_input").value,
                }), 
                response: "application/json; charset=UTF-8",
                url : url,

                success : function(data) {
                    console.log("it worked! post");
                    console.log(data);
                    window.location.replace("http://localhost:3000/gu4wdnfe/p3/api/v1")
                    },
                error : function(response) {
                    var response2 = JSON.parse(response.responseText);
                    var my_errors = response2['errors'];
                    var error_message = "";

                    //Put page up at top and every time you submit now it clears the content
                    var page = document.getElementById("error");

                    for (i = 0; i < my_errors.length; i++){
                        error_message = my_errors[i]['message'];

                        var error_para = document.createElement("p");
                        error_para.setAttribute("class", "error");
                        var error = document.createTextNode(error_message);
                        error_para.appendChild(error);

                        linebreak = document.createElement("br");
                        error_para.appendChild(linebreak);
                    }         
                }
                });
            }
         });
});