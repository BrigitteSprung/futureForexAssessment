from django.contrib import admin

# Register your models here.

from .models import *

# ENGAGEMENT HANDOVER
class RelationshipManagerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ['client']
    # raw_id_fields = ('client',)

# ENGAGEMENT HANDOVER
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationshipManager')
    # list_filter = ['client']
    raw_id_fields = ('relationshipManager',)

# ENGAGEMENT HANDOVER
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['client']
    raw_id_fields = ('client','relationshipManager')






admin.site.register(RelationshipManager, RelationshipManagerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Document, DocumentAdmin)