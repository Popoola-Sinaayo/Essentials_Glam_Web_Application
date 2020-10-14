from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('book', views.book, name="book"),
    path('comment', views.comment, name="comment"),
    path('success', views.success, name='success'),
    path('register_mail', views.register_mail, name="register_mail"),
    path('comment-handler', views.comment_handler, name="comment_handler"),
    path('product-video', views.product_video, name="video"),
    path('confirm', views.confirm, name="confirm"),
    path('product', views.product, name="product")
]
