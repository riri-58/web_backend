from django.contrib import admin
from .models import basket, comment, login, pacage

admin.site.register(login)

admin.site.register(comment),
admin.site.register(basket),
admin.site.register(pacage)
