even=odd=0

for i in range(1,101):
    if i % 2 == 1:
        even +=i
    else:
        odd +=i

print('홀수 합 :',even)
print('짝수 합 :',odd)