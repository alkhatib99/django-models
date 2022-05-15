from django.urls import path
from .views import SnackDetailView, SnackListView,HomeView
urlpatterns=[
path('',HomeView.as_view(),name="base"),
path('snack-list',SnackListView.as_view(),name='snack_list'),
path('snack-detail/<int:pk>',SnackDetailView.as_view(), name="snack_detail"),

]