from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template import loader
from django.template.loader import render_to_string
from .models import Mail_Subscriber, Comment, products


def index(request):
    return render(request, 'Essential_Glams/index.html')


def login_view(request):
    if request.user.is_authenticated:
        print("Authenticasted")
        return render(request, 'Essential_Glams/index.html')
    else:
        return render(request, 'Essential_Glams/login.html')


def Save_User(request):
    username = request.POST['username']
    password = request.POST['password']
    password_confirm = request.POST['confirm-password']
    if username == '' or password == '' or password_confirm == '':
        return render(request, 'Essential_Glams/register.html', {
            'message': "Please fill out required fields!"
        })
    elif password != password_confirm:
        return render(request, 'Essential_Glams/register.html', {
            'message': "Password must match"
        })
    else:
        try:
            user_to_save = User(username=username, password=password)
            user_to_save.save()
            login(request, user_to_save)
            return render(request, 'Essential_Glams/index.html')
        except IntegrityError as e:
            print(e)
            return render(request, 'Essential_Glams/register.html', {
                'message': "Username is already taken!"
            })


def login_user(request):
    username = request.POST['username']
    password_one = request.POST['password_one']
    user = authenticate(request, username=username, password=password_one)
    if user is not None:
        login(request, user)
        return render(request, 'Essential_Glams/index.html')
    else:
        return render(request, 'Essential_Glams/login.html', {
            'message': 'Incorrect username or password'
        })


def register_view(request):
    return render(request, 'Essential_Glams/register.html')


def logout_view(request):
    logout(request)
    return render(request, 'Essential_Glams/login.html')


def book(request):
    return render(request, 'Essential_Glams/contact.html')


def comment(request):
    return render(request, 'Essential_Glams/faq.html', {
        'Comment': Comment.objects.all()
    })


def success(request):
    return render(request, 'Essential_Glams/Success.html')


def mail():
    html_message = render_to_string(
        'Essential_Glams/Success.html', {'context': 'values'})
    send_mail('Hey', 'Hry Therre', 'olusegunpopoola4real@gmail.com',
              ['sinaayopopoola@gmail.com'], html_message=html_message, fail_silently=False)


def register_mail(request):
    Email = request.POST['Email']
    Email_Capitalized = Email.capitalize()
    try:
        Mail = Mail_Subscriber(Email_Subscribers=Email_Capitalized)
        Mail.save()
        html_message = render_to_string(
            'Essential_Glams/Welcome.html', {'context': 'values'})
        send_mail('Welcome!', 'Essential Glams', 'olusegunpopoola4real@gmail.com',
                  [Email_Capitalized], html_message=html_message, fail_silently=False)
        return render(request, 'Essential_Glams/Success.html')
    except IntegrityError as e:
        print(e)
        return render(request, 'Essential_Glams/Error.html')


def comment_handler(request):
    User = request.POST['User']
    Email = request.POST['Email']
    Comment_made = request.POST['Comment']
    if User == '' or Email == '' or Comment_made == '':
        return render(request, 'Essential_Glams/Contact.html', {
            'message': 'Fill in required fields'})
    else:
        c = Comment(User=User, User_Email=Email, comment=Comment_made)
        c.save()
        return render(request, 'Essential_Glams/comment.html', {
            'Comment': Comment.objects.all()
        })


def product(request):
    if request.method == "GET":
        return render(request, 'Essential_Glams/product.html', {
            'products': products.objects.all()
        })
    else:
        image = request.POST['File']
        p = products(image=image)
        p.save()
        return render(request, 'Essential_Glams/index.html')


def product_video(request):
    return render(request, 'Essential_Glams/product-video.html')
