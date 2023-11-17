from django.urls import path
from .views import home_view, login_page, register_page,log_out, post_view,add_post, single_post, post_edit, post_delete

urlpatterns = [
    path('', home_view, name='home_view'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', log_out, name='logout'),
    path('posts/', post_view, name='posts'),
    path('create-post/', add_post, name='add'),
    path('post/<int:pk>', single_post, name='post'),
    path('edit/<int:pk>', post_edit, name='edit'),
    path('delete/<int:pk>', post_delete, name='delete'),
]