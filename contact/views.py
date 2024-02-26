from django.shortcuts import render, reverse, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_form(request):
    """ Contact form view """

    template = 'contact/contact.html'
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Form submited.")
            return redirect(reverse("contact_form"))
        else:
            messages.error(request, "Failed to submit the form!")
    
    context = {
        "form": form,
    }
    return render(request, template, context)