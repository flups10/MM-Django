from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
import uuid

import datetime

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):

    try:
        exists = User.objects.get(email = request.POST['email'])
    except User.DoesNotExist:
        leng = User.objects.all().count()

        user = User(
                leng+1,
                request.POST['name'],
                request.POST['email'],
                request.POST['job_title'],
                request.POST['password'],
                )

        user.save()
        response = HttpResponseRedirect('/members')
        response.set_cookie('user_cookie', request.POST['email'])
        return response
    
    
    context = {
            'register_message': 'user already exists'
        }
    return render(request, 'users/index.html', context)

def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
        if user.password == request.POST['password']:
            pass
        else:
            return render(request, 'users/index.html', {'login_message': 'incorrect password'})
    except (User.DoesNotExist):
        return render(request, 'users/index.html', {'login_message': 'user does not exist'})
    response = redirect('members')
    response.set_cookie('user_cookie', request.POST['email'])
    return response


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('user_cookie')
    return response


def members(request):
    if request.COOKIES.get('user_cookie'):
        pass
    else:
        return redirect('/')
    members = User.objects.all()
    context = {'members': members,
               'user': request.COOKIES['user_cookie']}
    return render(request, 'users/members.html', context)


def profile(request, member_id):
    user = User.objects.get(pk=member_id)

    context = {
        'name': user.name,
        'job_title': user.job_title
    }
    return render(request, 'users/profile.html', context)

