death=int(input("there are 432542 snipers aming at u so if u dont wanna die enter a number"))
sum=0
temp=death

while temp>0:
    digit= temp%10
    sum += digit**3
    temp//=10

if death==sum:
     print("scinteficlly number is armstrong , not the name of the dude who landed on the moon lady")
else:
      print("scinteficlly number is not armstrong , not the name of the dude who landed on the moon lady")