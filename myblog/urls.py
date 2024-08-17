from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',homepage,name='home'),
    path('blog/<int:id>',views.blog_detail,name='detail'),
]


