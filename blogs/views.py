from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request,category_id):
    # Fetch the post that belongs to category_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    # Fetch the posts that belongs to category with the id category_id
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect user to homepage
        return redirect('home')
        # use get_object_or_404 when you want to show 404 erroe page if category does not exist
        # category = get_object_or_404(Category,pk=category_id)

    context = {
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)