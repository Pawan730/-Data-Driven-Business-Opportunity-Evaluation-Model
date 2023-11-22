from django.db.models import Avg, Max
from django.shortcuts import render, redirect


# Create your views here.
from admins.markovchain import opportunity_process
from admins.models import BusinessDetails
from . import markovchain


def login(request):
    print("hilogin")
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                print("success")
                data = BusinessDetails.objects.values('field').annotate(s1=Avg('investment'), s2=Avg('returnamount'),
                                                                        s3=Avg('profit'), s4=Avg('loss'))
                return render(request, 'admins/viewdata.html', {'objects': data})
    return render(request,'admins/login.html')
def adminpage(request):
    ans = BusinessDetails.objects.values('field').annotate(s1=Avg('investment'), s2=Avg('returnamount'),s3=Avg('profit'),s4=Avg('loss'))
    return render(request,'admins/adminpage.html',{'objects':ans,'chart_type':"bar"})

def viewdata(request):
    print("hiviewdata")
    data = BusinessDetails.objects.values('field').annotate(s1=Avg('investment'), s2=Avg('returnamount'),s3=Avg('profit'),s4=Avg('loss') )
    return render(request,'admins/viewdata.html',{'objects':data})

def maximun_value(request):
    markovchain = opportunity_process
    ans = BusinessDetails.objects.values('field').annotate(s1=Avg('investment')).order_by('-s1')
    ans1 = BusinessDetails.objects.values('field').annotate(s2=Avg('returnamount')).order_by('-s2')
    ans2 = BusinessDetails.objects.values('field').annotate(s3=Avg('profit')).order_by('-s3')
    ans3 = BusinessDetails.objects.values('field').annotate(s4=Avg('loss')).order_by('-s4')


    return render(request,'admins/maximumvalue.html',{'objects':ans,'objects1':ans1,'objects2':ans2,'objects3':ans3,'objects4':markovchain})

def returnamount(request):
    data = BusinessDetails.objects.values('field').annotate(s1=Avg('investment'), s2=Avg('returnamount'),
                                                            s3=Avg('profit'), s4=Avg('loss'))

    return render(request,'admins/returnamount.html',{'gg':data,'chart_type':"line"})


def profit(request):
    ans = BusinessDetails.objects.values('field').annotate(s1=Avg('investment'), s2=Avg('returnamount'), s3=Avg('profit'), s4=Avg('loss'))
    return render(request,'admins/profit.html',{'gg':ans,'chart_type':"line"})

def loss(request):
    ans = BusinessDetails.objects.values('field').annotate(s1=Avg('investment'), s2=Avg('returnamount'),s3=Avg('profit'),s4=Avg('loss'))
    return render(request,'admins/loss.html',{'gg':ans,'chart_type':"bar"})

def viewuserdetails(request):
    return render(request,'admins/viewuserdetails.html')

def logout(request):
    return redirect('login')

