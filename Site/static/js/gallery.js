/**
 * Created by mv on 11.02.2016.
 */

var allPhotos = document.querySelectorAll('.photos'),
    photosArray = [].slice.call(allPhotos),
    currentImg;


var photosHref = photosArray.map(function(photo) {
    return photo.src;
});

photosArray.forEach(function (photo) {
        photo.addEventListener('click', function () {
            $('#galleryModal').modal();
            currentImg = this;
            pasteNewImg(currentImg);
        });
});

document.body.addEventListener('keydown', function(elem) {
    if (elem.keyCode === 112) {
        $('.control-modal').modal()
    }

    var currentPhotoNumber,
        newNumber;

    if (typeof currentImg !== 'undefined') {
        currentPhotoNumber = photosHref.indexOf(currentImg.src);
        if (elem.keyCode === 37) {
            newNumber = currentPhotoNumber - 1;
            if (newNumber >= 0) {
                pasteNewImg(allPhotos[newNumber]);
                currentImg = allPhotos[newNumber];
            }
        }
        if (elem.keyCode === 39) {
            newNumber = currentPhotoNumber + 1;
            if (newNumber < allPhotos.length) {
                pasteNewImg(allPhotos[newNumber]);
                currentImg = allPhotos[newNumber];
            }
        }
    }
});

var galleryModalPicture = document.querySelector('#galleryModal .modal-body .modal-picture');
var loadGig = document.getElementById('loadGif');

var pasteNewImg = function (photo, flag) {
    galleryModalPicture.src = photo.src;
    galleryModalPicture.title = photo.title;
    if (!flag) {
        window.history.pushState({src: photo.src, title: photo.title}, null, null);
    }
    currentImg = photo;
    setCookie('current_image', photo.src);
    loadNewImg(galleryModalPicture, loadGig);
    getLikesForImage(photo.src);
    getComments(photo.src);
};

function loadNewImg(img, gif) {
    img.classList.remove('loaded');
    gif.classList.remove('hide');
    img.onload =  function() {
        this.classList.add('loaded');
        gif.classList.add('hide');
    }
}

window.addEventListener('popstate', function(e) {
    if (e.state !== null) {
        pasteNewImg(e.state, true);
    } else {
        $('#galleryModal').modal("hide");
    }
}, false);

function setCookie(name, value, exp) {
    if (typeof exp !== 'undefined') {
        document.cookie = name + '=' + value + ';' + 'expires=' + exp.toUTCString() + ';';
    } else {
        document.cookie = name + '=' + value + ';';
    }
}

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        '(?:^|; )' + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + '=([^;]*)'
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

window.onunload = function() {
    if ($('#galleryModal').is(':visible')) {
        setCookie('reload', true, new Date(new Date().getTime() + 10 * 1000));
    }
};

window.onload = function() {
    if (getCookie('reload') === 'true') {
        $('#galleryModal').modal();
        pasteNewImg({src: getCookie('current_image'), title:'Выживший'}, true);
        setCookie('reload', false);
    }
};

// 4-й таск (Супер-лайк)
var likeOne = $('#likes-icon');

likeOne.click(function () {  // Ничего не делаем с РЕФЕРОМ, а стоило бы
    $.ajax({
        type:'GET',
        url: '/is-authenticated/',
        success: function(data) {
            if (data === 'True') {
                $.ajax({
                    type:'POST',
                    url: '/gallery/like/',
                    data: {
                        href: $('#currentImage').attr('src')
                    },
                    success: function(data) {
                        $('#likes-counter').empty().append(data);
                    },
                    error: function (data) {
                        alert('Stop hacking my site !');
                    }
                });
            }
        },
        error: function (data) {
            alert('Stop hacking my site !');
        }
    });
});

function getLikesForImage (href) {  // Ничего не делаем с РЕФЕРОМ, а стоило бы
    $.ajax({
         type:'GET',
         url: '/gallery/get-likes/',
         data: {
             href: $('#currentImage').attr('src')
         },
         success: function(data) {
             $('#likes-counter').empty().append(data);
         },
         error: function (data) {
             alert('Stop hacking my site !');
         }
    });
}