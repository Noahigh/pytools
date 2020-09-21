def ask(*arg):
 try:
  a=input(arg[0])
 except IndexError:
  a=input()
 b=a.find(' ')
 d=[]
 if b==-1:
  return a
 while b==-1:
  b=a.find(' ')
  c=''
  if a[b-2:b-1]==' ':
   return 'error \' \' is carry was \' \''
  else:
   while True:
    try:
     c=c+a[b-2:b-1]
     b=b-1
    except IndexError:
     break
  d.append(c)
 return d
