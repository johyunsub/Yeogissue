from django.urls import path
from . import views 


urlpatterns = [
    path('', views.article_create),
    path('articles/<int:article_pk>/', views.article_detail),

]