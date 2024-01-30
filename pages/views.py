from django.shortcuts import render, get_object_or_404

from .models import Page

# Create your views here.
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)

    if(not page.is_active):
        #not find
        
        b = 0

    context = {
        'page': page,
    }
    return render(request, 'pages/page.html', context)