from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='account'
urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
  #  path('tymtable', views.tymtable, name='tymtable'),
    path('^delete/<int:pk>/',views.delete,name='delete'),
    path('tutorial',views.tutorial,name='tutorial'),
    url(r'^update/<int:pk>/',views.update,name='update'),


]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)