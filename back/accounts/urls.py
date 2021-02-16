from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('userid_check/', views.userid_check),
    path('nickname_check/', views.nickname_check),
    path('email_check/', views.email_check),
    path('user_delete/', views.user_delete),
    path('user_update/', views.user_update),
    path('api-token-auth/', obtain_jwt_token),
    path('login/', views.login),
    path('make_admin/', views.make_admin),
    path('get_user/', views.get_user),
    path('get_user_id/', views.get_user_id),
    path('passwordChange/', views.passwordChange),
    path('sendPassword/', views.sendPassword),

    path('alarm/',views.alarm),
    path('alarm_total/',views.alarm_total),
    path('alarm_check/',views.alarm_check),
    # path('<int:user_pk>/mypage/',views.mypage),
    path('profile_image/<str:user_id>/',views.profile_image),
]