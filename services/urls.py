from django.urls import path
from . import views
#must not reference an admin
#must also have a default path

urlpatterns = [
   path('',views.services)
]
#home is a function name in the views file