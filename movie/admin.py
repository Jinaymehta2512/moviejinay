from django.contrib import admin
from .models import Movie,Review,Email

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
@admin.register(Email)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'emailid')