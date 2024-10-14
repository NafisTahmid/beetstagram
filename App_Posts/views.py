from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_Login.models import UserProfile, Follow
from App_Posts.models import Post, Like
from App_Posts.forms import CommentForm, EditPostForm
from django.urls import reverse

# Create your views here.
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in = following_list.values_list('following'))
    already_liked = Like.objects.filter(user=request.user)
    liked_post_list = already_liked.values_list('post', flat=True)

    # initialize variables
    search = ''
    result = None
 
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains = search)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            post_id = request.POST.get('post_id')
            post = Post.objects.get(pk = post_id)
            comment.post = post
            comment.save()
    return render(request, 'App_Posts/home.html', context={'search':search, 'result':result, 'posts':posts, 'liked_post_list':liked_post_list, 'comment_form':comment_form})


@login_required
def liked(request, pk):
    post = Post.objects.get(pk = pk)
    already_liked = Like.objects.filter(post = post, user = request.user)

    if not already_liked:
        liked = Like(user = request.user, post = post)
        liked.save()
    return HttpResponseRedirect(reverse('App_Posts:post_details', kwargs={'pk':post.pk}))


@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(user=request.user, post=post)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Posts:post_details', kwargs={'pk':post.pk}))


@login_required
def post_details(request, pk):
    post = Post.objects.get(pk = pk)
    already_liked = Like.objects.filter(user=request.user, post=post)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            post = Post.objects.get(pk = pk)
            comment.post = post
            comment.save()
    return render(request, 'App_Posts/post_details.html', context={'post':post, 'already_liked':already_liked, 'comment_form':comment_form})


@login_required
def edit_post(request, pk):
    post = Post.objects.get(pk = pk)
    form = EditPostForm(instance = post)
    
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance = post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = request.user
            updated_post.image = post.image
            updated_post.save()
            return HttpResponseRedirect(reverse('App_Posts:post_details', kwargs={'pk':updated_post.pk}))

    return render(request, 'App_Posts/edit_post.html', context={'form':form})

@login_required
def delete_post(request, pk):
    selected_post = Post.objects.get(pk=pk)
    selected_post.delete()
    return HttpResponseRedirect(reverse('App_Login:profile'))