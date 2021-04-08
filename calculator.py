from urllib.request import urlopen as urlReader

def get_input():
    raw_input = input('Enter a command in the format \"operator x y\" where x and y are integers') 
    return (raw_input[0], raw_input[2], raw_input[4])

def cutIntFromLine(line, splitChar):
    x = 0
    if(line[1] == splitChar):
        x = line[0]
    elif(line[2] == splitChar):
        x = line[0:1]
    elif(line[3] == splitChar):
        x = line[0:2]
    return x


def getTupleFromLine(line):
    for i in range (0, (len(line)-1)):
        print("char " + str(i) + " = " + str(line[i]))
    line = line[5:] #remove "calc"
    op = line[0]
    line = line[1:]
    x = cutIntFromLine(line, " ")
    y = line[:-3]

    #y = cutIntFromLine(line, "\\")
    print("x= " + str(x) + " op=" + str(op) + " y=" + str(y))     
    



def getLinesFromFile():
    target_url = "https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt"
    data = urlReader(target_url)
    for line in data:
        print(line)
        getTupleFromLine(line)

def calculate(operator, x, y):
    x = int(x)
    y = int(y)
    if (operator == "+"):
        return (x + y)
    elif (operator == "/"):
        return (x / y)
    elif (operator == "-"):
        return (x - y)
    elif (operator == "*"):
        return (x * y)
    else:
        return "unrecognised operator"


#(op, x, y) = get_input()
#print(calculate(op, x, y))

getLinesFromFile()