from django.conf.urls import include, url
from django.contrib import admin
from main_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main_app.urls')),
]
