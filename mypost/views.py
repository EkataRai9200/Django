from django.shortcuts import render


# Create your views here.
def addPost(request):
    return render(request, 'posts.html')
