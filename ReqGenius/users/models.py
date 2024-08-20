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

class SupportTicket(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"
    

class EducationalContent(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.title
    

from django.db import models

class ZoomMeeting(models.Model):
    url = models.URLField(max_length=500)
    
    def __str__(self):
        return self.url



