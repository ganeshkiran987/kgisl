from django.urls import path
from . import views

urlpatterns =[

    path('breeds/',views.loadbreeds),
    path('delete/',views.deletesittinglist),
    path('create/',views.createsittinglist),
]