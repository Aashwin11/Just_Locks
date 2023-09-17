from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Signup

# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'index.html')

def lock_keep(request):
    return render(request, 'lock_keep.html')

def in_out(request):
    return render(request, 'in_out.html')

def selectee(request):
    return render(request, 'selectee.html')

def payment(request):
    return render(request, 'payment.html')

def qr_pay(request):
    return render(request, 'qrpay.html')

def success(request):
    return render(request, 'success.html')

def login(request):
    return render(request, 'login.html')

def  signup(request):
    #databse here
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        curr_address = request.POST.get('curr_address')
        sgn = Signup(fname= fname, lname = lname, dob= dob, phone= phone, email= email, curr_address = curr_address)
        sgn.save()
        return render(request, 'login.html')
    return render(request, 'sign_up.html')