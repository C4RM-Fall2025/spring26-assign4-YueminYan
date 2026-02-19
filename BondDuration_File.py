
def getBondDuration(y,face,couponRate,m,ppy):
  sumpvcf=0
  duration=0
  sumW=0
  cf=face*couponRate/ppy
  if ppy==1:
    for i in range(1,m+1):
      pvf=(1+y)**-i
      if i==m:
        cf=cf+face
      sumpvcf=sumpvcf+pvf*cf
      sumW=sumW+i*pvf*cf
    duration=sumW/sumpvcf

  if ppy!=1:
    t=m*ppy
    cf=face*couponRate/ppy
    for j in range(1,t+1):
      pvf=(1+y)**-j
      if j==m*ppy:
        cf=cf+face
      sumpvcf=sumpvcf+pvf*cf
      sumW=sumW+j*pvf*cf
    duration=sumW/sumpvcf

  return duration


