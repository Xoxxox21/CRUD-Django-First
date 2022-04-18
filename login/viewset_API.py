from login.models import user
from login.serializers import UserSerializer
from rest_framework import viewsets,permissions

class userViewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]