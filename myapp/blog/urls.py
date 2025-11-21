from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name='index'),
    path("blog/post/<str:slug>", views.detail, name='detail'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path("newpost",views.newpost, name="newpost"),
    path("editpost/<str:slug>", views.editpost, name="editpost"),
    path("deletepost/<str:slug>", views.deletepost, name="deletepost"),
    path("register", views.register, name="register"),
]
