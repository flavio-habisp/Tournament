from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


def dashboard(request):
    #return render(request, 'account/dashboard.html')
    return render(request, 'tournament/tourney.html')


def tournament(request):
    return render(request, 'matches/tournament4.html')
