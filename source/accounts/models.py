from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    pass

    def __str__(self):
        return (f"name of the user :  {self.username}")
