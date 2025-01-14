saraksts = [5, 78, 2, 38, 6, 91, 3]
print (saraksts)


#______________BUBBLE SORT_______________
# for j in saraksts:
#     for i in range(len(saraksts)-1): #range dabū kārtas nummuru
#         if saraksts[i] > saraksts[i+1]:
#             temp = saraksts[i]
#             saraksts[i] = saraksts[i+1]
#             saraksts[i+1] = temp
#______________BUBBLE SORT_______________


#______________BUBBLE SORT 2.0_______________
for j in range (len(saraksts)-1):
    for i in range(len(saraksts)-1-j): #range dabū kārtas nummuru
        if saraksts[i] > saraksts[i+1]:
            temp = saraksts[i]
            saraksts[i] = saraksts[i+1]
            saraksts[i+1] = temp
#______________BUBBLE SORT 2.0_______________

skaitlis = 23
def meklet(list, num):
    for i in  range (len(list)):
        if num == list[i]:
            print("ir", i)
            return
    print("nav", )

print(saraksts)

meklet(saraksts, 23)
meklet(saraksts, 2)