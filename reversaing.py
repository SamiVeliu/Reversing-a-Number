'''
Sami Veliu
Reversing a Number
'''






number = int(input('enter a 4 digit number'))
'''
Must be an integer
'''

N1 = (number-(number%10))/10
#
N2 = (N1 - (N1%10))/10
'''
This is setting Number 2 = Number1 (123) minus 12.3 / 10 
Thus Number 2 = 12
'''

N3 = (N2 - (N2%10))/10
#

print(number%10,int(N1%10),int(N2%10),int(N3%10))

