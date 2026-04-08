from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import SignUpForm


class LandingPageView(TemplateView):
    template_name = "landing.html"


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("landing")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})
