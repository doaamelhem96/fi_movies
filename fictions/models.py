from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
class Fiction(models.Model):
    title=models.CharField(max_length=255,help_text="insert the title of a movie")
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('movie_list')