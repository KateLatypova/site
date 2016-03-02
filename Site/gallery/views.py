import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.utils import timezone
from django_markdown.utils import markdown

from gallery.forms import CommentForm, DeleteCommentForm
from gallery.models import AlbumImage, CommentForImage


def main_page(request):
    args = {}
    img_list = AlbumImage.objects.all()
    args['images'] = img_list
    return render(request, 'gallery.html', args)


def get_image(string):
    href = re.search(r'gallery/.*', string).group(0)
    return get_object_or_404(AlbumImage, image=href)


COMMENT_TEMPLATE = """
                    <div id="comment_{{ id }}" class="row">
                        <div class="col-md-12">
                            <section class="comments">
                                <article class="row">
                                    <div class="col-md-12 col-sm-12">
                                        <div class="panel panel-default">
                                            <div class="panel-body">
                                                <header class="comments-header">
                                                    <div class="user">
                                                        <p>
                                                            <span class="fa fa-user"></span>
                                                            {{ author }}
                                                        </p>
                                                    </div>
                                                    <time>
                                                        <span class="fa fa-clock-o"></span>
                                                        {{ created_at }}
                                                    </time>
                                                    {% if edit_or_delete %}
                                                    <form action="edit/delete" method="post">
                                                        <div class="edit-panel">
                                                            <a style="color: black" onclick="showEditForm({{ id }}); return false;" href="get-edit-form/"><span class="fa fa-pencil-square-o" aria-hidden="true"></span></a>
                                                            <a style="color: black" onclick="deleteComment({{ id }}); return false;" href="delete-comment/"><span class="fa fa-times" aria-hidden="true"></span></a>
                                                        </div>
                                                    </form>
                                                    {% endif %}
                                                </header>
                                                <div class="comment-body">
                                                    <p><em>{{ text }}</em></p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </article>
                            </section>
                        </div>
                    </div>
                    """

def get_normal_comment(text_comment):
    text_comment = markdown(text_comment, safe=True)
    if 'HTML_REMOVED' in text_comment:
        return False
    else:
        return text_comment


def get_comment_item(comment, request_user):
    comment_item = {}
    comment_item['author'] = comment.author.username
    textComment = get_normal_comment(comment)
    if textComment:
        comment_item['text'] = textComment
    else:
        return None
    comment_item['created_at'] = timezone.localtime(comment.created_at).ctime()
    comment_item['updated_at'] = timezone.localtime(comment.updated_at).ctime()
    if comment.edits != '':
        old_comments = comment.edits.split('\n\n\n\n')
        old_comments = [comment + '\n' for comment in old_comments]
        comment_item['old_comments'] = old_comments[:len(old_comments)-1]
    comment_item['id'] = comment.id
    if comment_item['author'] == request_user.username:
        comment_item['edit_or_delete'] = True
    else:
        comment_item['edit_or_delete'] = False
    comment_template = Template(COMMENT_TEMPLATE)
    context = Context(comment_item)
    return comment_template.render(context)


def get_comments(request):
    if request.method == 'GET':
        if request.is_ajax():
            image = get_image(request.GET['href'])
            response = {}
            counter = 0
            for comment in image.comments.all():
                comment_item = get_comment_item(comment, request.user)
                if comment_item:
                    response[counter] = comment_item  # just dict
                    counter += 1
            return JsonResponse(response)
    return HttpResponse(request.META['HTTP_REFERER'])


@login_required
def send_comment(request):
    if request.method == 'POST':
        if request.is_ajax():
            if request.user.is_authenticated():
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    image = get_image(request.POST['href'])
                    comment.imageObject = image
                    comment.author = User.objects.get(username=request.user.get_username())
                    tempComment = get_normal_comment(request.POST['comment'])
                    if tempComment:
                        comment.text = request.POST['comment']
                        comment.save()
                        responseComment = get_comment_item(comment, request.user)  # just text
                        return JsonResponse({'comment': responseComment})
                    else:
                        return HttpResponse('take it easy !')
    return HttpResponse(request.META['HTTP_REFERER'])


@login_required
def delete_comment(request, id_comment):  # Поправить CSRF token
    if request.method == 'POST':
        if request.is_ajax():
            if request.user.is_authenticated():
                form = DeleteCommentForm(data=request.POST)
                if form.is_valid():
                    comment = get_object_or_404(CommentForImage, id=id_comment)
                    if comment.author.username == request.user.username:
                        comment.delete()
                        return HttpResponse('OK')
    return HttpResponse(request.META['HTTP_REFERER'])


@login_required
def get_edit_form(request, id_comment):  # Недоработанное место, нет перекида на РЕФЕРЕР в случае чего (смотри JS)
    if request.method == 'GET':
        if request.is_ajax():
            if request.user.is_authenticated():
                comment = get_object_or_404(CommentForImage, id=id_comment)
                if comment.author.username == request.user.username:
                    form = CommentForm(initial={'comment': comment.text})
                    edit_form_template = Template("{{ form.comment }}")
                    context = Context({'form': form})
                    edit_form_template.render(context)
                    return HttpResponse(edit_form_template.render(context))
    return HttpResponse(request.META['HTTP_REFERER'])


@login_required
def edit_comment(request, id_comment):
    if request.method == 'POST':
        if request.is_ajax():
            if request.user.is_authenticated():
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    comment = get_object_or_404(CommentForImage, id=id_comment)
                    if comment.author.username == request.user.username:
                        temp_comment = get_normal_comment(request.POST['comment'])
                        if temp_comment:
                            comment.edits = comment.edits + timezone.localtime(comment.updated_at).ctime() + '\n' + comment.text + '\n\n\n\n'
                            comment.updated_at = timezone.now()
                            comment.text = request.POST['comment']
                            comment.save()
                            response_comment = get_comment_item(comment, request.user)
                            return JsonResponse({0: response_comment})
                        else:
                            HttpResponse('take it easy !')
    return HttpResponse(request.META['HTTP_REFERER'])


@login_required
def add_like(request):  # Недоработанное место, нет перекида на РЕФЕРЕР в случае чего (смотри JS)
    if request.method == 'POST':
        if request.is_ajax():
            if request.user.is_authenticated():
                image = get_image(request.POST['href'])
                if request.user in image.likes.all():
                    image.likes.remove(request.user)
                else:
                    image.likes.add(request.user)
                return HttpResponse(str(len(image.likes.all())))
    return HttpResponse(request.META['HTTP_REFERER'])


def get_likes(request):  # Недоработанное место, нет перекида на РЕФЕРЕР в случае чего (смотри JS)
    if request.method == 'GET':
        if request.is_ajax():
            image = get_image(request.GET['href'])
            return HttpResponse(str(len(image.likes.all())))
    return HttpResponse(request.META['HTTP_REFERER'])
