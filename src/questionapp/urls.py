from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="app-home"),
    path(
        "question/<int:question_id>/",
        views.detail_view,
        name="detail-view",
    ),
    path(
        "question/new/",
        views.create_question,
        name="question-create",
    ),
    path(
        "my-questions-<int:user_id>/", views.my_questions, name="my-questions"
    ),
    path(
        "my-questions-<int:question_id>/delete",
        views.delete_question,
        name="delete-question",
    ),
    path(
        "my-questions-<int:question_id>/update",
        views.update_question,
        name="update-question",
    ),
]
