from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', sign_up),
    path('sign-in/', sign_in),
    path('admin/add-occupation/', add_occupation),
    path('admin/start-event/', start_event),
    path('agenda/', set_agenda_activities),
    path('team/register/', team_registration),
    path('participant/register/', participant_registration),
    path('admin/accept-team/', accept_team),
    path('admin/affect-mentors/', affect_mentors),
    path('admin/affect-judge/', affect_judge),
]
