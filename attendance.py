import pywhatkit as pyw         #send whatsapp msg 
import pyttsx3                  # type: ignore #speak absent student name
file=open(r"C:\Users\HP\OneDrive\Documents\CSschool\CSATTENDANCE (3).txt","a+")
import json      #sequence writting of dict
import datetime             #present date
dates=datetime.date.today()
abslist=[]             
numnotavllist=[]
Rollno=0
rec=""
def pnumber(name):
    if name == a:
        return #"+91 "    #enter mobile no. here
    elif name == b:
        return #"+91 "    #enter mobile no. here
    elif name == c:
        return #"+91 "    #enter mobile no. here
    elif name == d:
        return #"+91"    #enter mobile no. here
    elif name == e:
        return #"+91"    #enter mobile no. here
    elif name == f:
        return #"+91"    #enter mobile no. here
    elif name == g:
        return #"+91"    #enter mobile no. here
    elif name == h:
        return #"+91"    #enter mobile no. here
    elif name == q:
        return #"+91"    #enter mobile no. here
print(" class 12th COMPUTER SCIENCE studends attendance ")
file.write(" class 12th COMPUTER SCIENCE studends attendance ")
file.write("\n")
a="Aaditya Gupta        "
b="Krish Vinchurkar     "
c="yash Gupta           "
d="Gaurav Mehra         "
e="Kajal Dubey          "
f="Kashish Chaudhary    "
g="Naman Tiwari         "
h="Sameer Patel         " 
q="Youmit Chaudhry      "       
i=[a,b,c,d,e,f,g,h,q]
print("       NAME                ATTENDANCE")
file.write("       NAME                ATTENDANCE")
file.write("\n")
l={}
n=0
p=0
for k in i:
    Rollno=Rollno+1
    print(k,end=" ")
    file.write(k)
    m=input("is present or absent(present=0,absent=1)= ")
    file.write("is present or absent(present=0,absent=1)= ")
    file.write(m)
    file.write("\n")
    if m == "0":
        l[k]="present"
        n=n+1
        rec="present"
    elif m=="1":
        abslist.append(k)
        l[k]="absent"
        p=p+1
        rec="absent"
    else:
        print("wrong entry found")
        file.write("wrong entry found")
        file.write("\n") 
        rec="None"
    import mysql.connector as myrec
    mycon=myrec.connect(host="localhost",user="root",passwd="654321",database="attendance")
    cursor=mycon.cursor()
    data = "insert into AttenRec(ROLLno,NAME,ATTENDANCE,DATE) values({},'{}','{}','{}')".format(Rollno,k,rec,dates)
    cursor.execute(data)
    mycon.commit()
data = "insert into AttenRec(ROLLno,NAME,ATTENDANCE,DATE) values({},'{}','{}','{}')".format("NULL","NULL","NULL","NULL")
cursor.execute(data)
mycon.commit()
cursor.execute(data)
mycon.commit()
total=n+p
n=str(n)
p=str(p)
print("       NAME                ATTENDANCE")
file.write("       NAME                ATTENDANCE")
file.write("\n")
print(json.dumps(l,indent=3))
file.write(json.dumps(l,indent=3))
file.write("\n")
print("attendance taken by SAURABH NAYAK sir")
file.write("attendance taken by SAURABH NAYAK sir")
file.write("\n")
print("Total number of student = ",total)
file.write("Total number of student = ")
total=str(total)
file.write(total)
file.write("\n")
print("Total number of student that are PRESENT = ",n)
file.write("Total number of student that are PRESENT = ")
file.write(n)
file.write("\n")
print("Total number of student that are ABSENT = ",p)
file.write("Total number of student that are ABSENT = ")
file.write(p)
file.write("\n")
print("attendace taken in this date and time = "
      ,datetime.datetime.now())
file.write("attendace taken in this date and time = ")
date=(datetime.datetime.now())
date=str(date)
file.write(date)
file.write("\n")
file.write("-------------------------------------------------------------------------")
file.write("\n")
file.write("\n")
file.write("\n")
#now program for whatsapp msg
for i in abslist:
    number=pnumber(i)
    ms=str(i)
    gs="is absent today"
    msgs=ms+gs
    if number == None:
        numnotavllist.append(i)
    else:
        pyw.sendwhatmsg_instantly(number,msgs)
for nlist in numnotavllist:
    print(nlist , "number is not available kindly add it.")
file.close()
#made by Aaditya Gupta
mycon.close()
eak = "is absent today."
engine = pyttsx3.init()
engine.say("start")
engine.runAndWait()
for sp in abslist:
    speak = sp+eak
    engine = pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()
# Made by Aaditya Gupta
# Email = aaditya31977@gmail.com


