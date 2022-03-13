from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('show', views.show, name='show'),
    path('add', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('empshow', views.empshow, name='empshow'),
    path('empadd', views.empadd, name='empadd'),
    path('empupdate/<int:id>', views.empupdate, name='empupdate'),
    path('empdelete/<int:id>', views.empdelete, name='empdelete'),
    
]