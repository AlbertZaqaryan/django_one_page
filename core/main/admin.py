from django.contrib import admin
from .models import Category, Welcome, OurWork, OurTeam
# Register your models here.

admin.site.register(Welcome)
admin.site.register(Category)
admin.site.register(OurTeam)
admin.site.register(OurWork)

