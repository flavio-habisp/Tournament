from django.urls import path
from . import views


urlpatterns = [
    path('ajax/validate/', views.validate, name='validate'),
    path('tournament_form/', views.tournament_form, name='tournament_form'),
    path('tournament_new/', views.tournament_new, name='tournament_new'),
    path('tournament_del/<int:pk>/', views.tournament_del, name='tournament_del'),
    path('tournament/<int:pk>/', views.tournament, name='tournament'),

]
