# users/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_student = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_users'  # This assumes you have a pre-existing table named 'tbl_users'

    def __str__(self):
        return self.username

