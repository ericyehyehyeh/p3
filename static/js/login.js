$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data: {
				username : $('#login_username_input').val(),
				password: $('#login_password_input').val()
			}
			type : 'POST',
			url : '/gu4wdnfe/p3/api/v1/login',
			success : function(data) {
				console.log("username " + username + " has been logged in");

			}
		});

		event.preventDefault();
	});
})