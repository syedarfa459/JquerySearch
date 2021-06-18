
from django.urls import path
from . import views
app_name='locapp'
urlpatterns = [
    path('', views.index),
    path('searchsuggestion/', views.search, name='search'),
]

