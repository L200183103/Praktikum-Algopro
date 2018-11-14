Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Luckyta Afia Susanto'
>>> NIM = 'L200183103'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Name)
>>> type (a)
<class 'int'>
>>> ##because the variable of 'X' is a string that has been coverted into an integer using a variable int()
>>> type (b)
<class 'int'>
>>> ##because the variable 'b' calculate all of the number in the 'Name' variable members and including in the type of integer
>>> a / b
55.15
>>> ##because the variable 'a' is 1103 devided by the variable 'b' is 20, so that 1103 devided 20 is equal to 55.15 
>>> a // b
55
>>> ##because the variable 'a' divide the variable 'b', then the result changed from float(decimal number) into integer, so 55.15 is rounded 55
>>> 10 * (a-999)
1040
>>> ##because the variable 'a' is 1103, and reduced by 999 so the result is 104, then multiplied by 10 with the result are 1040 
>>> b ** 2
400
>>> ##because the variable 'b' power of 2, so that 20 power of 2 is 400
>>> a % b
3
>>> ##because % function to count the divide remainder after dividing the variable of a and b
>>> c = 12.5
>>> ##variable 'c' is rated 12.5
>>> type (c)
<class 'float'>
>>> ##because 12.5 is including the decimal number, so that named class 'float'
>>> a / c
88.24
>>> ##because the variable 'a' is 1103 divide the variable 'c' is 12.5, so that 1103 divided 12.5 is equal to 88.24
>>> a // c
88.0
>>> ##because the result from the variable 'a' divide the variable 'b' changed from float (decimal number) to integer, so 88.24 is rounded 88
>>> a % c
3.0
>>> ##because % function to count the divide remainder after dividing the variable of 'a' and 'c'
>>> c > b
False
>>> ##because the variable 'c' is '12.5' and variable 'b' is 20 so statement 'c' is greater than 'b' is False
>>> type (c > b)
<class 'bool'>
>>> ##because 'c' > 'b' is a comparison that determines the result is True or False, so including class 'bool'
>>> a > b and b > c
True
>>> ##because the variable 'a' is 1103, variable 'b' is 20 and the variable 'c' is 12.5 than the statement 'a' is greater than 'b' is greater than 'c'. So that the result is True
>>> a > 1100 or b < 10
True
>>> ##because the variable 'a' is 1103 which is greater than 1103, so the statement 'a' > 1103 is True while the variable 'b' is 20 which is greater than 10 so the statement 'b' < 10 is False
