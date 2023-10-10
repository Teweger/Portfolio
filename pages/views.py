import os
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def home(request):
    return render(request, "pages/home.html",{})

def download_pdf(request, *args, **kwargs):
    # Get the filename from the URL parameters
    filename = kwargs.get('p')

    # Define the path to the PDF file
    file_path = os.path.join('static', 'pdfs', filename)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404("PDF file not found")