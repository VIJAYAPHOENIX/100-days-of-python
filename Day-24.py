# # Today class is about "How to open,Read,Write in files using the keyword".
#
# pathway can be used as "../" . It used to jump one level ahead in pathway.
# # to create a new text file
# with open("name.txt",mode="w") as demo:
#
#     demo.write("is it working")

PLACEHOLDER = "[name]"

with open("./name.txt") as names_file:
    names = names_file.readline()

with open("./invitation.txt") as letter_file:
    letter_content = letter_file.read()
    print(letter_content)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        print(new_letter)