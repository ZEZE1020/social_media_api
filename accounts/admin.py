from django.contrib import admin
from django.contrib import admin
from .models import CustomUser, Follow

# Register the CustomUser model
admin.site.register(CustomUser)

# Register the Follow model
admin.site.register(Follow)
