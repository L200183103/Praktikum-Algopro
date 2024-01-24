Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Luckyta Afia Susanto'
>>> NIM = 103
>>> High = -
>>> Weight = -
>>> YearOfBirth = -
>>> I = (YearOfBirth, Weight, High, NIM, Name)
>>> Data = [YearOfBirth, Weight, High, NIM, Name]
>>> type (I)
<class 'tuple'>
>>> ##because the variable 'I' is a string data that has a row of objects with different data type so it's including class 'tuple' but cannot be changed.
>>> I[0]
2000
>>> ##because the index 0 from the variable 'I' refer to 2000
>>> a = NIM % 4; I[a]
103
>>> ##because the variable 'a' is remaining results from the variable 'NIM' is 103 divided by 4 with the remaining results is 3, then the program will print the value of variable 'I' on the index to the variable 'a', which means the 2nd, that is 103
>>> type (I[a])
<class 'int'>
>>> ##because I[a] is 103, where this is including class 'integer'
>>> I[a:4]
(103,)
>>> ##because the variable 'I' starting from 2nd index that is 103 until to the limit of the 3rd index which is 0 
>>> type (I[4])
<class 'str'>
>>> ##because I[4] is the data type of the value of variable 'I' in the 4th index which is refers to Name, and including class 'str' or string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
NameError: name 'Aku' is not defined
>>> ##I[0] = 'ok' cannot be executed because variable 'I' including class 'tuple'. And tuple is a type that cannot be changed (immutable)
>>> type (Data)
<class 'list'>
>>> ##because the variable 'Data' is a string data that has a row object with different data types but class'list' can be changed
>>> type (Data[4])
<class 'str'>
>>> ##because Data[4] is the data of the value variable 'Data' in the 4th index that is 'Name', so that including class 'str' or string 
>>> Data [4][5]
't'
>>> ##because Data[4][5] is the 5th index value in the variabe 'Data' at the 4th index, which is 't'
>>> Data [4][a:6]
'kyt'
>>> ##because Data [4][a:6] is the value from index to 'a' (which means 2nd index) until to the limit 5th index in the variable 'Data' at the 4th index which is refers to 'kyt' 
>>> Data[0] = 'ok'; Data
['ok', 0, 0, 103, 'Luckyta Afia Susanto']
>>> ##because to change index 0 of the list of 'Data' that is 'YearOfBirth' into 'ok'
>>> Data[-a]
1.6
>>> ##because Data[-a] gives an output the variable'Data' on 2nd index but counts from right that is 103
>>> range (a)
range(0, 3)
>>> ##because giving output the range from start (0) until 'a' (3)
