from django.contrib import admin
from django.urls import path
from blog import views #here
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('new_post/', views.new_post, name='new_post'),
    path("sending_gmail/ ",views.sending_gmail,name="sending_gmail"),
    path('post_details/<slug:slug>', views.post_details, name='post_details'),
    path('delete_blog_post/<slug:slug>/', views.delete_post,name='delete_blog_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

