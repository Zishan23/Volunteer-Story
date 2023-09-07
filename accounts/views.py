from django.shortcuts import redirect, render
from accounts.forms import SubmitStoryModelJoinForm, VolunteerJoinModelForm


def about_us_view(request):
    page_name = "About"
    context = {
        "page_name": page_name,
    }
    return render(request, "utility/about_us.html", context)


def our_team_view(request):
    return render(request, "utility/our_team.html")


def submit_story_view(request):
    page_name = "Submit Story"
    form = SubmitStoryModelJoinForm()
    if request.method == "POST":
        form = SubmitStoryModelJoinForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            context = {
                "page_name": page_name,
                "submitted": True,
            }
            return render(request, "utility/submit_story.html", context)
    context = {
        "page_name": page_name,
        "form": form,
    }
    return render(request, "utility/submit_story.html", context)


def volunteer_join_view(request):
    page_name = "Volunteer Join"
    form = VolunteerJoinModelForm()
    if request.method == "POST":
        form = VolunteerJoinModelForm(request.POST, request.FILES)
        print(form.errors)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            form.save()
            context = {
                "page_name": page_name,
                "submitted": True,
            }
            return render(request, "utility/volunteer_join.html", context)
    context = {
        "page_name": page_name,
        "form": form,
    }
    return render(request, "utility/volunteer_join.html", context)
