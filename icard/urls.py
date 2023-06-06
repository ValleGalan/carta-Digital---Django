"""
URL configuration for icard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Documentacion de rest api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#modelo importados
from users.api.router import router_user


#funcion de rest api
schema_view = get_schema_view(
   openapi.Info(
      title="CartaDigital APIDOC",
      default_version='v1',
      description="Documentacion de la api Carta Digital",
      terms_of_service="https://...",
      contact=openapi.Contact(email="vallegalan810@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls), #user:florencia_galan contraseña:123
    #DOCMENTACION DE REST API
    #path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #vistas
    path('api/', include('users.api.router')),

    path('api/', include(router_user.urls))
    


]
