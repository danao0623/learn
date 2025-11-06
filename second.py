print ("hello world, this is my first python program")

print("圓柱面積為:",3.14*5*10*10)

print("圓柱表面積為:",3.14*10*10*2+3.14*5*10*2)

user1=("王議揚")
user2=("許哲瑋")
print(f"{user1}的父親是:{user2}")   
print("hello",user1,"的父親是:",user2,sep="") #sep=""的意思是讓兩個字串中間不要有空格

a=1
a=[1,2,3,4,5]
print(type(a))  #type()用來查看變數的資料型態


a,b,c =1,2,3
if a<b:
    print("yes")
else:
    print("no")

# pi= 3.14159
# radius=float(input("請輸入圓的半徑:"))
# print("圓的半徑為:",radius,",圓的面積為:",pi*radius*radius)

# top=int(input("請輸入梯形上邊長:"))
# bottom=int(input("請輸入梯形下邊長:"))
# height=int(input("請輸入梯形高度:"))
# area=((top+bottom)*height)/2
# print("梯形面積為:",area)

# heart_rate=1
# day=heart_rate*60*24
# year=(float(day*365.25))
# print("一年心跳次數為:",year,"80歲時會跳:",year*80)

# Celsius=float(input("請輸入攝氏溫度:"))
# Fahrenheit=(Celsius*1.8)+32
# print("華氏溫度為:",Fahrenheit)

# BMI_Weight=float(input("請輸入體重(公斤):"))
# BMI_Height=float(input("請輸入身高(公尺):"))
# BMI=BMI_Weight/(BMI_Height**2)
# print("BMI為:",BMI)

# a =int(input("請輸入一個整數:"))
# b =int(input("請再輸入一個整數:"))
# count=(a**2-b**2)/(a+b)
# print("計算結果為:",count)

# a=int(input("請輸入國文分數:"))
# b=int(input("請輸入英文分數:"))
# c=int(input("請輸入數學分數:"))
# avarage=(a+b+c)/3
# print("平均為:",avarage)