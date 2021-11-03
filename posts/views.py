from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import PostForm, PostEditForm, CommentForm, SearchForm
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_comment = Comment(body=cd['body'],
                                  post=post,
                                  user=request.user)
            new_comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'post': post,
                                           'form': form,
                                           'comments': comments})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            cd = form.cleaned_data
            new_post = Post(title=cd['title'],
                            image=request.FILES['image'],
                            body=cd['body'],
                            author=request.user)
            new_post.save()

            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create.html', locals())


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.POST:
        form = PostEditForm(request.POST or None, request.FILES or None, instance=post)

        if form.is_valid():
            post.save()
            return redirect(post.get_absolute_url())

    else:
        form = PostEditForm(
            initial={
                'title': post.title,
                'image': post.image,
                'body': post.body
            }
        )

    return render(request, 'edit.html', locals())


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.POST:
        post.delete()
        return redirect('post_list')
    return render(request, 'delete.html', locals())


def search(request):
    posts = Post.objects.all()
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            target = form.data['search']
            print(target)
            p = Post.objects.filter(
                    Q(title__icontains=target) | Q(body__icontains=target)
                )
            return render(request, 'search_results.html', {'p': p})
    else:
        form = SearchForm()
    return render(request, 'list.html', locals())


# def search(request):
#     target = ''
#     form = SearchForm()
#     if request.POST:
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             target = form.data['search']
#     # posts = Post.objects.filter(title__icontains=target)
#
#     return render(request, 'search_results.html', locals())


