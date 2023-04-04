from django.contrib import admin
# you will need to register any custom models you want to modify and manage via the admin app/page here. 

# Register your models here.
from .models import Place

admin.site.register(Place) # this is how you make the models available to the admin page/app.
