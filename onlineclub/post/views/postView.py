from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from post.models import *


def home(request):
    posts = Posts.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail(request, id):
    club = get_object_or_404(Clubs, club_id=id)
    return render(request, 'detail.html', {'club':club})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_club= Clubs()
    new_club.club_desc = request.POST.get('club_desc','설명을 입력해주세요')
    new_club.recruitment_content = request.POST.get('recruitment_content','모집요강 작성 란입니다.')
    new_club.save()
    return redirect('detail', str(new_club.club_id))

def delete(request, id):
    delete_post = Posts.objects.get(post_id=id)
    delete_post.is_deleted = 1
    delete_post.delete()
    return redirect('home')