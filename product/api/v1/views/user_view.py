from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from api.v1.serializers.user_serializer import CustomUserSerializer, BalanceSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "head", "options"]
    permission_classes = (permissions.IsAdminUser,)


class BalancesViewset(viewsets.ModelViewSet):
    """Баланс и Бонусы."""

    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = (permissions.IsAdminUser,)
    http_method_names = ["get", "head", "options", "patch"]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BalanceSerializer
        return ChangeBalanceSerializer