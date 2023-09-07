from django.contrib.auth.decorators import login_required
from django.urls import path

from accounts import views

urlpatterns = [
    path("about-us", views.about_us_view, name="about_us"),
    path("our-team", views.our_team_view, name="our_team"),
    path("submit-your-story", views.submit_story_view, name="submit_your_story"),
    path("join-as-a-volunteer", views.volunteer_join_view, name="volunteer_join"),
]
