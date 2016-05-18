from django.contrib import admin

from .models import Client, Executive, Person


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_receipt_name',
                    'client_receipt_address', 'client_nit')
    search_fields = ['client_name']


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_name', 'person_lastname')
    search_fields = ['person_name', 'person_lastname',]


class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'executive_comssn')
    search_fields = ['person']


admin.site.register(Client, ClientAdmin)
admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(Person, PersonAdmin)
