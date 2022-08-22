from django.contrib.auth import get_user_model
from rest_framework import serializers
from employers import models

UserModel = get_user_model()


class EmployeeCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email", "password"]

    def create(self, validated_data):
        user = UserModel(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        employee = models.Employee.objects.create(user=user)
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = models.Employee
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "photo",
            "rating",
            "barbershop",
        ]

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_last_name(self, instance):
        return instance.user.last_name

    def get_email(self, instance):
        return instance.user.email
