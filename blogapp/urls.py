from django.urls import path
from . import views


urlpatterns = [
    path('user-register',views.register,name = 'user'),
    path('user-contact',views.contact,name = 'contact'),
    path('user-blog', views.blog,name = 'blog'),
    path('user-about',views.about,name = 'about'),
    path('',views.signup, name='signup'),
    path('login',views._login, name='login'),
    path('postlist',views.PostList.as_view(),name = 'postlist'),
    path('PostDetail',views.PostDetail.as_view(),name = 'postdetail'),
    
]