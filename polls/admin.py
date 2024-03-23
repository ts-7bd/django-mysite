from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    #list_display = ["choice_text", "votes"]
    model = Choice
    extra = 5  

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "pk", "votes"]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Datum", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
