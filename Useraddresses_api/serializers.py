from rest_framework import serializers
from Useraddresses.models import userAddresses

class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = userAddresses
        fields = "__all__"