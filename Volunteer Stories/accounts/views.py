from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.forms import AuthorForm, UserForm, UserUpdateForm, VolunteerJoinForm
from accounts.models import Author
from blog.models import Newsletter


class AuthorCreateView(CreateView):
    template_name = "accounts/author_form.html"
    form_class = UserForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        Author.objects.create(user=user)
        Newsletter.objects.create(email=user.email)
        return super().form_valid(form)


class AuthorUpdateView(View):
    def get(self, request, *args, **kwargs):
        author_form = AuthorForm(instance=request.user.author)
        user_form = UserUpdateForm(instance=request.user)
        context = {"author_form": author_form, "user_form": user_form}
        return render(request, "accounts/author_update.html", context=context)

    def post(self, request, *args, **kwargs):
        author_form = AuthorForm(
            request.POST, request.FILES, instance=request.user.author
        )
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if author_form.is_valid() and user_form.is_valid():
            user_form.save()
            author_form.save()
        return redirect("accounts_update")


def about_us_view(request):
    page_name = "About"
    context = {
        "page_name": page_name,
    }
    return render(request, "utility/about_us.html", context)


def our_team_view(request):
    return render(
        request,
        "utility/our_team.html",
    )


def join_us_view(request):
    page_name = "Join"
    form = VolunteerJoinForm()
    if request.method == "POST":
        form = VolunteerJoinForm(request.POST)
        print(form)
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
