from django.urls import path
from .views import HabitCompletionList

urlpatterns = [
    path('habit-completions/', HabitCompletionList.as_view(),
         name='habit-completions'),
]
