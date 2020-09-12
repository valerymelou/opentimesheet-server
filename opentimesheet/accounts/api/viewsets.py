from rest_framework import status
from rest_framework.response import Response

from opentimesheet.core.api.viewsets import BaseModelViewSet

from ..api.serializers import AccountSerializer, CreateAccountSerializer
from ..models import Account


class AccountViewSet(BaseModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    prefetch_for_includes = {"__all__": ["user"]}
    select_for_includes = {"__all__": ["user"]}

    def get_serializer_class(self):
        if self.action == "create":
            return CreateAccountSerializer

        return AccountSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # Delete linked user
        instance.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
