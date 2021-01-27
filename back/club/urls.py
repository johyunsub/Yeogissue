from django.urls import path
from . import views 

urlpatterns = [
    path('',views.club_list),
    path('create/',views.club_create),
    path('club_detail/<str:club_pk>',views.club_detail),
]
