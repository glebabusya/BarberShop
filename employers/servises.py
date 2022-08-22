from employers import models


def get_available_employers():
    return models.Employee.objects.filter(is_available=True)
