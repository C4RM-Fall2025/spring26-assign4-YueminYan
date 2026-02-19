

def getBondPrice_Z(face, couponRate, times, yc):
  sumpvcf=0
  cf=face*couponRate
  for t, y in zip(times,yc):
    pvf=(1+y)**-t
    if t==times[-1]:
      cf=cf+face
    sumpvcf=sumpvcf+cf*pvf
  return sumpvcf
