from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Message

# Create your views here.

def index(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': "Username already exists!!"})
        
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': "Email already exists!!"})
        
        elif password != cpassword:
            return JsonResponse({'success': False, 'message': "password and confirm password missed match!!"})
        
        else:
            new_user = User.objects.create(
                first_name=full_name,
                email=email,
                username=username,
                password=password
            )
            
            new_user.save()
            
            return JsonResponse({'success': True, 'message': "Sign Up compeleted successfully.."})
        
    return render(request, "index.html")

def message_m(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        
        if not email or not subject or not message:
            return JsonResponse({'success': False, 'message': "email, subject, message is required!!"})
        
        else:
            new_message = Message.objects.create(
                name=name,
                email=email,
                number=number,
                subject=subject,
                message=message
            )
            
            new_message.save()
            
            return JsonResponse({'success': True, 'message': "Message sent successfully.."})
    return render(request, "index.html")
