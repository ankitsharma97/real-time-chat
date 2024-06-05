from django.urls import path,include
from .views import index
urlpatterns = [
    path('<str:grp_name>/', index)
]
