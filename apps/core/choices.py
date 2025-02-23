from django.db import models

class GenreChoices(models.TextChoices):
    THRILLER = "thriller"
    COMEDY = "comedy"
    DETECTIVE = "detective"
    FANTASY = "fantasy"