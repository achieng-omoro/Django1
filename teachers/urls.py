from django.urls import path
from . import views
#must not reference an admin
#must also have a default path

urlpatterns = [
   path('',views.home)
]
#home is a function name in the views file