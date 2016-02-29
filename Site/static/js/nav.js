/**
 * Created by mv on 02.02.2016.
 */

$(document).ready(function() {
    $(".button-contacts").click(function () {
        $(".contacts-links").slideToggle();
    });

    $(".button-nav").click(function () {
        $(".nav-links").slideToggle();
    });

    var login = document.querySelector('.button-auth');
    login.addEventListener('click', function () {
        $('#auth').modal();
    });

    var authLink = document.getElementById('register-form-link');
    var logLink = document.getElementById('login-form-link');
    var authForm = document.getElementById('register-form');
    var logForm = document.getElementById('login-form');

    authLink.addEventListener('click', function (event) {
        authLink.classList.add('active');
        logLink.classList.remove('active');
        authForm.style.display = 'block';
        logForm.style.display = 'none';
        event.preventDefault();
    });

    logLink.addEventListener('click', function (event) {
        this.classList.add('active');
        authLink.classList.remove('active');
        logForm.style.display = 'block';
        authForm.style.display = 'none';
        event.preventDefault();
    })

});

