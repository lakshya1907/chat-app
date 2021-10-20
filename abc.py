from pywebio.input import*
from pywebio.output import*







def exam():
    s = 0
    

    name = input("enter your name")
    input("enter your login id ")
    input("enter your password", type=PASSWORD)
    
    q1 = radio("10+5 is equal to",["15","23","14","234"])
    if q1 == "15":
        s+=1

    q2 = radio("245-45 is equal to",["232","290","200","234",])
    if q2 =="200":
        s+=1

    q3 = radio("34-1 is equal to",["33","20","60","24",])
    if q2 =="33":
        s+=1

    put_text( name, "your score is :", str(s), "/3")
    if s >=2:
        put_text("congratulation!! you passed!!")
    else:
        put_text("you failed, better luck next time.")



exam()


