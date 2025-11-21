from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import post , AboutUs, User
from django.http import Http404
from django.contrib.auth.hashers import make_password
from .forms import ContactForm
from .forms import postForm
from .forms import registerForm

# static demo data

# posts = [
#         {'id': 1, 'title': 'post 1', 'content': 'content of post 1'},
#         {'id': 2, 'title': 'post 2', 'content': 'content of post 2'},
#         {'id': 3, 'title': 'post 3', 'content': 'content of post 3'},
#         {'id': 4, 'title': 'post 4', 'content': 'content of post 4'},
#         {'id': 5, 'title': 'post 5', 'content': 'content of post 5'},
#     ]


# Create your views here.
def index(request):
    blog_titles = "Bigg Boss Tamil season 9"
    posts = post.objects.all()
    return render(request, "index.html",{'blog_titles': blog_titles, 'posts': posts})


def detail(request, slug):

    # static data 
    # post = next((item for item in posts if item['id'] == int (post_id)), None)

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    
    try:
        #  model post id
         post_obj = post.objects.get(slug=slug)

    except post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, "detail.html", {'post': post_obj})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if form.is_valid():
            logger = logging.getLogger("TESTING")
            logger.debug(f'post data is { form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}')
            success_message = "Form submitted successfully!"
            form = ContactForm()  
            # Clear the form
            return render(request, "contact.html", {'form': form, 'success_message': success_message})

        else:
            logger.debug("form validation failure")   
        return render(request, "contact.html",{'form':form, 'name': name, 'email': email, 'message':message}) 
    return render(request, "contact.html")


def about(request):
    about_obj = AboutUs.objects.first()
    return render(request, "about.html",{'about_content': about_obj.content,'about_title': about_obj.title,'about_img': about_obj.img_url })


def newpost(request):
    form = postForm()
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        title = request.POST.get('title')
        content = request.POST.get('content')
        slug = request.POST.get('slug')
        image_url = request.POST.get('image_url')
        uploaded_file = request.FILES.get('image')
        
        new_post = post(title=title, content=content, slug=slug, img_url=image_url, image=uploaded_file)
        new_post.save()
        return render(request, "newpost.html", {'success_message': "Post created successfully"})
    return render(request, "newpost.html", {'form': form})



def editpost(request, slug):
    post_obj = post.objects.get(slug=slug)
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        post_obj.title = request.POST.get('title')
        post_obj.content = request.POST.get('content')
        post_obj.slug = request.POST.get('slug')
        post_obj.img_url = request.POST.get('image_url')
        uploaded_file = request.FILES.get('image')
        
        if uploaded_file:
            post_obj.image = uploaded_file
        elif post_obj.img_url:  # If URL is provided but no file uploaded
            post_obj.image = None  # Clear the uploaded image
            
        post_obj.save()
        return render(request, "editpost.html", {'success_message': "Post updated successfully"})
    
    form = postForm(initial={
    'title': post_obj.title,
    'content': post_obj.content,
    'slug': post_obj.slug,
    'img_url': post_obj.img_url,
    })
    return render(request, "editpost.html", {'form': form})


def deletepost(request, slug):
    post_obj = post.objects.get(slug=slug)
    post_obj.delete()
    return render(request, "deletepost.html", {'success_message': "Post deleted successfully"})


def register(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Hash password before saving
            hashed_password = make_password(password)
            
            # Save user to database
            new_user = User(name=name, email=email, password=hashed_password)
            new_user.save()
            
            success_message = "Registration successful!"
            form = registerForm()  # Clear the form
            return render(request, "register.html", {'form': form, 'success_message': success_message})
        
        return render(request, "register.html", {'form': form})
    return render(request, "register.html", {'form': form})
