from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from base.serializers import ResetPasswordSerializer
from employers import servises, serializers


class EmployeeViewSet(ModelViewSet):
    queryset = servises.get_available_employers()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.EmployeeCreateSerializer
        return serializers.EmployeeSerializer

    @action(methods=["POST"], detail=True)
    def set_password(self, request, pk=None):
        employee = self.get_object()
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = employee.user
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response({"status": "password set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
