from django.urls import path
from .views import MemberCreateView, MemberProfileView

urlpatterns = [
    path('create/', MemberCreateView.as_view()),
    path('me/', MemberProfileView.as_view()),
]

