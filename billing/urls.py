from django.urls import path
from .views import MemberBillListView

urlpatterns=[
    path('',MemberBillListView.as_view()),
]

