from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.utils import timezone
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')  #published_date__lte特定用法吧
    return render(request, 'polls/post_list.html', {'posts':posts})


