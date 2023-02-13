from django.contrib import admin
from .models import AboutMe, ServiceDescription, Service, Category, Gallery, Contact


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type',)
    search_fields = ('service_type',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'image', 'category')
    list_filter = ('title', 'publication_date', 'image', 'category')
    search_fields = ('title', 'publication_date', 'image', 'category')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'facebook', 'fixly')


admin.site.register(AboutMe)
admin.site.register(ServiceDescription)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Contact, ContactAdmin)
