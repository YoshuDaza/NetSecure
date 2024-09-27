from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contactanos(request):
    return render(request, 'contactanos.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Captura los datos del formulario
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Envía el correo
            full_message = f"De: {first_name} {second_name} <{email}>\n\nMensaje:\n{message}"
            send_mail(subject, full_message, 'yobandazag2003@gmail.com', ['yobandazag2003@gmail.com'])

            # Mensaje de éxito
            messages.success(request, 'Tu mensaje ha sido enviado exitosamente.')
            return redirect('contact')  # Cambia según tu URL de contacto

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})