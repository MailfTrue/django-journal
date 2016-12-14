from .models import Post,Category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-sticky','-published_date')
    category = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts,
                                                    'cat':category})

def post_details(request,pk):
    post = get_object_or_404(Post,pk=pk)
    try:
        next_post = post.get_previous_by_created_date()
        next_post_url = reverse('post_detail',kwargs={'pk': next_post.pk})
    except:
        next_post_url=""

    try:
        prev_post = post.get_next_by_created_date()
        prev_post_url = reverse('post_detail',kwargs={'pk': prev_post.pk})
    except:
        prev_post_url=""

    context = {'post':post,
                'next':next_post_url,
                'prev':prev_post_url}
    return render(request,'blog/post_detail.html', context = context)

def category_posts(request,category):
    category = category.replace("-"," ")
    post = Post.objects.filter(categories__name=category).order_by('-sticky','-published_date')
    categories = Category.objects.all()
    return render(request, 'blog/category_posts.html', {'posts':post,
                                                        'category':category,
                                                        'cat':categories})
