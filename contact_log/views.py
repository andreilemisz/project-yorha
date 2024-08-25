from django.shortcuts import get_object_or_404, render
from contact_log.models import Contact

def contact_log_startingpage(request):
    
    contacts = Contact.objects.all().order_by("id")[:10]
    context = {
        "contacts" : contacts,
    }
    
    return render(request, 'contact_log/homepage.html', context)

def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id
    )

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact_log/single_contact.html',
        context
    )
# Create your views here.
