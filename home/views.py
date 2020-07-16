from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('this is home')

def contact(request):
    # messages.success(request, 'Welcome to conatact.')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<9 or len(content)<5:
            messages.error(request,'Please fill with correct details')
        else:
            contact= Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message has been send.Thankyou for contacting us,we will be touch with you soon.')
    return render(request,'home/contact.html')

def about(request):
    # return HttpResponse('this is about')

    return render(request,'home/about.html')

def search (request):
    query = request.GET['query']
    # query come form search id(basic.html)
    if len(query)>70:
        allPosts = Post.objects.none()
    else:        
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent) 

    if allPosts.count() == 0:
        messages.warning(request,'No search found,Please search  with correct querry')
    params= {'allPosts': allPosts, 'query': query }
    return render(request,'home/search.html',params)

    # return HttpResponse("this is search")   

def handelsignup (request):
    if request.method== 'POST':

    else:
        return HttpResponse ('404 - Not Found')


 