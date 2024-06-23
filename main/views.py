from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'This is the home page',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About',
        'content': 'О нас',
        'text_on_page': 'Это крутой шоп, братанчик',
    }
    return render(request, 'main/about.html', context)
