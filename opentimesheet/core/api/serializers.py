from rest_framework_json_api import serializers

from opentimesheet.users.api.serializers import UserSerializer


class BaseModelSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer()
    modified_by = UserSerializer()

    class JSONAPIMeta:
        included_resources = ("user", "created_by", "modified_by")

    def update(self, instance, validated_data):
        request = self.context.get("request")
        instance.modified_by = request.user
        return super(BaseModelSerializer, self).update(instance, validated_data)
