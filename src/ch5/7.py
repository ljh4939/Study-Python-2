import sys
num =[8,7,3,2,9,4,1,6,5]
max = -sys.maxsize - 1
min = sys.maxsize

for value in num:
   if value > max:
     max = value
   if value < min:
     min = value

print('최댓값 :',max)
print('최솟값 :',min)