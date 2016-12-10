from .models import Post,Category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-sticky','-published_date')
    category = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts,
                                                    'cat':category})

def post_details(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html', {'post':post})

def category_posts(request,category):
    category = category.replace("-"," ")
    post = Post.objects.filter(categories__name=category)
    categories = Category.objects.all()
    return render(request, 'blog/category_posts.html', {'posts':post,
                                                        'category':category,
                                                        'cat':categories})
