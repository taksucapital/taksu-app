from django.urls import path

from front.views.home import Home

urlpatterns = [
    path("", Home.as_view(), name="index"),  
]