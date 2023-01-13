from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='uploads/')
    location = models.CharField(max_length=120)
    description = models.TextField()
    people_on_photo = models.TextField()

    def __str__(self):
        return f"{self.user_created} - {self.location}"

