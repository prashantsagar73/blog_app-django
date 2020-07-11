from django.shortcuts import render, HttpResponse


# Create your views here.
def blogHome(request):
    return render(request,'blog/bloghome.html')
    # return HttpResponse('this is blogHome. all the blog post will be here')
def blogPost(request,slug):
    return render(request,'blog/blogpost.html')

    # return HttpResponse(f'this is blogPost{slug}')    
 