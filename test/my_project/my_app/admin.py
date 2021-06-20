from django.contrib import admin
from .models.cars import Cars
from .models.tokens import Tokens

# Register your models here.

admin.site.register(Cars)
admin.site.register(Tokens)