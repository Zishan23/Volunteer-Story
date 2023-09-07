from django.shortcuts import redirect, render
from django.views import View
from accounts.forms import SubmitStoryModelJoinForm, VolunteerJoinModelForm
from accounts.models import TeamMemberModel


def about_us_view(request):
    page_name = "About | "
    context = {
        "page_name": page_name,
    }
    return render(request, "utility/about_us.html", context)


def our_team_view(request):
    page_name = "Our Team | "
    team_members = TeamMemberModel.objects.filter(is_active=True, is_deleted=False)
    context = {
        "page_name": page_name,
        "team_members": team_members,
    }
    return render(request, "utility/our_team.html", context)


# def submit_story_view(request):
#     page_name = "Submit Story | "
#     form = SubmitStoryModelJoinForm()
#     if request.method == "POST":
#         form = SubmitStoryModelJoinForm(request.POST, request.FILES)
#         print(form.errors)
#         if form.is_valid():
#             form.save()
#             context = {
#                 "page_name": page_name,
#                 "submitted": True,
#             }
#             return render(request, "utility/submit_story.html", context)
#     context = {
#         "page_name": page_name,
#         "form": form,
#     }
#     return render(request, "utility/submit_story.html", context)


class SubmitStoryView(View):
    template_name = "utility/submit_story.html"
    page_name = "Submit Story | "

    def get(self, request, *args, **kwargs):
        form = SubmitStoryModelJoinForm()
        context = {
            "page_name": self.page_name,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SubmitStoryModelJoinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                "page_name": self.page_name,
                "submitted": True,
            }
            return render(request, self.template_name, context)
        else:
            print(form.errors)

        context = {
            "page_name": self.page_name,
            "form": form,
        }
        return render(request, self.template_name, context)


def volunteer_join_view(request):
    page_name = "Volunteer Join | "
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
