from django.urls import path
from states import views

urlpatterns = [
    path('states/', views.StateList.as_view()),
    path('states/<int:pk>/', views.StateDetail.as_view()),
]
