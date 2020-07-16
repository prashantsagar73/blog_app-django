from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.db import IntegrityError
from django.contrib.auth.models import User

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

def handelsignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        name= request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username)>12:
            messages.error(request,"Username must be under 12 character")
            return redirect('home') 
        if not username.isalnum():
            messages.error(request,"Username contain only letters and number")
            return redirect('home') 
        if pass1 != pass2:
            messages.error(request,"Passworddo not match")
            return redirect('home')  

        # creating users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else: 
        return HttpResponse ('404 - Not Found')


 