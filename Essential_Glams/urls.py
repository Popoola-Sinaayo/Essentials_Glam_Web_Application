from django.urls import path

from . import views


urlpatterns = [
    path('', views.login_view, name="login"),
    path('index', views.index, name="index"),
    path('Save-User', views.Save_User, name="Save_User"),
    path('login', views.login_user, name="User_login"),
    path('register', views.register_view, name="register_view"),
    path('logout', views.logout_view, name="logout"),
    path('book', views.book, name="book"),
    path('comment', views.comment, name="comment"),
    path('success', views.success, name='success'),
    path('register_mail', views.register_mail, name="register_mail"),
    path('comment-handler', views.comment_handler, name="comment_handler"),
    path('product-video', views.product_video, name="video"),
    path('test', views.test, name="test"),
    path('confirm', views.confirm, name="confirm"),
    path('login_in', views.login_in, name="login_in"),
    path('product', views.product, name="product")
]
