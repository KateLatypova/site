from django.shortcuts import render


def visit_page(request):
    return render(request, 'visit.html', {})
