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


if 'Secret santa folder' not in os.listdir():
    os.chdir(r'C:\Users\Niki\Documents\python\secretSanta\Secret santa folder')
    
shuffle(participants)
for i in range(len(participants)):
    for j in range(i+1, len(participants)):
        with open(participants[i]+".txt", 'w') as writer:
            writer.write( participants[j])
        break
    if i+1 == len(participants):
        with open(participants[i]+".txt", 'w') as writer:
            writer.write(participants[0])
        

