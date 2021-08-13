from django.contrib import admin
from django.urls import path, include
from post.views import postView, postEditView

urlpatterns = [
    path('', postEditView.club, name="home"),
    path('<int:id>', postView.detail, name="detail"),
    path('new/', postView.new, name="new"),
    path('create/', postView.create, name="create"),
    path('<int:id>/delete', postView.delete, name="delete"),
    path('<int:id>/edit/<int:club_detail_id>', postEditView.detailpage_update, name="detailupdate"),
    
]