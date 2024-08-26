from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact_log.models import Contact

def contact_log_startingpage(request):
    
    contacts = Contact.objects.all().order_by("id")
    paginator = Paginator(contacts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj" : page_obj,
        "site_title": "Contacts",
    }
    
    return render(request, 'contact_log/homepage.html', context)

def contact_log_search(request):
    
    search_value = request.GET.get("q", "").strip()
    
    if search_value == "":
        return redirect("contact_log:contact_log_startingpage")
    
    contacts = Contact.objects\
            .filter(
            Q(name__icontains=search_value) |
            Q(rank__name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by("id")
        
    paginator = Paginator(contacts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    context = {
        "page_obj" : page_obj,
        "site_title": "Contacts",
        'search_value': search_value,
    }
    
    return render(request, 'contact_log/homepage.html', context)

def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id
    )

    context = {
        'contact': single_contact,
        "site_title": single_contact.name
    }

    return render(
        request,
        'contact_log/single_contact.html',
        context
    )
# Create your views here.
