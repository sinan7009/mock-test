import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _



class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True  # to register this as base class to inherit


class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = "base_category"
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("category_name",)

    def __str__(self):
        return self.category_name


class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category',
                                 on_delete=models.CASCADE)  # CASCADE option means that when a Category instance is deleted, all related objects that reference that instance via this foreign key will also be deleted.
    question = models.CharField(max_length=100)


    class Meta:
        db_table = "base_question"
        verbose_name = _("question")
        verbose_name_plural = _("questions")
        ordering = ("question",)

    def __str__(self):
        return self.question


class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "base_answer"
        verbose_name = _("answer")
        verbose_name_plural = _("answers")
        ordering = ("answer",)

    def __str__(self):
        return str(self.question)


class User(models.Model):
    username = models.CharField( max_length=100)

    class Meta:
        db_table = "base_user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("username",)

    def __str__(self):
        return str(self.username)


class UserModule(models.Model):
    user = models.ForeignKey(User, related_name='user_module', on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)

    class Meta:
        db_table = "base_UserModule"
        verbose_name = _("UserModule")
        verbose_name_plural = _("UserModules")
        ordering = ("module_name",)

    def __str__(self):
        return str(self.module_name)


class UserResult(models.Model):
    module = models.ForeignKey(UserModule, related_name='module_result', on_delete=models.CASCADE)
    qstn = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    total_mark = models.IntegerField(default=0)

    class Meta:
        db_table = "base_UserResult"
        verbose_name = _("UserResult")
        verbose_name_plural = _("UserResults")
        ordering = ("total_mark",)

    def __str__(self):
        return str(self.module)
