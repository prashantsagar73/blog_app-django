from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post,BlogComment
from django.contrib import messages


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    context = {'allPosts' : allPosts}
    return render(request,'blog/bloghome.html',context)
    # return HttpResponse('this is blogHome. all the blog post will be here')
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post':post, 'comments':comments}
    return render(request,'blog/blogpost.html',context)

    # return HttpResponse(f'this is blogPost{slug}')
     
def postComment(request):
    if request.method == "POST": 
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")   
        post = Post.objects.get(sno=postSno)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request,"Your comment has been posted successfully")

    return redirect(f"/blog/{post.slug}")       
 