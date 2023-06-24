from django.urls import path
from .views import listele
urlpatterns = [
    path('',listele,name="blogliste"), # 127.0.0.1:8000/blog
    # path("ozel/") #127.0.0.1:8000/blog/ozel
]