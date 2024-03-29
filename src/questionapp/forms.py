from .models import Question, Answer
from django import forms


class CreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "title",
            "content",
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "answer",
        ]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "title",
            "content",
        ]
