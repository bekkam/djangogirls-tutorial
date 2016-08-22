from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
"""
The dot before models means current directory or current application.
Both views.py and models.py are in the same directory. This means we can use .
and the name of the file (without .py).
Then we import the name of the model (Post).
"""
from .models import Post


def post_list(request):
    """Get published posts ordered by publish date"""

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # pass to render: everything received from user via inet, template file, args for template to use
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Return the specified post detail, else 404"""

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    """Add a post"""

    if request.method == "POST":
        # construct the PostForm with data from the form
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # post_detail is the name of the view we want to go to.
            # Remember that this view requires a pk variable. To pass it to
            # the views we use pk=post.pk, where post is the newly created blog post!
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    """Edit a post"""

    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
