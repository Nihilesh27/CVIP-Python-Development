import random
alpha_Upper="QWERTYUIOPLKJHGFDSAZXCVBNM"
alpha_Lower="qwertyuiopasdfghjklzxcvbnm"
digit="1234567890"
symbol="!@#$%^&*()_-+/*?><:;}{[]"

password1=alpha_Upper
password2=alpha_Lower
password3=alpha_Lower+alpha_Upper

password4=alpha_Lower+alpha_Upper+digit

password5=alpha_Lower+alpha_Upper+digit+symbol
print("choose type of password")

x=input("[only lower][only upper][only digit][only symbol][both upper and lower][upper lover and digit][upper lower digit and symbol]")

length=int(input("enter password size:"))

if x =="only lower":
    password="".join(random.sample(password2,length))
if x =="only upper":
    password="".join(random.sample(password1,length))
if x =="only digit":
    password="".join(random.sample(digit,length))
if x =="only symbol":
    password="".join(random.sample(symbol,length))
if x =="both upper and lower":
    password="".join(random.sample(password3,length))
if x =="upper lower digit and symbol":
    password="".join(random.sample(password5,length))

print("the generated password is:" + password)
