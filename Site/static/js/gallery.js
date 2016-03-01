/**
 * Created by mv on 11.02.2016.
 */

var allPhotos = document.querySelectorAll('.photos'),
    photosArray = [].slice.call(allPhotos),
    currentImg;

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
        currentPhotoNumber = photosArray.indexOf(currentImg);
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

var pasteNewImg = function (photo) {
    galleryModalPicture.src = photo.src;
    galleryModalPicture.title = photo.title;
    loadNewImg(galleryModalPicture, loadGig);
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