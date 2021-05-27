from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts = [
#     {
#         'author': 'DivyaSD',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'March 09, 2020'
#     },
#     {
#         'author': 'IrsAyvid',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'March 10, 2020'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
