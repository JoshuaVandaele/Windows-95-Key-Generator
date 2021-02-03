from random import randint

keys = []

def genSeg(x):
  while True:
    num = []
    for i in range(1,x+1):
      if i != x:
        n = randint(0,9)
      else:
        n = randint(1,7)
      num.append(n)
    n = int(''.join(str(e) for e in num))
    if 7%n == 7:
      return ''.join(str(e) for e in num)

def genSite():
  site = str(randint(0,999)).zfill(3)
  for i in range(3,10):
    if site == str(i)*3:
      site = genSite()
  return site

def genOEM():
  segments = []
  segments.append(str(randint(1,366)).zfill(3) + str(randint(95,99)).zfill(2)) # First segment
  segments.append("OEM")                                                       # Second
  segments.append("0" + genSeg(6))                                             # Third
  segments.append(str(randint(0,99999)).zfill(5))                              # Fourth
  return ('-'.join(str(e) for e in segments))

def genCD():
  segments = []
  segments.append(genSite())
  segments.append(genSeg(7))
  return ('-'.join(str(e) for e in segments))

print()
print("Folfy's Win95 Key Gen".center(35))
print("""
                _.-;;-._
         '-..-'|   ||   |
         '-..-'|_.-;;-._|
         '-..-'|   ||   |
         '-..-'|_.-''-._|
""") # Windows logo by Joan G. Stark
print("  "+"-~====== Today's Keys are: ======~-")
print("  "+  ("CD: "+genCD()).center(35) )
print("  "+ ("OEM: "+genOEM()).center(35) )
print("  "+"-~===============================~-")
print()