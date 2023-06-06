from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer  #como queremos que nos devuelva lso datos
    queryset = User.objects.all()
    #encriptar el pasword cuando creas un usuario
    def create(self,request,*args,**kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request,*args,**kwargs)
    
    #encriptar el pasword cuando actualizar los datos 
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

# devuelve los datos del usuario
class UserView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)