from django.urls import path

from rules import views

urlpatterns = [
    path("rules/", views.RuleView.as_view()),
    path("rules/<str:pk>/", views.RuleDetailView.as_view()),
]
