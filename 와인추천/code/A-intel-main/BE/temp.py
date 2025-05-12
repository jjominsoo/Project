import json
with open("BE/userinfo.json","r") as json_file:
    info = json.load(json_file)

newinfo = info[1:-1].split(",")
print(newinfo[0])

templist = []
for i in range(len(newinfo)):
    templist.append(int(newinfo[i]))


userinfo = [4,0,1,1,1]
print(templist)
print(userinfo)
usertemp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp = 0
for num in templist:
    if(temp == 0):
        usertemp[num] = 1
        temp += 1
    elif(temp == 1):
        usertemp[5+num] = 1
        temp += 1
    elif(temp == 2):
        usertemp[12] = num
        if(num == 0):
            temp += 1
            # red 질문
        else:
            temp += 3
            # white 질문
    elif(temp == 3):
    # red
        usertemp[13] = num
        temp += 1
    elif(temp == 4):
    # red 2
        usertemp[14] = num
    elif(temp == 5):
    # white
        usertemp[13] = num
        if(num == 0):
            temp += 1
        else:
            temp += 2
    elif(temp == 6):
    # white 2
        if(num == 2):
            usertemp[15] = 1
            usertemp[16] = 1
        else:
            usertemp[16-num] = 1         
    elif(temp == 7):
        usertemp[17] = num


print(usertemp)