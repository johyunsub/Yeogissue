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
    # path('<int:article_pk>/emotion_comment/',views.emotion_comment),
    path('emotion_comment/',views.emotion_comment),

    path('<int:comment_pk>/recomments/', views.create_recomment),
    path('recomments/', views.recomment_list),
    path('recomments/<int:recomment_pk>/', views.recomment_detail_update_delete),
    path('badrecomments/<int:recomment_pk>/', views.badrecomment),

    path('<int:article_pk>/like/', views.like),
    path('<int:comment_pk>/comment_like/', views.like_comment),
    path('<int:article_pk>/scrap/', views.scrap),

    path('myscrap/<int:user_pk>/',views.myscrap),
    path('my_articles/',views.my_articles),

    path('club/<int:club_pk>/',views.club_article),

    path('make_hashtag/',views.hashtag_suggest),

    path('search_bar/',views.search_bar),

    #path('comment_emotion',views.comment_emotion),

    path('top_hashtag/', views.top_hashtag),

    path('my_emotion/', views.my_emotion),

    
    path('comment_rank/', views.comment_rank),
    path('like_rank/', views.like_rank),

    path('hash_emotion/', views.hash_emotion),
    path('hash_all/', views.hash_all),
]