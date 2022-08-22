from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils.crypto import salted_hmac


class User(models.Model):
    first_name = models.CharField("first name", max_length=128)
    last_name = models.CharField("last name", max_length=128)
    email = models.EmailField(verbose_name="email", unique=True)
    password = models.CharField("password", max_length=128)
    last_login = models.DateTimeField("last login", blank=True, null=True)
    is_active = True

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    _password = None

    class Meta:
        db_table = "user"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(
            key_salt,
            self.password,
            algorithm="sha256",
        ).hexdigest()


class BarberShop(models.Model):
    """Model of open and working barbershops"""

    address = models.TextField(verbose_name="address", max_length=500)
    photo = models.ImageField(
        verbose_name="barber shop photo", upload_to="addresses/%Y/%m/%d/"
    )

    def __str__(self):
        return self.address
