from django.shortcuts import render, redirect
from .models import Question
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateQuestion, AnswerForm, UpdateForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
def home_view(request):
    content = {"posts": Question.objects.order_by("-date_posted").all()}
    return render(request, "questionapp/home.html", content)


@login_required
def detail_view(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    form = AnswerForm()
    if request.method == "POST":
        question.answer_set.create(
            answer=request.POST.get("answer"), author=request.user
        )
    answers = question.answer_set.all()
    content = {"posts": question, "answer_form": form, "answers": answers}
    return render(request, "questionapp/detail-view.html", content)


@login_required
def create_question(request):
    if request.method == "POST":
        form = CreateQuestion(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user

            p.save()
            messages.success(request, "Question Created!")
            return HttpResponseRedirect(reverse("detail-view", args=(p.id,)))
    else:
        form = CreateQuestion()
    return render(request, "questionapp/question_form.html", {"form": form})


@login_required
def delete_question(request, question_id):
    question = Question.objects.filter(id=question_id).first()
    question.delete()
    messages.success(request, "Your question Has been deleted!")
    return redirect("app-home")


@login_required
def update_question(request, question_id):
    if request.method == "POST":
        question = Question.objects.filter(id=question_id).first()
        form = UpdateForm(request.POST)
        if form.is_valid():
            t1 = request.POST.get("title")
            t2 = request.POST.get("content")
            question.title = t1
            question.content = t2
            question.save()
            messages.success(request, "Question Updated!")
            return redirect("app-home")
    elif request.method == "GET":
        question = Question.objects.filter(id=question_id).first()
        form = UpdateForm(instance=question)
    return render(
        request, "questionapp/update-form.html",
        {"form": form, "question": question}
    )


@login_required
def my_questions(request, user_id):
    user = User.objects.get(id=user_id)
    questions = user.question_set.all()
    content = {"questions": questions, "username": user.username}
    return render(request, "questionapp/my-questions.html", content)


def error_404(request, exception):
    return render(request, "error/error-404.html")


def error_403(request, exception):
    return render(request, "error/error-403.html")


def error_500(request):
    return render(request, "error/error-500.html")
