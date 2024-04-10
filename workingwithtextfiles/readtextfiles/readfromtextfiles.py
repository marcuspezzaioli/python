
people_who_have_paid = set()
people_who_have_not_paid = set()
setting_people_who_have_not_paid = False

with open (".\\textfilestoread/textfile1.txt", 'r') as file:
    for line in file:
        # Ignore new line escape sequence at end of string, and blank lines
        text = line.rstrip()

        # Do not want to collect this line as a name of a person
        if text == "People Who Have Paid" or text == "":
            continue

        # Update the set we are adding to, then continue loop so do not collect this line as a name.
        if text == "People Who Have Not Paid":
            setting_people_who_have_not_paid = True
            continue

        if setting_people_who_have_not_paid:
            people_who_have_not_paid.add(text)
        else:
            people_who_have_paid.add(text)

# end = "" prevents a default new line being printed
print("People who have paid: ", end="")
counter = 0
for person in people_who_have_paid:
    # For last person don't put a comma after name, and allow new line to be printed
    if counter == len(people_who_have_paid) - 1:
          print(person) 
    else:
        print(person + ", ", end="")
        counter += 1


print("People who have not paid: ", end="")
counter = 0
for person in people_who_have_not_paid:
    if counter == len(people_who_have_not_paid) - 1:
          print(person) 
    else:
        print(person + ", ", end="")
        counter += 1