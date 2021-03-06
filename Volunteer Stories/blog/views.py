from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from accounts.models import Author, Image
from blog.forms import CommentForm, PostForm
from blog.models import Category, SubCategory, Newsletter, Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        page_name = "Home"
        featured_posts = Post.objects.filter(featured=True)[0:3]
        latest_posts = Post.objects.order_by("-timestamp")[0:2]
        images = Image.objects.filter(is_active=True)
        hero_images = [image for image in images if image.is_hero]
        divider_images = [image for image in images if image.is_divider]
        gallery_images = [image for image in images if image.is_gallery]
        hero_image = hero_images[0] if hero_images else None
        divider_image = divider_images[0] if divider_images else None
        is_subscribed = False
        if request.user.is_authenticated:
            is_subscribed = Newsletter.objects.filter(
                Q(email=request.user.email)
            ).exists()
        context = {
            "page_name": page_name,
            "featured_posts": featured_posts,
            "latest_posts": latest_posts,
            "hero_image": hero_image,
            "divider_image": divider_image,
            "gallery_images": gallery_images,
            "is_subscribed": is_subscribed,
        }
        return render(request, "blog/index.html", context=context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        print("Email", email)
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()
        messages.info(request, "Successfully subscribed!")
        return redirect("index")


def post_detail_view(request, slug):
    post = Post.objects.get(slug=slug)
    latest_posts = Post.objects.all().order_by("-timestamp")[0:3]
    similar_posts = Post.objects.filter(category=post.category)[0:3]
    categories = Category.objects.all()

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.instance.user = request.user.author
        comment_form.instance.post = post
        comment_form.save()
        return redirect(reverse("post_detail", kwargs={"slug": post.slug}))
    context = {
        "post": post,
        "latest_posts": latest_posts,
        "categories": categories,
        "similar_posts": similar_posts,
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context=context)


class PostListView(ListView):
    page_name = "Blog"
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = self.page_name
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:3]
        context["categories"] = Category.objects.all()
        return context


def categorized_post_view(request, category):
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(category=category)
    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "blog/categorized_post.html", context=context)


class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get("q", "")
        search_result = Post.objects.filter(
            Q(title__icontains=q) | Q(overview__icontains=q)
        ).all()
        context = {"search_result": search_result}
        return render(request, "blog/search.html", context=context)


def post_create_view(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = Author.objects.filter(user=request.user).first()
        instance.slug = slugify(instance.title, instance.id)
        instance.save()
        messages.success(request, "Successfully created")
        return redirect(reverse("post_detail", kwargs={"slug": instance.slug}))
    context = {"form": form}
    return render(request, "blog/post_create.html", context=context)


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    form_class = PostForm

    def form_valid(self, form):
        if form.instance.author == self.request.user.author:
            form.save()
            return redirect(reverse("post_detail", kwargs={"slug": form.instance.slug}))


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("index")


def load_sub_categories(request):
    category = request.GET.get("category")
    print(category)
    subcategories = SubCategory.objects.filter(category=category)
    return render(request, "blog/sub-categories.html", {"subcategories": subcategories})
