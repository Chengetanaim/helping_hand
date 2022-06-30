from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView
from .forms import PostForm, CommentForm


class IndexView(ListView):
    queryset = Post.objects.order_by('-date_added')
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/index.html'


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('-date_added')
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/post.html', context)


def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    context = {'form': form}
    return render(request, 'blog/new_post.html', context)


def new_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.save()
        return redirect('blog:post', post_id=post_id)
    context = {'form': form, 'post': post}
    return render(request, 'blog/new_comment.html', context)


def about_us(request):
    return render(request, 'blog/about_us.html')




