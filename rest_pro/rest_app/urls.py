from django.urls import path
from . import views







urlpatterns = [
    path('', views.index, name='index'),
    path('admhome/', views.admhome, name='admhome'),
    path('cxhome/',views.cxhome,name='cxhome'),
    path('userview/', views.userview, name='userview'),
    path('login/', views.login, name='login'),
    path('add_chef/', views.add_chef, name='add_chef'),
    path('add_food/', views.add_food, name='add_food'),
    path('add_waiter/', views.add_waiter, name='add_waiter'),
    path('signup/', views.signup, name='signup'),
    path('view_chef/',views.view_chef,name='view_chef'),
    path('view_food/',views.view_food,name='view_food'),
    path('cx_food/',views.cx_food,name='cx_food'),
    path('update_chef/<int:id>/',views.update_chef,name='update_chef'),
    path('add_order/<int:id>/',views.add_order,name='add_order'),
    path('view_order/',views.view_order,name='view_order'),
    path('view_foodorder/',views.view_foodorder,name='view_foodorder'),
    path('confirm_order/<int:id>/',views.confirm_order,name='confirm_order'),
    path('rej_order/<int:id>/',views.rej_order,name='rej_order'),


]
