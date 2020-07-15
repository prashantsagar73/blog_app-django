from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    context = {'allPosts' : allPosts}
    return render(request,'blog/bloghome.html',context)
    # return HttpResponse('this is blogHome. all the blog post will be here')
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogpost.html',context)

    # return HttpResponse(f'this is blogPost{slug}')    
 