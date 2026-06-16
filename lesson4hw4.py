b="101101111"
i_b=""
for x in b:
 i_b+="1"if x=="0"else"0"
c=1
r=""
for x in i_b[::-1]:
 if x=="1"and c==1:
  r="0"+r
 else:
  if c==1:
   r="1"+r
   c=0
  else:
   r=x+r
print(r)