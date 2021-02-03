from random import randint

def genSeg(x):
  while True: # While the generated segment isn't valid
    num = [] # Variable to store the generated digits
    for i in range(1,x+1):
      if i != x:
        n = randint(0,9) # Generate a digit
      else: # If it's the last digit, it must be between 1 and 7
        n = randint(1,7) # Generate a digit
      num.append(n) # Add the digit to the full number

    n = int(''.join(str(e) for e in num)) # make n an int
    if 7%n == 7: #If it's divisible by 7 it's a good segment, therefore return it as a string
      return ''.join(str(e) for e in num)

def genSite():
  site = str(randint(0,999)).zfill(3)  # Make a random three digit number betwen 000 and 999
  for i in range(3,10):
    if site == str(i)*3:  # If it's 333-444-...-999 it's forbidden, therefore make a new one
      site = genSite()
  return site

def genOEM():
  segments = []
  segments.append(str(randint(1,366)).zfill(3) + str(randint(95,103))[-2:3].zfill(2)) # First segment
  segments.append("OEM")                                                       # Second
  segments.append("0" + genSeg(6))                                             # Third
  segments.append(str(randint(0,99999)).zfill(5))                              # Fourth
  return ('-'.join(str(e) for e in segments)) # Fuse them all together

def genCD():
  segments = []
  segments.append(genSite()) # First segment
  segments.append(genSeg(7)) # Second
  return ('-'.join(str(e) for e in segments))  # Fuse them all together

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
