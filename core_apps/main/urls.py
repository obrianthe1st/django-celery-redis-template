"""core URL Configuration
 2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import newView

urlpatterns = [
    path("app1/",newView,name="app1"),

]