import os
from random import shuffle

# used for the input of names in the "participants" list
personInput=None
participants = []

print("to exit input 0")
while personInput != 0:
    personInput = input("input name:")
    if personInput=="0":
        break
    participants.append(personInput)

#checks if the folder that contains the files exists, if not, it creates it
if 'Secret santa folder' not in os.listdir():
    os.chdir(r'C:\Users\Niki\Documents\python\secretSanta\Secret santa folder')
    
# shuffles the list of names
shuffle(participants)

#creates files, with the name of the participants, containing the name of the perseon that will receave a gift from the person
for i in range(len(participants)):
    for j in range(i+1, len(participants)):
        with open(participants[i]+".txt", 'w') as writer:
            writer.write( participants[j])
        break
    # for the last person in the list
    if i+1 == len(participants):
        with open(participants[i]+".txt", 'w') as writer:
            writer.write(participants[0])
        

