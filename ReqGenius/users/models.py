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

class SRS(models.Model):
    username = models.CharField(max_length=150, primary_key=True)  # Use CharField for username
    field1 = models.TextField()
    field2 = models.TextField()
    field3 = models.TextField()
    field4 = models.TextField()
    field5 = models.TextField()

    class Meta:
        db_table = 'tbl_srs'  # Ensure this table exists in your database

    def _str_(self):
        return self.username


from django.utils import timezone
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    overall_experience = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    ease_of_use = models.CharField(max_length=20, choices=[
        ('Very Easy', 'Very Easy'),
        ('Easy', 'Easy'),
        ('Neutral', 'Neutral'),
        ('Difficult', 'Difficult'),
        ('Very Difficult', 'Very Difficult')
    ])
    functionality = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor')
    ])
    visual_design = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor')
    ])
    performance = models.CharField(max_length=20, choices=[
        ('Very Fast', 'Very Fast'),
        ('Fast', 'Fast'),
        ('Average', 'Average'),
        ('Slow', 'Slow'),
        ('Very Slow', 'Very Slow')
    ])
    additional_comments = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"Feedback from {self.name} - {self.created_at}"

class SupportRequest(models.Model):
    username = models.CharField(max_length=255, primary_key=True)  # Primary key as text
    email = models.EmailField()
    report = models.TextField()
    file = models.URLField(blank=True, null=True)  # URLField for URLs, allows blank or null

    class Meta:
        db_table = 'tbl_support'  # Specify the table name to match your SQL table

    def _str_(self):
        return self.username
class EducationalContent(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)

    def _str_(self):
        return self.title
    

from django.db import models

class ZoomMeeting(models.Model):
    url = models.URLField(max_length=500)
    
    def _str_(self):
        return self.url
    
class NewTable(models.Model):
    field1 = models.CharField(max_length=100)  # Example text field
    field2 = models.IntegerField()  # Example integer field
    field3 = models.DateField()  # Example date field
    field4 = models.TextField()  # Example text area
    field5 = models.URLField()  # Example URL field

    class Meta:
        db_table = 'tbl_new_table'  # Custom table name

    def __str__(self):
        return f'{self.field1}'