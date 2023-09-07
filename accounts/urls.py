from django.urls import path

from accounts import views
from accounts.views import SubmitStoryView

urlpatterns = [
    path("about-us", views.about_us_view, name="about_us"),
    path("our-team", views.our_team_view, name="our_team"),
    path('submit-your-story/', SubmitStoryView.as_view(), name='submit_your_story'),
    path("join-as-a-volunteer", views.volunteer_join_view, name="volunteer_join"),

]
