from django.db import models


class Projects(models.Model):

    title = models.CharField(default=False, max_length=100)
    image = models.ImageField(default=False, upload_to="images")
    description = models.TextField(default=False)
    link = models.URLField(default=False)
