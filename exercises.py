# Write a dice rolling game program
# Write a python program that keeps asking the user if they want to roll the dice,
# It should ask them to choose a yes/no or y/n as answer
# If the user inputs 'yes' or 'y', generate 2 random dice numbers,
# If the user enters another value rather than 'yes' or 'y' or 'no' or 'n',
# tell them 'Invalid choice!' and continue the game
# If the user inputs 'no' or 'n', tell them 'Thanks for playing!', then terminate the game.


# code:

# import random
# while True:
#     user_input = input(
#         "Do you want to roll the dice? (yes/no or y/n):").lower().strip()
#     if user_input == 'yes' or user_input == 'y':
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f"You rolled a {dice1} and a {dice2}.")
#     elif user_input == 'no' or user_input == 'n':
#         print("Thank you for playing!")
#         break
#     else:
#         print("Invalid choice!")


# user_input = input('input anything please:')
# reversed_sentence = user_input.split()[::-1]
# reversed_sentence = ' '.join(reversed_sentence)
# print(f'reversed senetnce is:, {reversed_sentence}')


# # Original text
# text = "I am a boy. I am 29 years old."

# # Split the text into sentences
# sentences = text.split(". ")

# # Reverse the order of sentences
# reversed_sentences = ". ".join(sentences[::-1])

# # Add a period at the end if it was removed
# if not reversed_sentences.endswith("."):
#     reversed_sentences += "."

# print(reversed_sentences)


# clea
import qrcode
data = input('Enter your URL:')
filename = input('Enter your file name:')
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill='black', back_color='white')

image.save(filename)
print(f"QR code saved as {filename}")
