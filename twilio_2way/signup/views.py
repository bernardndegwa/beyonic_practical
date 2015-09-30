from django.shortcuts import render, redirect
from django.http import HttpResponse

from signup.models import PhoneEmail

def home_page(request):
    if request.method == 'POST':
        PhoneEmail.objects.create(text=request.POST['phoneemail_text'])
        return redirect('/')
        
    phoneemails = PhoneEmail.objects.all()
    return render(request, 'home.html', {'phoneemails': phoneemails})
