

def getBondPrice(y,face,couponRate,m,ppy):
  sumpvcf=0
  cf=face*couponRate/ppy
  if ppy==1:
    if i==m:
      cf=cf+face
    for i in range(1,m+1):
      pvf=(1+y)**-i
      sumpvcf=sumpvcf+cf*pvf
  elif ppy!=1:
    t=m*ppy
    for j in range(1,t+1):
      if j==m*ppy:
        cf=cf+face
      for j in range(1,m+1):
        pvf=(1+y)**-j
        sumpvcf=sumpvcf+cf*pvf
  return sumpvcf
