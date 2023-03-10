ss = input ("Enter Score:")

fs = 0.0
try:
   fs = float(ss)
except:
   fs = -1

if(fs == -1):
   print('Input Error')
   quit()

grade = ''

if fs >= 0.9:
   grade = 'A'

elif fs >= 0.8:
   grade = 'B'

elif fs >= 0.7:
   grade = 'C'

elif fs >= 0.6:
   grade = 'D'
else:
   grade = 'F'

print(grade)