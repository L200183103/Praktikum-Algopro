#Activity 1
d = {'Triangle' : 'L = 0.5 * a *t',
     'Square' : 'L = s ** 2',
     'Rectangle' : 'L = p * l',
     'Circle' : 'L = pi * r ** 2',
     'Paralellogram' : 'L = a * t'}

print '''

No |Nama Bangun     |Rumus Luas     
---|----------------|---------------
1. |Triangle        |%s
2. |Square          |%s
3. |Rectangle       |%s
4. |Circle          |%s
5. |Parallelogram   |%s

'''%(d['Triangle'],
     d['Square'],
     d['Rectangle'],
     d['Circle'],
     d['Paralellogram'])

#Activity 2 Login system
n = 0
while n<3:
    x = input ('Enter your password : ')
    n +=1
    if x=='Welcomeadmin':
        print ('Login Successful!')
        n=3
    if x!='Welcomeadmin':
        if n==3 :
            print ('Sorry, you have tried 3 times. your access is rejected')
        elif x!='Welcomeadmin' :
            print ('Wrong password')
print ('---------------------------------------------------')

#Activity 3 Time Greeting. Created by: Luckyta Afia Susanto
h = ('morning' , 'noon' , 'afternoon' , 'evening' , 'night')
d = input ('enter your name : ')
v = input('what time is it now? ')
v = float (v)
if v>=01.00 and v<=10.00:
    print ('good' , h[0] , d)
elif v>=10.01 and v<=14.59:
    print ('good' , h[1] , d)
elif v>=15.00 and v<=18.00:
    print ('good' , h[2] , d)
elif v>=18.01 and v<=20.59:
    print ('good' , h[3] , d)
elif v>=21.00 and v<=24.59:
    print ('good' , h[4] , d)

print ('hi, ')


