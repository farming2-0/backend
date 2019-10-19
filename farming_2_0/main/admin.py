# Register your models here.
from django.contrib import admin

from .models import Machine, Crop, Stage, Tip

admin.site.register(Machine)
admin.site.register(Crop)
admin.site.register(Stage)
admin.site.register(Tip)