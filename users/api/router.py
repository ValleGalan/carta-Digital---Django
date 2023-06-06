from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter() #llamarlo desde el proyecto icard urls.py

router_user.register(
    prefix = 'users', basename ='users', viewset= UserApiViewSet
)

urlpatterns =[
    path('auth/me/', UserView.as_view() )
]