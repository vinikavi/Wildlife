from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Admin,User,Booking
from .forms import AdminRegister,Login,TicketBooking,userLogin,UserRegister
from django.core.mail import send_mail
from random import randint

# Create your views here.
def Home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'admin.html')
def userreg(request):
    return render(request,'admin.html')
def UserHome(request):
    return render(request,'userhome.html')

def adminRegister(request):
    form=AdminRegister()
    if request.method=='POST':
        form=AdminRegister(request.POST)
        if form.is_valid():
            # n='KV'
            # for i in range(0,4):
            #     n=n+str(randint(0,9))
            # reg_id=n
            name=form.cleaned_data['name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            mobileno=form.cleaned_data['mobileno']
            k=Admin(username=username,name=name,password=password,email=email,mobileno=mobileno)
            k.save() 
            if not k:
                return HttpResponse("Registration not completed")
            else:
                return redirect("/adminlog")
            # reg_id=request.session['id']=k.reg_id
            # sub="registration success"
            # sender='kavipy2@gmail.com'
            # msg="Hello Mr/Ms."+request.POST['name']+"\n"+"register_id:"+reg_id+"\n"+"\n""Password:"+request.POST['password']+"\n"+"your application submited successfully."+"\n"+"- It is auto genrated yahoo mail."
            # # msg2="Thank you for register"+"\n"+"it is auto generated mail"
            # to=request.POST['email']
            # send_mail(sub,msg,sender,[to]) 
    return render(request,'register.html',{'form':form})
def adminLogin(request):
    form=Login()
    if request.method=='POST':
        form=Login(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name'] 
            request.session['name']=name
            password =form.cleaned_data['password']
            user=Admin.objects.filter(name=name,password=password)
            if not user:
                return HttpResponse("""login failed""")
            else:
                return redirect("/userhome")
    return render(request,'login.html',{'form':form})
def booking(request):
    form=TicketBooking()
    if request.method=='POST':
        form=TicketBooking(request.POST)
        if form.is_valid():
            n=''
            for i in range(0,4):
                n=n+str(randint(0,9))
            reg_id=n
            name=form.cleaned_data['name']
            # password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            age=form.cleaned_data['age']
            parks_names=form.cleaned_data['parks_names']
            # cost=form.cleaned_data['cost']
            # totaltickets=form.cleaned_data['totaltickets']
            child=form.cleaned_data['child']
            c=50*int(child)
            adult=form.cleaned_data['adult']
            a=100*int(adult)
            cost=c+a
            total=int(child)+int(adult)
            print(cost)
            country=form.cleaned_data['country']
            status=form.cleaned_data['status']
            state=form.cleaned_data['state']
            date=form.cleaned_data['date']
            city=form.cleaned_data['city']
            idproof=form.cleaned_data['idproof']
            idno=form.cleaned_data['idno']
            vehicle_no=form.cleaned_data['vehicle_no']  
            # reg_id=form.cleaned_data['reg_id']
            k=Booking(reg_id=reg_id,name=name,email=email,status=status,mobile=mobile,age=age,parks_names=parks_names,cost=cost,total=total,adult=adult,child=child,country=country,state=state,date=date,city=city,idproof=idproof,idno=idno,vehicle_no=vehicle_no)
            k.save()
            reg_id=request.session['id']=k.reg_id
            sub="registration success"
            sender='kavipy2@gmail.com'
            msg="Hello Mr/Ms."+request.POST['name']+"\n"+"register_id:"+reg_id+"\n"+"date:"+request.POST['date']+"\n"+"cost:"+str(cost)+"\n"+"your ticket is booked  successfully."+"\n"+"-It is auto genrated  gmail."
            # msg2="Thank you for register"+"\n"+"it is auto generated mail"
            to=request.POST['email']
            send_mail(sub,msg,sender,[to])
            return render(request,'ticket.html',{'form':form,'status':status,'parks_names':parks_names,'total':total,'ticket_id':k.reg_id,'cost':cost,'adult':adult,'parks_names':parks_names,'child':child,'Date':date})

    return render(request,'booking.html',{'form':form})    
def getdtls(request):
    # if request.method=='POST':
    name1=request.session['name']
    # print(name1)
    dbuser=Booking.objects.filter(name=name1)
    if dbuser:
        return render(request,'display.html',{'name':dbuser})
    else:
        return HttpResponse("previously ur not booking any ..... please Book A Ticket...")

    # dtls=Booking.objects.all()
    # return render(request,'display.html',{'dtls':dtls})
    # return render(request,'display.html')
def alldetails(request):
    all=Booking.objects.all()
    # all.save()
    return render(request,'details.html',{'all':all})