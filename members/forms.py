from django import forms
from .models import Member


class NewMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Member
        fields = "__all__"
        labels = {
            'name': '名字',
            'height': '身高',
            'weight': '體重',
        }
