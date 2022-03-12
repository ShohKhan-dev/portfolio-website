from django.shortcuts import render

# Create your views here.


def index(request):

    context = {'active_menu':'main'}
    return render(request, 'index.html', context)


def about(request):
    context = {'active_menu':'about'}
    return render(request, 'about.html', context)
    

def blogs(request):
    context = {'active_menu':'blogs'}
    return render(request, 'blogs.html', context)

    


def article(request):
    context = {'active_menu':'article'}
    return render(request, 'article.html', context)


def projects(request):
    context = {'active_menu':'projects'}
    return render(request, 'projects.html', context)


def resume(request):
    context = {'active_menu':'resume'}
    return render(request, 'resume.html', context)



def contact(request):
    context = {'active_menu':'contact'}
    return render(request, 'contact.html', context)