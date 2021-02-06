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
    path('badcomments/<int:comment_pk>/', views.badcomment),

    path('<int:comment_pk>/recomments/', views.create_recomment),
    path('recomments/', views.recomment_list),
    path('recomments/<int:recomment_pk>/', views.recomment_detail_update_delete),
    path('badrecomments/<int:recomment_pk>/', views.badrecomment),

    path('<int:article_pk>/like/', views.like),
    path('<int:comment_pk>/comment_like/', views.like_comment),
    path('<int:article_pk>/scrap/', views.scrap),

    path('myscrap/<int:user_pk>/',views.myscrap),

    path('club/<int:club_pk>/',views.club_article),

    path('make_hashtag/',views.hashtag_suggest),

    path('search_bar/',views.search_bar),

    #path('comment_emotion',views.comment_emotion),
]