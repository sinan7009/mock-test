from django.contrib import admin
from . models import Category
from . models import Question
from . models import Answer
from .models import User
from .models import UserModule
from .models import UserResult


#
admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question ,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(UserModule)
admin.site.register(UserResult)


