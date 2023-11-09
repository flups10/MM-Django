from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):

    User.objects.get_or_create({
            'name': request.POST['name'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'job_title': request.POST['job_title']
            })

    response = HttpResponse('test')
    response.set_cookie('user_cookie', request.POST['email'])
    return redirect('members')


def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
    except (User.DoesNotExist):
        raise Http404("User does not exist")

    print(request.POST['password'])

    response = HttpResponse('test')
    response.set_cookie('user_cookie', request.POST['email'])
    return redirect('members')


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('user_cookie')
    return response

def members(request):
    print(request.user)
    if request.user == None:
        redirect('/')
    members = User.objects.all()
    context = {'members': members}
    return render(request, 'users/members.html', context)
    

def profile(request, member_id):
    user = User.objects.get(pk=member_id)

    context = {
        'name': user.name,
        'job_title': user.job_title
    }
    return render(request, 'users/profile.html', context)