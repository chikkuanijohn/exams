from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm



def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to contact list after saving
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})
# Contact list
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

# Contact detail
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

# Edit contact
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form, 'contact': contact})

# Delete contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_contact.html', {'contact': contact})

# Call page
def call_page(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'call_page.html', {'contact': contact})
