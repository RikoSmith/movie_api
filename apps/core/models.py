from django.db import models

from apps.core.choices import GenreChoices


class Movie(models.Model):
    title = models.CharField(max_length=1000, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=False)
    genre = models.CharField(choices=GenreChoices.choices, max_length=1000, null=True, blank=True)
    actors = models.ManyToManyField(
        "core.Person", related_name="played_movies", blank=True
    )
    directors = models.ManyToManyField(
        "core.Person", related_name="directed_movies", blank=True
    )


class Person(models.Model):
    first_name = models.CharField(max_length=1000, null=False, blank=False)
    last_name = models.CharField(max_length=1000, null=False, blank=False)
    birth_date = models.DateField(null=False)
