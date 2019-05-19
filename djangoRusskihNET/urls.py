"""djangoRusskihNET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from stories_app import views
from django.conf.urls.static import static # These two is used to show pictures
from django.conf import settings # These two is used to show pictures

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name = 'home'),
    path('stories/', views.stories, name = 'stories'),
    path('news/', views.news, name = 'news'),
    re_path (r'story/(?P<story_id>[0-9]+)/$', views.story_detailes, name = "storyDetail"),
    path('contacts/', views.contacts, name = 'contacts'),
    path('services/', views.services, name = 'services'),
    path('test/', views.test, name = 'test'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This is will add MEDIA_URL and MEDIA root for any contant in the folder and attach that to a URL specified in settings
