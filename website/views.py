from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def about_view(request):
    return render(request, 'coderedcms/pages/about.html')

def courses_view(request):
    return render(request, 'coderedcms/pages/courses.html')

# Contact Form View
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can handle the logic here (email or database)
        messages.success(request, "Your message has been sent!")
        return redirect('contact')
    return render(request, 'coderedcms/pages/contact.html')

# Feedback Form View
def feedback_view(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        # Save to database or send email
        messages.success(request, "Thank you for your feedback!")
        return redirect('feedback')
    return render(request, 'coderedcms/pages/feedback.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'coderedcms/pages/login.html', {'form': form})
