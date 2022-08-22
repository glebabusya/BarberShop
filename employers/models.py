from django.contrib.auth import get_user_model
from django.db import models
from base.models import BarberShop
User = get_user_model()


class Employee(models.Model):
    user = models.OneToOneField(verbose_name="user", to=User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        verbose_name="phone number", max_length=13, blank=True, null=True
    )
    registration_date = models.DateField(
        verbose_name="registration date", auto_now_add=True
    )
    photo = models.ImageField(
        verbose_name="employee photo",
        upload_to="employers/%Y/%m/%d/",
        blank=True,
        null=True,
    )
    rating = models.DecimalField(
        verbose_name="employee rating",
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True,
    )

    is_available = models.BooleanField(verbose_name="", default=True)
    barbershop = models.ForeignKey(
        verbose_name="employee work place",
        to=BarberShop,
        related_name="employers",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "employee"
        ordering = ["-rating", "user"]
