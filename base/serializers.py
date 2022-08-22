from rest_framework import serializers


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        password = data["password"]
        password2 = data["password2"]
        if password == password2:
            return data
        raise serializers.ValidationError("Passwords do not match")
