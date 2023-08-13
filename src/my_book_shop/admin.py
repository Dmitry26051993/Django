from django.contrib import admin

from my_book_shop.models import Book, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Comment)