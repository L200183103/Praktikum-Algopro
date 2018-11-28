def konversiSuhu(C=0,F=0):
    "Program untuk mengubah Celcius ke Fahrenheit dan sebaliknya"
    if F == 0:
        F = (C * 9 / 5) + 32
        print ("Suhu",C,"Celcius setara dengan",F,"Fahrenheit")
    elif C == 0:
        C = (F - 32) * 5 / 9
        print ("Suhu",F,"Fahrenheit setara dengan",C,"Celcius")
