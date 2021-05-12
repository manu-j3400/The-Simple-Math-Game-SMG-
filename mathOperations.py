from mathPowerUps import mathPower
import mathDict as math
import time
import os

def clear():
        os.system('clear')

def mathFunctions():
#1__________________________________________________________________________

    q1 = input(math.mathContents["questions"]["q1"])

    if q1 == "4":
        print(math.mathContents["responses"]["r1"])
        #mathPower.Correct += 1
        #print(mathPower.Correct)
        time.sleep(2)
        print("______________________________\n")
        q2 = input(math.mathContents["questions"]["q2"])
    elif q1 != "4":
        print(math.mathContents["answers"]["a1"])
        print("______________________________\n")
        time.sleep(2)
        q2 = input(math.mathContents["questions"]["q2"])
    elif q1 != str:
        print(math.mathContents["responses"]["r2"])
#2__________________________________________________________________________

    if q2 == "42":
        print(math.mathContents["responses"]["r1.2"])
        time.sleep(2)
        print("______________________________\n")
        q3 = input(math.mathContents["questions"]["q3"])
    elif q2 != "42":
        print(math.mathContents["answers"]["a2"])
        print("______________________________\n")
        time.sleep(2)
        q3 = input(math.mathContents["questions"]["q3"])
    elif q2 != str:
        print(math.mathContents["responses"]["r2"])
#3__________________________________________________________________________

    if q3 == "5":
        print(math.mathContents["responses"]["r1.3"])
        time.sleep(2)
        print("______________________________\n")
        q4 = input(math.mathContents["questions"]["q4"])
    elif q3 != "5":
        print(math.mathContents["answers"]["a3"])
        print("______________________________\n")
        time.sleep(2)
        q4 = input(math.mathContents["questions"]["q4"])
    elif q3 != str:
        print(math.mathContents["responses"]["r2"])
#4__________________________________________________________________________

    if q4 == "2":
        print(math.mathContents["responses"]["r1.4"])
        time.sleep(2)
        print("______________________________\n")
        q5 = input(math.mathContents["questions"]["q5"])
    elif q4 != "2":
        print(math.mathContents["answers"]["a4"])
        print("______________________________\n")
        time.sleep(2)
        q5 = input(math.mathContents["questions"]["q5"])
    elif q4 != str:
        print(math.mathContents["responses"]["r2"])


#5__________________________________________________________________________

    if q5 == "81":
        print(math.mathContents["responses"]["r1.5"])
        time.sleep(2)
        print("______________________________\n")
        q6 = input(math.mathContents["questions"]["q6"])
    elif q5 != "81":
        print(math.mathContents["answers"]["a5"])
        print("______________________________\n")
        time.sleep(2)
        q6 = input(math.mathContents["questions"]["q6"])
    elif q5 != str:
        print(math.mathContents["responses"]["r2"])
#6__________________________________________________________________________

    if q6 == "81":
        print(math.mathContents["responses"]["r1.6"])
        time.sleep(2)
        print("______________________________\n")
        q7 = input(math.mathContents["questions"]["q7"])
    elif q6 != "81":
        print(math.mathContents["answers"]["a6"])
        print("______________________________\n")
        time.sleep(2)
        q7 = input(math.mathContents["questions"]["q7"])
    elif q6 != str:
        print(math.mathContents["responses"]["r2"])
#7__________________________________________________________________________

    if q7 == "54":
        print(math.mathContents["responses"]["r1.7"])
        time.sleep(2)
        print("______________________________\n")
        q8 = input(math.mathContents["questions"]["q8"])
    elif q7 != "54":
        print(math.mathContents["answers"]["a7"])
        print("______________________________\n")
        time.sleep(2)
        q8 = input(math.mathContents["questions"]["q8"])
    elif q7 != str:
        print(math.mathContents["responses"]["r2"])
#8__________________________________________________________________________

    if q8 == "a2 + b2 = c2":
        print(math.mathContents["responses"]["r1.8"])
        time.sleep(2)
        print("______________________________\n")
        q9 = input(math.mathContents["questions"]["q9"])
    elif q8 != "a2 + b2 = c2":
        print(math.mathContents["answers"]["a8"])
        print("______________________________\n")
        time.sleep(2)
        q9 = input(math.mathContents["questions"]["q9"])
    elif q7 != str:
        print(math.mathContents["responses"]["r2"])
#9__________________________________________________________________________

    if q9 == "2":
        print(math.mathContents["responses"]["r1.9"])
        time.sleep(2)
        print("______________________________\n")
        q10 = input(math.mathContents["questions"]["BreakTime | q10"])
    elif q9 != "2":
        print(math.mathContents["answers"]["a8"])
        print("______________________________\n")
        time.sleep(2)
        q10 = input(math.mathContents["questions"]["BreakTime | q10"])
    elif q9 != str:
        print(math.mathContents["responses"]["r2"])
#10__________________________________________________________________________

    if q10 == "begin":
        print("10...")
        time.sleep(1)
        print("9...")
        time.sleep(1)
        print("8...")
        time.sleep(1)
        print("7...")
        time.sleep(1)
        print("6...")
        time.sleep(1)
        print("5...")
        time.sleep(1)
        print("4...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("______________________________\n")
        time.sleep(0.5)
        q10and11 = input(math.mathContents["questions"]["q10and11"])
#11__________________________________________________________________________

        if q10and11 == "25":
                print(math.mathContents["responses"]["r1.11"])
                clear()
                print("______________________________\n")
                time.sleep(2)
                print(math.mathContents["finalAnswerResponse"]["done"])
        elif q10and11 != "25":
                print(math.mathContents["answers"]["a11"])