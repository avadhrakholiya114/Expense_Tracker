from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('update/<id>', views.update),
    path('delete/<id>', views.delete),

]