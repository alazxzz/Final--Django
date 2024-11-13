from rest_framework import permissions, status, generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.translation import gettext as _

class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
