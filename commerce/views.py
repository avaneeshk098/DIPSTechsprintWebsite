from django.shortcuts import render
from django.core.mail import send_mail
from .models import Item
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import http
# Create your views here.
def item_list(request):
    return render(request, "index1.html") 

def gaming(request):
    return render(request, 'gaming.html')

def decoding(request):
    return render(request, 'decoding.html')

def thinkathon(request):
    return render(request, 'thinkathon.html')

def team(request):
    return render(request, 'team.html')
    
hint = ['HINT 1: This is the first clue;', 'HINT 2: This is the second clue;', 'HINT 3: This is the third clue']
def homemail(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        send_mail("Website Contact Form:  " + name, "You have received a new message from your website contact form.\n\n"+"Here are the details:\n\nName: "+ name +"\n\nEmail: " + email + "\n\nPhone: "+ phone+ "\n\nMessage:\n"+ message, email, ['dps.it.council@gmail.com'], fail_silently=False)
        return HttpResponseRedirect("/home")

def main(request):
    return render('index.html')
def submail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        send_mail("Website Subscription List Added: "+ email, "You need to add a user to the website  subscription list.\n\n" + "Here are the details:\n\nEmail:" + email, email, ['dps.it.council@gmail.com'], fail_silently=False)
        return HttpResponseRedirect('/TechSprint')
        
def TechSprint(request):
    return render(request, 'index2.html')
def index(request):
    response = render(request, 'index.html')
    response.set_cookie("arestedkjkhfdiiens", datetime.datetime.now())
    return response

def hints(request):
    return render(request, 'hints.html')

def challenge(request):
    return render(request, 'challenge.html')

def acknowledge(request):
    return render(request, 'acknowledge.html')

def scoreboard(request):
    return render(request, 'scoreboard.html')

def hints_post(request, id):
    if(request.method == "POST"):
        if(id < 3):
            return HttpResponse(hint[id])
        else:
            return HttpResponse(list(hint))
    else:
        return HttpResponse("Can't access this data.")