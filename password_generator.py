import random
alpha_Upper="QWERTYUIOPLKJHGFDSAZXCVBNM"
alpha_Lower="qwertyuiopasdfghjklzxcvbnm"
digit="1234567890"
symbol="!@#$%^&*()_-+/*?><:;}{[]"

pas=alpha_Upper+alpha_Lower+digit+symbol

length=int(input("enter password size:"))

password="".join(random.sample(pas,length))

print("the generated password is:" + password)