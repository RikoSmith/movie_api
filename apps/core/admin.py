from django.contrib import admin

from apps.core.models import Movie, Person, Country


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class PersonCountry(admin.ModelAdmin):
    pass
