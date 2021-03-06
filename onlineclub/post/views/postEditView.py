from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from post.models import *


# def post_edit(request, id):
#     edit_post = Posts.objects.get(post_id=id)
#     return render(request, 'post/edit.html', {'post':edit_post})

# def post_update(request, id):
#     update_post = Posts.objects.get(post_id=id)
#     update_post.post_title = request.POST['post_title']
#     update_post.post_content = request.POST['post_content']
#     update_post.post_img_url = request.POST['post_img_url']
#     update_post.updated_at = timezone.now()
#     update_post.save()
#     return redirect('detail', str(update_post.post_id))


def club(request):
    #동아리 이름과 동아리 한줄 설명 가져오기 위해서
    club = Clubs.objects.all()
    return render(request, 'home.html', {'club':club})



def detailpage_update(request, id, pk):
    update_detailpage = Clubs.objects.get(club_id=id, club_detail_id=pk)

    if request.method =="POST":
    
        update_detailpage.club_desc = request.POST.get('club_desc')
        update_detailpage.recruitment_content = request.POST.get('recruitment_content')
        update_detailpage.save()
        return redirect('detail' , str(update_detailpage.club_id))

    else:
        return render(request,'edit.html',{'club':club}, str(update_detailpage.club_detail_id))

