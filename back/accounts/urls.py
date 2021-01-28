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
    path('make_admin/', views.make_admin),
]