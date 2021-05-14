import mysql.connector
from django.shortcuts import render
user=""
psswd=""
name=""

mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="bbm")
def login(request):
    return render(request,"miniproject.html")

def log(request):
    global user,psswd,cursor
    cursor=mydb.cursor()
    name=request.GET["name"]
    age = int(request.GET["age"])
    phno = int(request.GET["phno"])
    user = request.GET["username"]
    psswd = request.GET["psw"]
    print(name,age,phno,user,psswd)
    cursor.execute(f"insert into si values('{name}',{age},{phno},'{user}','{psswd}')")
    cursor.execute("commit")
    return render(request,"miniproject.html")

def si(request):
    return render(request,"si.html")
def home(request):
    return render(request, "home.html")


def home1(request):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="bbm")
    cursor=mydb.cursor()
    user=request.GET["username"]
    psswd=request.GET["password"]
    try:
        query=f"select * from si where username='{user}' and pwd='{psswd}'"
        cursor.execute(query)
        str=cursor.fetchall()
        print(str)
        if str[0][3]==user and str[0][4]==psswd:
            return render(request,"home.html")
        else:
            return render(request,"miniproject.html")
    except Exception as e:
        return render(request,"miniproject.html")

def dgbg(request):
    return render(request,"dgbg.html")

def home2(request):
    return render(request,"home2.html")

def srap(request):
    cursor=mydb.cursor()
    cursor.execute("select * from dgap")
    str=cursor.fetchall()
    return render(request,"srap.html", {'str':str})

def dgap(request):
    return render(request,"dgap.html")


def drs(request):
    cursor=mydb.cursor()
    name=request.GET["name"]
    gender = request.GET["gender"]
    address = request.GET["address"]
    age = int(request.GET["age"])
    phno = int(request.GET["phno"])
    city = request.GET["city"]
    bloodgroup = request.GET["bloodgroup"]
    print(name,gender,address,age,phno,city,bloodgroup)
    cursor.execute(f"insert into dgap values('{name}','{gender}','{address}',{age},{phno},'{city}','{bloodgroup}')")
    cursor.execute("commit")
    return render(request,"drs.html")
def hospital(request):
    return render(request,"hospital.html")
def bloodstock(request):
    return render(request,"bloodstock.html")
def us(request):
    cursor = mydb.cursor()
    hid = request.GET["hid"]
    hname = request.GET["hname"]
    address = request.GET["address"]
    city = request.GET["city"]
    phno = int(request.GET["phno"])
    cursor.execute(f"insert into hospital values('{hid}','{hname}','{address}','{city}',{phno})")
    cursor.execute("commit")
    return render(request,"us.html")

def bus(request):
    cursor = mydb.cursor()
    hname = request.GET["hname"]
    bloodgroup = request.GET["bloodgroup"]
    availibility = request.GET["availibility"]
    cursor.execute(f"insert into bloodstock values('{hname}','{bloodgroup}','{availibility}')")
    cursor.execute("commit")
    return render(request,"bus.html")

def bloodgroup(request):
    bg=request.GET["bloodgroup"]
    cursor=mydb.cursor()
    cursor.execute(f"select * from dgap where bloodgroup='{bg}'")
    str=cursor.fetchall()
    return render(request, "srap.html", {'str': str})
def login1(request):
    return render(request,"miniproject.html")


