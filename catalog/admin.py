from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)

class BookInline(admin.TabularInline):
    model = Book
    

# REgister the admin class for Author using decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'display_genre', 'language')
    list_filter = ('author','language')
    inlines = [BooksInstanceInline]


#admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','status', 'due_back')
    list_filter = ('status', 'due_back','language')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id', 'language')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )




admin.site.register(Genre)
admin.site.register(Language)