var commentForm = $('#commentForm');

$('#commentSubmit').click(function () {
    commentForm.submit();
});

commentForm.submit(function () {
    var href = $('#currentImage').attr('src');

    $.ajax({
        type: 'POST',
        url: '/gallery/send-comment/',
        data: {
            comment: $('#newComment').val(),
            href: href,
            csrfmiddlewaretoken: $.cookie('csrftoken')
        },
        success: function (data) {
            // Возвращает сообщение, но по сути мы его нигде не используем
            $('#newComment').val('');
            $('.markItUpPreviewFrame').remove();
            if (typeof data === 'string') {
                if (data !== 'take it easy !') {
                    window.location.href = data;
                }
            }
            else {
                getComments(href);
            }
        },
        error: function (data) {
            alert('Stop hacking my site !');
        }
    });
    return false;
});

var comments = $('#allComments');

function getComments (href) {
    $.ajax({
        type: 'GET',
        url: '/gallery/get-comments/',
        data: {
            href: href
        },
        success: function (data) {
            if (typeof data === 'string') {
                window.location.href = data;
            }
            else {
                comments.empty();
                for (var counter in data) {
                    comments.append(data[counter]);
                }
            }
        },
        error: function (data) {
            alert('Stop hacking my site !');
        }
    });
}

function deleteComment (id) {
    $.ajax({
         type:'POST',
         url: '/gallery/delete-comment/' + id,
         success: function(data) {
             if (typeof data === 'string'){
                 if (data !== 'OK') {
                     window.location.href = data;
                 }
                 getComments($('#currentImage').attr('src'))
             }
         },
         error: function (data) {
             alert('Stop hacking my site !');
         }
    });
}

var oldIdComment;
var oldComment;

function showEditForm (id) {  // Ничего не делаем с РЕФЕРОМ, а стоило бы
    $.ajax({
         type:'GET',
         url: '/gallery/get-edit-form/' + id,
         success: function(data) {
             // Сгенерили форму, полученную с сервера.
             if (oldIdComment && oldComment) {
                 var oldCommentDiv = $('#comment_' + oldIdComment);
                 oldCommentDiv.empty();
                 oldCommentDiv.append(oldComment);
             }
             oldIdComment = id;
             var commentDiv = $('#comment_' + id);
             oldComment = commentDiv.html();
             commentDiv.empty();
             var editForm = $('<form id="edit_form" action="" method="post" role="form"></form>');
             var submitButton = '<input type="submit" name="edit-submit" id="edit-submit" class="form-control btn btn-info" value="Edit comment">';
             editForm.append(data, submitButton);
             commentDiv.append(editForm);
             addList($('#edit_form'), id);
         },
         error: function (data) {
             alert('Stop hacking my site !');
         }
    });
}

function addList(editForm, id) {
    editForm.submit(function() {
        $.ajax({
            type:'POST',
            url: '/gallery/edit-comment/' + id,
            data: {
                comment: $('#id_comment').val()
            },
            success: function(data) {
                if (typeof data === 'string') {
                    if (data !== 'take it easy !') {
                        window.location.href = data;
                    }
                } else {
                    var commentBlock = $('#comment_' + id);
                    commentBlock.replaceWith(data[0]);
                }
            },
            error: function (data) {
                alert('Stop hacking my site !');
            }
        });
        return false;
    });
}