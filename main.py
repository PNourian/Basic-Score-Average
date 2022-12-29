import os
def roundDef(number):
    return round(number*4)/4
scores = []
check = False
while not check:
    scores.clear()
    checkInput = False
    scoreLen = 0
    while not checkInput:
        scoreLen = input("Tedad nomarate khod to vared konid: ")
        try:
            scoreLen = int(scoreLen)
            checkInput = True
        except:
            print("Lotfan yek adad vared konid!")
    for i in range(scoreLen):
        checkInput = False
        scoreInput = 0
        while not checkInput:
            scoreInput = input("Nomre khod to vared konid: ")
            try:
                scoreInput = int(scoreInput)
                checkInput = True
            except:
                print("Lotfan yek adad vared konid!")
        scores.append(scoreInput)
    print("Nomarat: ", scores)
    inputBool = input("Aia in nomarat dorost hastand? (y/n): ").lower()
    if inputBool == "y":
        check = True
print("Jame nomarat: ", sum(scores))
avg = sum(scores)/len(scores)
print("Float moadel: ", avg)
print("Round moadel: ", roundDef(avg))
if input("Aia mikhahid export begirid? (y/n): ").lower() == "y":
    file = open("export.txt", "w")
    file.write(f"Jame nomarat: {sum(scores)}\nFloat moadel: {avg}\nRound moadel: {roundDef(avg)}")
    file.close()
