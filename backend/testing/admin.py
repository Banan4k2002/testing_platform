from django.contrib import admin
from .models import TestPerson, Test, Answer, Group, Theme, NameSprav


@admin.register(TestPerson)
class TestPersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(NameSprav)
class NameSpravAdmin(admin.ModelAdmin):
    pass
