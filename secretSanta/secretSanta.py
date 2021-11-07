import os
from random import shuffle

personInput=None
participants = []

print("to exit input 0")
while personInput != 0:
    personInput = input("input name:")
    if personInput=="0":
        break
    participants.append(personInput)
    
shuffle(participants)
for i in range(len(participants)):
    for j in range(i+1, len(participants)):
        #print("{} -> {}".format(participants[i], participants[j]))
        with open(participants[i]+".txt", 'w') as writer:
            writer.write( participants[j])
        break
    if i+1 == len(participants):
        with open(participants[i]+".txt", 'w') as writer:
            writer.write(participants[0])
        #print("{} -> {}".format(participants[len(participants)-1], participants[0]))
        

# for i in participants:
#     with open(str(i)+".txt", 'w') as reader:
#         choose = random.choice(participants2)
#         if choose != str(i):
#             reader.write(choose)
#             # participants2.remove(choose)

