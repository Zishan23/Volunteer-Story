from django.shortcuts import redirect, render
from accounts.forms import VolunteerJoinForm


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
    form = VolunteerJoinForm()
    if request.method == "POST":
        form = VolunteerJoinForm(request.POST, request.FILES)
        print(form.errors)
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
