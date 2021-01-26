from django.urls import path
from . import views

urlpatterns = [
    path('',views.issuemaker),
    path('issue_search/',views.issue_search),
    # path('youtube/',views.youtube),
    # path('naver_search/',views.naver_search),
]
