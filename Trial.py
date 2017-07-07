def split(origlist):
    mid = len(origlist)/2
    templist = []
    templist.append(orig[:mid])
    templist.append(orig[mid:])

    while(checkIfReadyForMerge(templist)):
        templist2 = []
        for x in range(0, len(templist)):
            if len(templist[x]) >1:
                mid = len(templist[x]) / 2
                templist2.append(templist[x][:mid])
                templist2.append(templist[x][mid:])
            else:
                templist2.append(templist[x])
        templist = templist2

    return templist


def checkIfReadyForMerge(list):
    for x in range(0, len(list)):
        if len(list[x]) > 1:
            return True
    return False

def merge(list):
    listcopy = list

    while len(listcopy) > 1:
        semifinal = []
        total = len(listcopy) / 2

        for x in range(0, total):
            templist2 = []
            i=0
            j=0
            curr = x*2

            while i < len(listcopy[curr]) and j < len(listcopy[curr+1]):
                if listcopy[curr+1][j] > listcopy[curr][i]:
                    templist2.append(listcopy[curr][i])
                    i=i+1


                else:
                    templist2.append(listcopy[curr+1][j])
                    j=j+1



            while i < len(listcopy[curr]):
                templist2.append(listcopy[curr][i])
                i = i+1

            while j < len(listcopy[curr+1]):
                templist2.append(listcopy[curr+1][j])
                j = j + 1

            semifinal.append(templist2)

        if len(listcopy)%2 == 1:
            semifinal.append(listcopy[-1])



        print(" final final semifinal", semifinal)
        listcopy = semifinal






orig = [54,26,93,17,77, 100000, 31,44,55,20, -1]

# alist = []
#
# in1 = "go"
#
# while in1 != str('end'):
#     in1 = raw_input('enter number: ')
#     if in1 != str('end'):
#         alist.append(in1)
#         print("finput: ",  alist)
#     else:
#         print("end")

semi = split(orig)
print('semi ', semi)
merge(semi)
#print(orig)