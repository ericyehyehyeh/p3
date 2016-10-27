$(document).ready(function() {

    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";

    $.ajax({
        type: "GET",
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify(), 
        url: url,
        success: function(data) {
            var username = data['username'];
            var firstname = data['firstname'];
            var lastname = data['lastname'];
            var email = data['email'];
            // Assign these values to the fields

            var page = document.getElementById('edit_submit_input');

            var el_1 = document.createElement("input");
            el_1.setAttribute("id", "update_firstname_input");
            el_1.setAttribute("type", "text");
            el_1.setAttribute("placeholder", "Firstname");
            el_1.setAttribute("name", "firstname");
            el_1.setAttribute("value", "");
            var submit_1 = document.createElement("input");
            submit_1.setAttribute("type", "submit");
            submit_1.setAttribute("id", "update_firstname_submit");
            submit_1.setAttribute("value", "Submit");

            var el_2 = document.createElement("input");
            el_2.setAttribute("id", "update_lastname_input");
            el_2.setAttribute("type", "text");
            el_2.setAttribute("placeholder", "Last Name");
            el_2.setAttribute("name", "lastname");
            el_2.setAttribute("value", "");
            var submit_2 = document.createElement("input");
            submit_2.setAttribute("type", "submit");
            submit_2.setAttribute("id", "update_lastname_submit");
            submit_2.setAttribute("value", "Submit");

            var el_3 = document.createElement("input");
            el_3.setAttribute("id", "update_email_input");
            el_3.setAttribute("type", "text");
            el_3.setAttribute("placeholder", "Email");
            el_3.setAttribute("name", "email");
            el_3.setAttribute("value", "");
            var submit_3 = document.createElement("input");
            submit_3.setAttribute("type", "submit");
            submit_3.setAttribute("id", "update_email_submit");
            submit_3.setAttribute("value", "Submit");

            var el_4 = document.createElement("input");
            el_4.setAttribute("id", "update_password1_input");
            el_4.setAttribute("type", "text");
            el_4.setAttribute("placeholder", "First Password");
            el_4.setAttribute("name", "password1");
            el_4.setAttribute("value", "");
            var el_5 = document.createElement("input");
            el_5.setAttribute("id", "update_password2_input");
            el_5.setAttribute("type", "text");
            el_5.setAttribute("placeholder", "Re-Enter Password");
            el_5.setAttribute("name", "password2");
            var submit_4 = document.createElement("input");
            submit_4.setAttribute("type", "submit");
            submit_4.setAttribute("id", "update_password_submit");
            submit_4.setAttribute("value", "Submit");

            page.appendChild(el_1);
            page.appendChild(submit_1);
            page.appendChild(el_2);
            page.appendChild(submit_2);
            page.appendChild(el_3);
            page.appendChild(submit_3);
            page.appendChild(el_4);
            page.appendChild(el_5);
            page.appendChild(submit_4);


            document.getElementById('Georges').value = "George Swirski";
        },
        error: function(response) {

            var page = document.getElementById('new_user_input');

            var el_0 = document.createElement("input");
            el_0.setAttribute("id", "new_username_input");
            el_0.setAttribute("type", "text");
            el_0.setAttribute("placeholder", "Username");
            el_0.setAttribute("name", "username");
            el_0.setAttribute("value", "");
            
            

            var el_1 = document.createElement("input");
            el_1.setAttribute("id", "new_firstname_input");
            el_1.setAttribute("type", "text");
            el_1.setAttribute("placeholder", "Firstname");
            el_1.setAttribute("name", "firstname");
            el_1.setAttribute("value", "");
            

            var el_2 = document.createElement("input");
            el_2.setAttribute("id", "new_lastname_input");
            el_2.setAttribute("type", "text");
            el_2.setAttribute("placeholder", "Last Name");
            el_2.setAttribute("name", "lastname");
            el_2.setAttribute("value", "");

            var el_4 = document.createElement("input");
            el_4.setAttribute("id", "new_password1_input");
            el_4.setAttribute("type", "text");
            el_4.setAttribute("placeholder", "First Password");
            el_4.setAttribute("name", "password1");
            el_4.setAttribute("value", "");
            var el_5 = document.createElement("input");
            el_5.setAttribute("id", "new_password2_input");
            el_5.setAttribute("type", "text");
            el_5.setAttribute("placeholder", "Re-Enter Password");
            el_5.setAttribute("name", "password2");


            var el_3 = document.createElement("input");
            el_3.setAttribute("id", "new_email_input");
            el_3.setAttribute("type", "text");
            el_3.setAttribute("placeholder", "Email");
            el_3.setAttribute("name", "email");
            el_3.setAttribute("value", "");

            var submit = document.createElement("input");
            submit.setAttribute("type", "submit");
            submit.setAttribute("value", "Submit");


            
            
            page.appendChild(el_0);
            page.appendChild(el_1);
            page.appendChild(el_2);
            page.appendChild(el_4);
            page.appendChild(el_5);
            page.appendChild(el_3);
            page.appendChild(submit);

        }
    });


    //EDIT ROUTE
    $("#edit_submit").submit(function(event) {
        event.preventDefault();
        var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/user";

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
                if (!re_letternum.test(password1)){
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
                if (!re_email.test(email)){
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
                        "username" : document.getElementById("update_username_input").value,
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
                    },

                    error : function(response) {
                        var response = JSON.parse('response');
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
                var response = JSON.parse('response');
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

        var username = document.getElementById("new_username_input").value;
        var firstname = document.getElementById("new_firstname_input").value;
        var lastname = document.getElementById("new_lastname_input").value;
        var email = document.getElementById("new_email_input").value;
        var password1 = document.getElementById("new_password1_input").value;
        var password2 = document.getElementById("new_password2_input").value;


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
        if (!re_letternum.test(password1)){
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
        if (!re_email.test(email)){
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
                "username" : document.getElementById("new_username_input").value,
                "firstname" : document.getElementById("new_firstname_input").value,
                "lastname" :  document.getElementById("new_lastname_input").value,
                "email" : document.getElementById("new_email_input").value,
                "password1" : document.getElementById("new_password1_input").value,
                "password2" : document.getElementById("new_password2_input").value
            }), 
            response: "application/json",
            url : url,

            success : function(data) {
                console.log("it worked! post");
                console.log(data);
                window.location.replace("http://localhost:3000/gu4wdnfe/p3/api/v1")
                },
            error : function(response) {
                console.log(response)
                var my_errors = []
                my_errors = response.responseText['errors'];
                console.log(my_errors);
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
});