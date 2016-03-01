from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as djangoLogin, logout as djangoLogout, authenticate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render

from homePage.forms import RegistrationForm, AuthenticationForm


def index_page(request):
    return render(request, 'index.html', {})


def description_page(request):
    return render(request, 'description.html', {})


def register(request):
    if request.is_ajax():
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            newUser = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password2'])
            newUser.first_name = request.POST['firstname']
            newUser.last_name = request.POST['lastname']
            newUser.save()
            newUser = authenticate(username=request.POST['username'], password=request.POST['password2'])
            djangoLogin(request, newUser)
            return HttpResponse(request.META['HTTP_REFERER'])
        else:
            response = dict([(key, [error for error in value]) for key, value in form.errors.items()])
            return JsonResponse(response)
    return HttpResponse(request.META['HTTP_REFERER'])


def login(request):
    """
    Log in view
    """
    if request.is_ajax():
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    djangoLogin(request, user)
                    return HttpResponse(request.META['HTTP_REFERER'])
                else:
                    response = {'user': 'You were banned !'}
                    return JsonResponse(response)
            else:
                response = {'user': 'Check your input !'}
                return JsonResponse(response)
        else:
            response = dict([(key, [error for error in value]) for key, value in form.errors.items()])
            return JsonResponse(response)
    return HttpResponse(request.META['HTTP_REFERER'])

@login_required
def logout(request):
    djangoLogout(request)
    return redirect(request.META['HTTP_REFERER'])