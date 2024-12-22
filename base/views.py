from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'index.html', {'message': 'Thank you for your message!'})
    return render(request, 'index.html')
