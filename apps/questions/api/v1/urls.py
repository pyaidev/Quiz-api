from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('question-list/', QuestionsListView.as_view()),
    path('answer/', AnswerQuestionsView.as_view()),
    path('quiz-list/', QuizListView.as_view()),
    path('subject-list/', SubjectView.as_view()),
    path('statistics/',StatisticView.as_view()),
]
