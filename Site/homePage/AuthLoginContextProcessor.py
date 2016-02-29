from homePage.forms import RegistrationForm, AuthenticationForm

def authLoginForm(request):
    context = {'registrationForm': RegistrationForm(), 'autheticationForm': AuthenticationForm()}
    return context