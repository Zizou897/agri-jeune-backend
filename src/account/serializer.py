from rest_framework import serializers
from account.models import  Store
from authentications.models import User


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "phone_number",
            "logo",
            "address",
            "description",
        ]


class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "user",
            "name",
            "phone_number",
            "logo",
            "address",
            "description",
        ]