#run on python3 not python2
import os
import codecs


def print_output(input):
    input = input.split("\n")
    input = list(filter(None, input))
    print("<html>")
    print("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />")
    print("<body>")
    for i in input:
        line = i + "<br />"
        print(line)
    print("</body>")
    print("</html>")


def fsm(input):
    V1 = u"\u0E40\u0E41\u0E42\u0E43\u0E44"
    C1 = u"\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D\u0E0E\u0E0F" \
         + u"\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F" \
         + u"\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E"
    C2 = u"\u0E23\u0E25\u0E27\u0E19\u0E21"
    V2 = u"\u0E34\u0E35\u0E36\u0E37\u0E38\u0E39\u0E31\u0E47"
    T  = u"\u0E48\u0E49\u0E4A\u0E4B"
    V3 = u"\u0E32\u0E2D\u0E22\u0E27"
    C3 = u"\u0E07\u0E19\u0E21\u0E14\u0E1A\u0E01\u0E22\u0E27"

    state_0 = V1+ C1
    state_1 = C1
    state_2 = C2 + V2 + T + V3 + C3 + V1 + C1
    state_3 = V2 + T + V3 + C3
    state_4 = T + V3 + C3 + V1 + C1
    state_5 = V3 + C3 + V1 + C1
    state_6 = C3 + V1 + C1

    state = 0
    counter = 0
    result = []
    #print("state: " + str(state))
    for each in input:
        if (len(result) != 0 and result[-1] == " "):
            del result[-1]
        result.append("\n")
        state = 0
        for char in each:
            if (char in state_0 and state == 0):
                result.append(char)
                if (char in V1):
                    state = 1
                else:
                    state = 2
            elif (char in state_1 and state == 1):
                result.append(char)
                state = 2
            elif (char in state_2 and state == 2):
                result.append(char)
                if (char in C2):
                    state = 3
                if (char in V2):
                    state = 4
                if (char in T):
                    state = 5
                if (char in V3):
                    state = 6
                if (char in C3):
                    state = 9
                if (char in V1):
                    state = 7
                if (char in C1):
                    state = 8
            elif (char in state_3 and state == 3):
                result.append(char)
                if (char in V2):
                    state = 4
                if (char in T):
                    state = 5
                if (char in V3):
                    state = 6
                if (char in C3):
                    state = 9
            elif (char in state_4 and state == 4):
                result.append(char)
                if (char in T):
                    state = 5
                if (char in V3):
                    state = 6
                if (char in C3):
                    state = 9
                if (char in V1):
                    state = 7
                if (char in C1):
                    state = 8
            elif (char in state_5 and state == 5):
                result.append(char)
                if (char in V3):
                    state = 6
                if (char in C3):
                    state = 9
                if (char in V1):
                    state = 7
                if (char in C1):
                    state = 8
            elif (char in state_6 and state == 6):
                result.append(char)
                if (char in C3):
                    state = 9
                if (char in V1):
                    state = 7
                if (char in C1):
                    state = 8
            elif (state == 7):
                result.insert(-1, " ")
                result.append(char)

                state = 1
            elif (state == 8):
                result.insert(-1, " ")
                result.append(char)
                state = 2
            elif (state == 9):
                result.append(char)
                result.append(" ")
                state = 0

    result = ''.join(result)
    # print_output(result)

def fst():
    folder = "folder"

    content_set = []
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        with codecs.open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()
            content_set.append(content)
    del content_set[0]
    clean_set = []
    for each in content_set:
        each = each.split("\n")
        clean_set += each
    clean_set = list(filter(None, clean_set))
    fsm(clean_set)

fst()
