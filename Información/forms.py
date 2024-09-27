from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label="Nombre")
    second_name = forms.CharField(max_length=50, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    subject = forms.CharField(max_length=100, required=True, label="Asunto")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Mensaje")