
a,b,c,d=input('네 수를 입력해주세요 ').split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
sel1=(a+b+c+d)/4
sel2=((a-sel1)**2+(b-sel1)**2+(c-sel1)**2+(d-sel1)**2)/4
print('평균:',sel1)
print('분산:',sel2)
