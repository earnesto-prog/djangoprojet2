from django import forms


class TodolistForm(forms.Form):
    text = forms.CharField(max_length=45, widget = forms.TextInput(
        attrs={'id': 'list_item', 'type': 'text', 'class': 'validate', 'placeholder': 'Enter item here'}
    ))