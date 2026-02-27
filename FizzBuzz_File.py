def FizzBuzz(start,end):
  outlist=[]
  for i in range(start,end+1):
    if i % 15==0:
      outlist.append("fizzbuzz")
    elif i % 3==0:
      outlist.append("fizz")
    elif i % 5==0:
      outlist.append("buzz")
    else:
      outlist.append(i)

   return outlist

