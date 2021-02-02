from django.urls import path
from . import views 


urlpatterns = [
    path('article_list/', views.article_list),
    path('article_create/', views.article_create),
    path('<int:article_pk>/', views.article_detail),
    path('hashtag/<int:article_pk>/',views.hashtag_create),

    path('<int:article_pk>/comments/', views.create_comment),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),

    path('<int:comment_pk>/recomments/', views.create_recomment),
    path('recomments/', views.recomment_list),
    path('recomments/<int:recomment_pk>/', views.recomment_detail_update_delete),

    path('<int:article_pk>/like/', views.like),
    path('<int:article_pk>/scrap/', views.scrap),
]