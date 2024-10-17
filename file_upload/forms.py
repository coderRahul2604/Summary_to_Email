from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    email = forms.EmailField(label="Recipient Email", required=True)
