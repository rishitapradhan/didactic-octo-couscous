def calculateAnswer():
  sh=3
  st="hello world"
  letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  ans=""
  for i in st:
    if (i.upper() in letters):
      x=letters.index(i.upper())
      if(sh<=x):
        ans=ans+letters[x-sh]
      else:
        ans=ans+letters[len(letters)-sh+x]
    if(i==" "):
      ans=ans+i
  return ans
print(calculateAnswer())