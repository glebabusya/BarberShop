from rest_framework.viewsets import ModelViewSet

from employers import servises, serializers


class EmployeeViewSet(ModelViewSet):
    queryset = servises.get_available_employers()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.EmployeeCreateSerializer
        return serializers.EmployeeSerializer
