from django.urls import path

from habit_tracker import views

urlpatterns = [

    path('habit-completions/', views.HabitCompletionList.as_view()),
    path('habit-completions/<int:pk>/', views.HabitCompletionDetail.as_view()),

]
