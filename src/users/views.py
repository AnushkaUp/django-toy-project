from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm, UserUpdateForm, AccountUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created! Login Now")
            return redirect("login")
    else:
        form = UserRegisterationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def account(request):
    if request.method == "POST":
        us_form = UserUpdateForm(request.POST, instance=request.user)
        acc_form = AccountUpdateForm(
            request.POST, request.FILES, instance=request.user.account
        )
        if us_form.is_valid() and acc_form.is_valid():
            us_form.save()
            acc_form.save()
            messages.success(request, "Account Updated!")
            return redirect("account")
    else:
        us_form = UserUpdateForm(instance=request.user)
        acc_form = AccountUpdateForm(instance=request.user.account)
    content = {"us_form": us_form, "acc_form": acc_form}
    return render(request, "users/account.html", content)
