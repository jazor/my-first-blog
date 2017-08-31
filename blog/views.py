from django.shortcuts import render

from blog.models import Post


def post_list(request):

    posts = Post.objects.select_related('author')

    return render(request, 'blog/post_list.html',
                  {'posts': posts})
