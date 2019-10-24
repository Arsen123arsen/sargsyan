from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index),
    path('OrderPermit.aspx/', views.index1),
    path('home.aspx',views.index2),
    path('Login.aspx',views.index3),
    path('SecurityIssue.aspx',views.index4),
    path('ParkingIssue.aspx',views.index5),
    path('MaintenanceIssue.aspx',views.index6),
]

