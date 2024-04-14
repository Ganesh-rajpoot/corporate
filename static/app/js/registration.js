// script.js

$(document).ready(function() {
    $('#registrationForm').submit(function(event) {
        event.preventDefault();
        
        var formData = {
            'username': $('#username').val(),
            'email': $('#email').val(),
            'mobile': $('#mobile').val(),
            'password': $('#password').val(),
            'refrel_code': $('#refrel_code').val()
        };
        console.log("this is the user name",username);
        console.log("this is the user email",email);
        console.log("this is the user mobile",mobile);
        $.ajax({
            type: 'POST',
            url: '/registration/',  // URL to your backend view for handling registration
            data: formData,
            dataType: 'json',
            success: function(data) {
                console.log('Registration successful');
                // Handle success response
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
                // Handle error response
            }
        });
    });
});
