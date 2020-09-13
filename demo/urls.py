"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls',namespace='account')),
    #path('/account/',include('account.urls')),
    #path('/login/',include('account.urls')),
    #path('/register/', include('account.urls')),
    #path('/logout/', include('account.urls')),
    #path('/contact/',include('account.urls')),
    #path('about/', include('account.urls')),
    #path('tymtable/', include('account.urls')),
    #path('tutorial/', include('account.urls')),
    #path('delete/', include('account.urls')),
    #path('tutorial', include('account.urls')),
    #path('^update/', include('account.urls')),
    path('account/',include('django.contrib.auth.urls')),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='account/login.html'))
]