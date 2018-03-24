from django.contrib import admin

from .models import Associate


@admin.register(Associate)
class AssociateModelAdmin(admin.ModelAdmin):
    list_display = 'user_email', 'tax_id', 'phone', 'created_at'
    search_fields = 'tax_id',
    date_hierarchy = 'created_at'

    def user_email(self, obj):
        return obj.user.email
