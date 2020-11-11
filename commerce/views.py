from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Item
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime, time
import http
import random, base64
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('commerce\cred.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Scoreboard').sheet1
# Create your views here.
def index(request):
    return render(request, "index1.html") 

random.seed(time.process_time())

def generate():
    passes = ["DPS{1tz_R3D}", "DPS{Wh1T3_SuS}", "DPS{P1nk_V3nTed}", "DPS{1Tz_Gr3eN}", "DPS{Blu3_SuS}", "DPS{y3LL0W}", "DPS{N0T_BlaCk}", "DPS{Br0Wn_V3nTed}", "DPS{CyAN_SUs}", "DPS{0RanG3}"]
    count = 1
    for i in range(0,10):
        count = random.randint(0,9)
    secret = passes[count] 
    indent = 1
    word = list(secret)
    random.shuffle(word)
    code="secret = input('Enter the secret key: ')\ntry:\n"
    for i in word:
            indents = "  " * indent
            code += indents + f"if secret[{secret.index(i)}] == '{i}':"
            code+='\n'
            indent += 1
    code+="  " * indent
    code+="print('Nice you got the password now just go to https://itcouncil.herokuapp.com/techsprint/treasurehunt_challenge/challenge and give the password. We will announce the results 30 mins after the event ends')\nexcept IndexError:\n \tprint('Password is too small')"
    return base64.b32encode(code.encode('ascii')).decode('ascii')

def gaming(request):
    return render(request, 'gaming.html')

def decoding(request):
    return render(request, 'decoding.html')

def thinkathon(request):
    return render(request, 'thinkathon.html')

def team(request):
    return render(request, 'team.html')

hint2 = ['What is DTMF???', 'Just google "Online DTMF decoder" and upload your audio file.', 'http://dialabc.com/sound/detect/index.html', ' There are many base encodings not just base64', 'Base32 encoding? What is that', 'You can decode it from this website: https://emn178.github.io/online-tools/base32_decode.html']
hint1 = ['Did you know you could hide stuff inside images?', 'You can hide files inside images!', 'You can extract the image (open it with any extracting software like WinRAR or 7Zip)', 'There is a text file hidden with the name "error.txt" in the image.', 'Have you ever heard of base64.', 'You can decode base64 here https://www.base64decode.org/']
passes = ["DPS{1tz_R3D}", "DPS{Wh1T3_SuS}", "DPS{P1nk_V3nTed}", "DPS{1Tz_Gr3eN}", "DPS{Blu3_SuS}", "DPS{y3LL0W}", "DPS{N0T_BlaCk}", "DPS{Br0Wn_V3nTed}", "DPS{CyAN_SUs}", "DPS{0RanG3}"]

def register(request):
    response = render(request, 'register.html')
    if request.method == "POST":
        response.set_cookie("team_name", request.POST.get("name"))
        response.set_cookie("password", request.POST.get("pass"))
        response.set_cookie('team_id', len(sheet.get_all_records())+1)
        sheet.insert_row([request.POST.get("name"), '', '', '', '', ''], len(sheet.get_all_records())+1)
    return response

def image(request):
    return render(request, 'image.html')

def image_hints(request):
    if request.method == 'POST':
        hints_to_send = []
        if datetime.time(10,15,00) < datetime.datetime.now().time():
            hints_to_send.append(hint1[0])
        if datetime.time(10,22,00) < datetime.datetime.now().time():
            hints_to_send.append(hint1[1])
        if datetime.time(10,27,00) < datetime.datetime.now().time():
            hints_to_send.append(hint1[2])
        if datetime.time(10,32,00) < datetime.datetime.now().time():
            hints_to_send.append(hint1[3])
        if datetime.time(10,42,00) < datetime.datetime.now().time():
            hints_to_send.append(hint1[4])
        if datetime.time(10,47,00) < datetime.datetime.now().time():
            hints_to_send.append(hint1[5])
        return JsonResponse({'hints' : hints_to_send })
    else:
        return HttpResponse("Can't access this data.")

def homemail(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        send_mail("Website Contact Form:  " + name, "You have received a new message from your website contact form.\n\n"+"Here are the details:\n\nName: "+ name +"\n\nEmail: " + email + "\n\nPhone: "+ phone+ "\n\nMessage:\n"+ message, email, ['dps.it.council@gmail.com'], fail_silently=False)
        return HttpResponseRedirect("/")

def submail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        send_mail("Website Subscription List Added: "+ email, "You need to add a user to the website  subscription list.\n\n" + "Here are the details:\n\nEmail:" + email, email, ['dps.it.council@gmail.com'], fail_silently=False)
        return HttpResponseRedirect('/techsprint')
        
def index_redir(request):
    return HttpResponseRedirect('/techsprint/treasurehunt_challenge/home')
def techsprint(request):
    return render(request, 'index2.html')

def verify1(request):
    if request.method == 'POST':
        code = int(request.POST.get('code'))
        for i in range(0, 10):
            code1 = generate()
        result = None
        if code == 287996:
            result = JsonResponse({'answer': True, 'code': code1})
        else:
            result = JsonResponse({'answer': False, 'code': code1})
        return result

def verify2(request):
    if request.method == 'POST':
        para = request.POST.get('para')
        result = None
        if para in passes:
            result = JsonResponse({'answer': True})
        else:
            result = JsonResponse({'answer': False})
        return result

def decoding_index(request):
    #if (datetime.date(2020, 11,13) - datetime.date.today()).days <= 0:
    response = render(request, 'index.html')
        #response.set_cookie("arestedkjkhfdiiens", datetime.datetime.now())
    #else:
        #response = HttpResponse('This page is not accessible at the momment.')
    return response

def hints(request):
    #if (datetime.date(2020, 11,13) - datetime.date.today()).days < 0:
    response = render(request, 'hints.html')
    #else:
        #response = HttpResponse('This page is not accessible at the momment.')
    return response

def challenge(request):
    #if (datetime.date(2020, 11,13) - datetime.date.today()).days < 0:
    response = render(request, 'challenge.html')
    #else:
        #response = HttpResponse('This page is not accessible at the momment.')
    return response

def acknowledge(request):
    #if (datetime.date(2020, 11,13) - datetime.date.today()).days < 0:
    response = render(request, 'acknowledge.html')
    #else:
        #response = HttpResponse('This page is not accessible at the momment.')
    return response

def scoreboard(request):
    #if (datetime.date(2020, 11,13) - datetime.date.today()).days < 0:
    response = render(request, 'scoreboard.html')
    #else:
        #response = HttpResponse('This page is not accessible at the momment.')
    return response

def hints_post(request):
    if(request.method == "POST"):
        hints_to_send = []
        if datetime.time(11,2,00) < datetime.datetime.now().time():
            hints_to_send.append(hint2[0])
        if datetime.time(11,12,00) < datetime.datetime.now().time():
            hints_to_send.append(hint2[1])
        if datetime.time(11,17,00) < datetime.datetime.now().time():
            hints_to_send.append(hint2[2])
        if datetime.time(11,24,00) < datetime.datetime.now().time():
            hints_to_send.append(hint2[3])
        if datetime.time(11,34,00) < datetime.datetime.now().time():
            hints_to_send.append(hint2[4])
        if datetime.time(11,41,00) < datetime.datetime.now().time():
            hints_to_send.append(hint2[5])
        return JsonResponse({'hints':hints_to_send})
    else:
        return HttpResponse("Can't access this data.")