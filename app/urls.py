from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', sign_up),
    path('sign-in/', sign_in),
    path('admin/add-occupation/', add_occupation),
    path('admin/start-event/', start_event),
    path('admin/agenda/', set_agenda_activities),
    path('admin/challenges/', set_challenges),
    path('team/register/', team_registration),
    path('participant/register/', participant_registration),
    path('admin/accept-team/', accept_team),
    path('admin/affect-mentors/', affect_mentors),
    path('admin/affect-judge/', affect_judge),
    path('team/request-mentor/', request_mentor),
    path('team/get-mentoring-requests/<str:pk>/', get_mentoring_requests),
]
