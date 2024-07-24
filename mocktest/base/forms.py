from django import forms
from . models import Question,Answer

class AddQustion(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__" #to get all feild

