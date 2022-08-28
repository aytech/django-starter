from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def page_not_found(request, path):
    return render(request, 'index.html', {'path': path})
