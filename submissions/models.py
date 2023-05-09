# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# model for hackathon submissions
class Hackathon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='images/')
    hackathon_image = models.ImageField(upload_to='images/')
    submission_type_choices = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link')
    ]
    submission_type = models.CharField(max_length=20, choices=submission_type_choices)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField()
    reward_prize = models.FloatField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        if not self.submission_type:
            raise ValidationError("Submission type is required")
        submission_types = dict(self.submission_type_choices)
        if self.submission_type not in submission_types:
            raise ValidationError("Invalid submission type")
    
    # def __str__(self):
    #     return f"{self.id}. {self.title} - Created by - {self.created_by}"


# model for hackathon submissions
class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="AnonymousUser")
    name = models.CharField(max_length=200)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='images/submissions/', blank=True, null=True)
    submission_image = models.ImageField(upload_to='images/submissions/', blank=True, null=True)
    submission_link = models.URLField(blank=True, null=True)
    # submitssion_type = models.


class HackathonRegistration(models.Model):
    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['hackathon', 'user']