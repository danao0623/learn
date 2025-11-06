# score=int(input("請輸入你的分數:"))
# if score>=90:
#      print("A")
# elif score>=80:
#      print("B")
# elif score>=70:
#      print("C")
# elif score>=60:
#      print("D")
# else:
#      print("E")

# a =list(map(int,input("請輸入3個數字:").split()))        #map(int())就是()裡的所有數字都轉換為int，#再用split()把輸入的數字分開
# if (a[0]+a[1]>a[2]) and (a[0]+a[2]>a[1]) and (a[1]+a[2]>a[0]):
#     print("可以形成三角形")
#     if (a[0]==a[1]) and (a[1]==a[2]):
#         print("正三角形")
#     elif (a[0]==a[1]) or (a[1]==a[2]) or (a[0]==a[2]):
#         print("等腰三角形")
# else:
#     print("不可以形成三角形")
# print("你輸入的數字是:",a)

# score_list=list(map(int,input("請輸入分數:").split()))
# score_grade=["A","B","C","D","E"]
# score_level = [90, 80, 70, 60, 0]
# for score in score_list:
#     for i in range(5):
#         if score>=score_level[i]:
#             print("你的分數是:",score,"等級是:",score_grade[i])
#             break

# Group =list(input("請輸入你的身高體重值:").split(','))
# BMI_level = [30, 24,17.5 ]
# BMI_grade = ["肥胖","過重" ,"正常"]
# for group in Group:
#     height,weight=map(float,group.split())
#     BMI=weight/((height/100)**2)
#     for i in range(3):
#         if BMI>=BMI_level[i]:
#             print("你的身高體重值為:",group,"BMI為:",round(BMI,2),"等級是:",BMI_grade[i])
#             break
#     else:
#         print("你的身高體重值為:",group,"BMI為:",round(BMI,2),"等級是:過輕")

# game_point =list(input("請輸入玩家姓名與分數(用空白分隔，每組用逗號):").split(','))
# point_level= (90,80,70,60)
# point_grade= ("S","A","B","C")
# for gameplayer in game_point:
#     name,point=gameplayer.split()
#     point=int(point)
#     for i in range(4):
#         if point>=point_level[i]:
#             print("玩家:",name,"分數為:",point,"等級是:",point_grade[i])
#             break
#     else:
#         print("玩家:",name,"分數為:",point,"等級是:D")

# for i in range(100,10,-3):
#      print (i)

# i=0
# while i<=100:
#     i=i+1
#     if i%13!=0:
#         continue
#     print(i)

# for i in range(1,5):
#     for j in range(1,5):
#         if i*j<8:
#             continue
#         print(i*j)

# money=25000
# month=0
# while money<50000:
#     money=money+(money*0.03)
#     month=month+1

# print("你需要",month,"月才能翻倍")

# i=0
# for i in range(0,5):
#     i=i+1
#     print("*"*i) 

# num=0
# for i in range(0,101):
#     num+= i
# print(num)

# num=0
# for i in range(1,21):
#     i=i+1  
#     if i%13==0:
#         continue
#     if i%17==0:
#         break
#     print(i)

# i=0
# j=0
# sum=0
# for i in range(1,10):
#     for j in range(1,10):
#         sum = i * j
#         print(i,"x",j,"=",sum,end="\t")
#   print()

# start=int(input("請輸入一個起始金額:"))
# rate=float(input("請輸入月利率(百分比):"))/100
# j=0
# money=start
# while money < 2*start:
#     money=money+(money*rate)
#     j=j+1
# print("你需要",j,"月才能翻倍","你的金額為:",money)
