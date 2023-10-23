from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your message was submitted successfully.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(
                request, f'Message failed! Please ensure the form is valid.')
    form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
