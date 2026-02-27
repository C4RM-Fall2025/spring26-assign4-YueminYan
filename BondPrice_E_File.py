def getBondPrice_E(face,couponRate,m,yc):
  sumpvcf=0
  cf=face*couponRate
  for t, yt in enumerate(yc,start=1):
    pvf=(1+yt)**-t
    if t==m:
      cf=cf+face
    sumpvcf=sumpvcf+cf*pvf
  return round(sumpvcf)
