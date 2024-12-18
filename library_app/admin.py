from django.contrib import admin
from .models import Author, Book


class CustomAuthorAdmin(admin.ModelAdmin):
    fields_to_display = ('full_name', 'bio')
    search_options = ('full_name',)

    def get_list_display(self, request):
        return self.fields_to_display

    def get_search_fields(self, request):
        return self.search_options


class CustomBookAdmin(admin.ModelAdmin):
    display_fields = ('title', 'author', 'year_published', 'genre', 'category', 'publisher_name')
    filter_options = ('year_published', 'genre', 'publisher_name')
    search_criteria = ('title', 'author__full_name', 'genre', 'publisher_name')

    def get_list_display(self, request):
        return self.display_fields

    def get_list_filter(self, request):
        return self.filter_options

    def get_search_fields(self, request):
        return self.search_criteria


admin.site.register(Author, CustomAuthorAdmin)
admin.site.register(Book, CustomBookAdmin)
