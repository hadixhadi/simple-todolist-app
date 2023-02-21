from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('delet/<int:id>',views.delet,name='delet'),
    path('deletall/',views.delet_all)
]