from django.contrib import admin

from .models import Animal, Zoo, AnimalCount


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Zoo)
class ZooAdmin(admin.ModelAdmin):
    pass

@admin.register(AnimalCount)
class AnimalCountAdmin(admin.ModelAdmin):
    pass