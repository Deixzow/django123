from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)    # 這跟@admin.register()是一樣的操作


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability',{
            'fields':('status', 'due_back', 'borrower')
        }),
    )


from .models import Role, Weapon

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'weapon', 'summ')
    list_filter = ('name', 'weapon')
    search_fields = ('name', )
    ordering = ('id', )


class RoleInline(admin.TabularInline):
    model = Role

@admin.register(Weapon)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill')
    inline = [RoleInline]

