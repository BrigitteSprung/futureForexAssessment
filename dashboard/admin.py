from django.contrib import admin
from .models import *

# RELATIONSHIP MANAGER
class RelationshipManagerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ['client']
    # raw_id_fields = ('client',)

# CLIENT
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationshipManager')
    # list_filter = ['client']
    raw_id_fields = ('relationshipManager',)

# DOCUMENT REQUEST
class DocumentRequestAdmin(admin.ModelAdmin):
    list_display = ('client',)
    list_filter = ['client']
    raw_id_fields = ('client','relationshipManager')

# DOCUMENT
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ['client']
    raw_id_fields = ('documentRequest',)






admin.site.register(RelationshipManager, RelationshipManagerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentRequest, DocumentRequestAdmin)