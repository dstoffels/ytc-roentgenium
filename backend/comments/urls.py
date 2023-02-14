from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('comments/', views.comments_table),
    path('comment/', views.add_comment),
    path('comments/<int:comment_id>/', views.edit_comment),
    path('comments/<int:comment_id>/replies/', include('replies.urls')),
]
