from django.contrib import admin
from .models import UserAbs
from django.contrib.auth.admin import UserAdmin

class UserAbsAdmin(UserAdmin):
    list_display  = ('username', 'email', 'password', 'telefone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + ((None , {'fields' : ('telefone','biografia','idade','endereco','escolaridade', 'animais')}))
    add_fieldsets = UserAdmin.add_fieldsets + ((None , {'fields' : ('telefone','biografia','idade','endereco','escolaridade', 'animais')}))

admin.site.register(UserAbs)

# Register your models here.
