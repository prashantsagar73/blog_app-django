from django.shortcuts import render, HttpResponse


# Create your views here.
def blogHome(request):
    return HttpResponse('this is blogHome. all the blog post will be here')
def blogPost(request,slug):
    return HttpResponse(f'this is blogPost{slug}')    
 