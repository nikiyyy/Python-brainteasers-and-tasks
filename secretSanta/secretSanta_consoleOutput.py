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
   
# shuffles the list of names   
shuffle(participants)

#creates files, with the name of the participants, containing the name of the perseon that will receave a gift from the person
for i in range(len(participants)):
    for j in range(i+1, len(participants)):
        print("{} -> {}".format(participants[i], participants[j]))
        break
    
    # for the last person in the list
    if i+1 == len(participants):
        print("{} -> {}".format(participants[len(participants)-1], participants[0]))


