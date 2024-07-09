from django.contrib import admin
from .models import TestPerson, Test, Answer, Group, Theme, NameSprav


@admin.register(TestPerson)
class TestPersonAdmin(admin.ModelAdmin):
    list_display = ('log_test', 'passw_test')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme_name',)


@admin.register(NameSprav)
class NameSpravAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_name_cod')
