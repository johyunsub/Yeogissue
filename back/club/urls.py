from django.urls import path
from . import views

urlpatterns = [
    path('club_image/<str:club_pk>/', views.club_image),
    path('', views.club_list),
    path('create/', views.club_create),
    path('club_detail/<str:club_pk>/', views.club_detail),
    path('club_article/', views.club_article),
    path('club_article_list/<str:club_pk>/news/', views.club_article_list_news),
    path('club_article_list/<str:club_pk>/youtube/',views.club_article_list_youtube),
    path('club_article_list/<str:club_pk>/etc/', views.club_article_list_etc),
    path('club_article_detail/<str:club_article_pk>/', views.club_article_detail),
    path('club_signup/<str:club_pk>/', views.club_signup),
    path('member_approve/<str:club_pk>/', views.member_approve),
    path('member_delete/<str:club_pk>/<str:member_id>/', views.member_delete),
    path('member_check/<str:club_pk>/', views.member_check),
    path('club_member_delete/<str:club_pk>/', views.club_member_delete),
    path('myclub/', views.myclub),
]
