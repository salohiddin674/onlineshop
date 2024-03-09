from django.urls import path
from .views import *

urlpatterns = [
    path('singin/',signin_view,),
    path('sin_up/',signup_view ),
    path('logout/',logout_view),
    path('edit_user/<int:pk>/',edit_user_view),
]