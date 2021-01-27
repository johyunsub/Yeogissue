from django.urls import path
from . import views 


urlpatterns = [
    path('article_list/', views.article_list),
    path('article_create/', views.article_create),
    path('<int:article_pk>/', views.article_detail),

]