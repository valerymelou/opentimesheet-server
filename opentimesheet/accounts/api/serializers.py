from django.contrib.auth import get_user_model

from opentimesheet.core.api.serializers import BaseModelSerializer
from opentimesheet.users.api.serializers import UserSerializer

from ..models import Account


class AccountSerializer(BaseModelSerializer):
    user = UserSerializer()
    included_serializers = {"user": UserSerializer}

    class Meta:
        model = Account
        fields = (
            "id",
            "first_name",
            "last_name",
            "hire_date",
            "release_date",
            "user",
            "created",
            "created_by",
            "modified",
            "modified_by",
        )

    class JSONAPIMeta:
        included_resources = ("user", "created_by", "modified_by")


class CreateAccountSerializer(BaseModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "hire_date", "release_date", "user")

    class JSONAPIMeta:
        included_resources = ("user",)

    def create(self, validated_data):
        request = self.context.get("request")
        current_user = request.user
        user_data = validated_data.pop("user")
        user = get_user_model()(email=user_data["email"])
        user.set_password(user_data["password"])
        user.save()
        account = Account.objects.create(
            user=user, created_by=current_user, **validated_data
        )
        return account
