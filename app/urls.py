from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', sign_up),
    path('sign-in/', sign_in),
    path('admin/add-occupation/', add_occupation),
    path('admin/start-event/', start_event),
    path('admin/affect-mentors/', affect_mentors),
]
