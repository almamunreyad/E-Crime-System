from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'login.html')


def criminal(request):
    criminalData = Criminal_List.objects.all()
    # for search 
    search = request.GET.get('search')
    
    if search != None:
        criminalData = Criminal_List.objects.filter(criminal_name__icontains = search)
        
    data = {
        'criminalData':criminalData
    }
    
    return render(request, 'criminal.html', data)


def form(request):
    if request.method == 'POST':
        image = request.FILES['image']
        crim_id = request.POST['crim_id']
        name = request.POST['name']
        nation_id = request.POST['nation_id']
        phone = request.POST['phone']
        gender = request.POST['gender']
        date = request.POST['date']
        report = request.POST['report']
        
        user = Form.objects.filter(crim_id = crim_id)
        if user:
            message = "This criminal's information already Exist"
            return render(request, 'form.html', {'msg':message})
        else:
            newUser = Form.objects.create(image = image, crim_id = crim_id, name = name, nation_id = nation_id, phone = phone, gender = gender, date = date, report = report)
            message = "Information Send Successfully"
            return render(request, 'form.html', {'msg':message})
        
        
    return render(request, 'form.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        user = SignUp.objects.filter(email = email)
        if user:
            message = "User Already Exist"
            return render(request, 'signup.html', {'msg':message})
        else:
            newUser = SignUp.objects.create(name = name, email = email, password = password)
            message = "Registration Successfully"
            return render(request, 'login.html', {'msg':message})
        
        
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = SignUp.objects.get(email = email)
        
        if user:
            if user.password == password:
                request.session['email'] = user.email
                
                return render(request, 'home.html')
            else:
                message = "Password or email not match"
                return render(request, 'login.html', {'msg':message})
        else:
            message = "User does not exist"
            return render(request, 'signup.html', {'msg':message})
        
    return render(request, 'login.html')


def logout(request):
    try:
        del  request.session['email']
    except:
        return render(request, 'login.html')
    return render(request, 'login.html')