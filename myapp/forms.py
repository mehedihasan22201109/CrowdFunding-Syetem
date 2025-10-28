from django import forms


from .models import event


class eventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = "__all__"
