from django.urls import path
from . import views

urlpatterns = [
    path('',views.issuemaker),
    path('issue_search/news/',views.issue_news),
    path('issue_search/youtube/',views.issue_youtube),
]
