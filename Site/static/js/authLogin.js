$('#register-form').submit(function (event) {
    $.ajax({
        type: 'POST',
        url: '/account/register/',
        data: {
            username: $('#id_username_reg').val(),
            email: $('#id_email_reg').val(),
            firstname: $('#id_firstname').val(),
            lastname: $('#id_lastname').val(),
            password1: $('#id_password1').val(),
            password2: $('#id_password2').val(),
            csrfmiddlewaretoken: $.cookie('csrftoken')
        },
        success: function (data) {
            var username_error_reg = $('#username-error-reg').empty().hide();
            var email_error_reg = $('#email-error-reg').empty().hide();
            var firstname_error_reg = $('#firstname-error-reg').empty().hide();
            var surname_error_reg = $('#surname-error-reg').empty().hide();
            var password1_error_reg = $('#password1-error-reg').empty().hide();
            var password2_error_reg = $('#password2-error-reg').empty().hide();
            var other_errors_reg = $('#other-errors-reg').empty().hide();
            if (data['username']) {
                data['username'].forEach(function (item) {
                    username_error_reg.append(item);
                    username_error_reg.show();
                });
            }
            if (data['email']) {
                data['email'].forEach(function (item) {
                    email_error_reg.append(item);
                    email_error_reg.show();
                });
            }
            if (data['firstname']) {
                data['firstname'].forEach(function (item) {
                    firstname_error_reg.append(item);
                    firstname_error_reg.show();
                });
            }
            if (data['lastname']) {
                data['lastname'].forEach(function (item) {
                    surname_error_reg.append(item);
                    surname_error_reg.show();
                });
            }
            if (data['password1']) {
                data['password1'].forEach(function (item) {
                    password1_error_reg.append(item);
                    password1_error_reg.show();
                });
            }
            if (data['password2']) {
                data['password2'].forEach(function (item) {
                    password2_error_reg.append(item);
                    password2_error_reg.show();
                });
            }
            if (data['__all__']) {
                other_errors_reg.append(data['__all__']);
                other_errors_reg.show();
            }
            if (typeof data === 'string') {
                window.location.href = data;
            }
        },
        error: function (data) {
            console.log(data);
            alert('Stop hacking my site !');
        }
    });
    return false;
});

$('#login-form').submit(function(event){
    $.ajax({
         type:'POST',
         url:'/account/login/',
         data: {
             username: $('#id_username_log').val(),
             password: $('#id_password').val(),
             csrfmiddlewaretoken: $.cookie('csrftoken')
         },
         success: function(data) {
             var username_error_log = $('#username-error-log').empty().hide();
             var password_error_log = $('#password-error-log').empty().hide();
             var other_errors_log = $('#other-errors-log').empty().hide();
             if (data['username']) {
                 data['username'].forEach(function(item) {
                     email_error_log.append(item);
                     email_error_log.show();
                 });
             }
             if (data['password']) {
                 data['password'].forEach(function(item) {
                     password_error_log.append(item);
                     password_error_log.show();
                 });
             }
             if (data['user']) {
                 other_errors_log.append(data['user']);
                 other_errors_log.show();
             }
             if (typeof data === 'string') {
                 window.location.href = data;
             }
         },
         error: function (data) {
             alert('Stop hacking my site !');
         }
    });
    return false;
});
