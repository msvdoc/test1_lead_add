from django import forms

class LeadAddForm(forms.Form):
    fio_client = forms.CharField(label="Ф.И.О.", help_text="Введи Ф.И.О.", max_length=200)
    phone_client = forms.CharField(label="Телефон", help_text="Введи телефон", max_length=200)
    address_client = forms.CharField(label="Адрес", help_text="Введи адрес", max_length=200)