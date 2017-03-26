from django.shortcuts import render
#import time zone
from django.utils import timezone
#include the model we have written in models.py
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
