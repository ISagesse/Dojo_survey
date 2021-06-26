from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    request.session['user_name'] = request.POST['user_name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    return redirect("/")

def result(request):
    context = {
        'name': request.session['user_name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment']
    }
    return render(request, 'result.html', context)