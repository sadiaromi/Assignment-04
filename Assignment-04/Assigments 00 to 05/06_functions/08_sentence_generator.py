def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I just found a {word} in my treasure chest!")
    elif part_of_speech == 1:
        print(f"Whenever I'm happy, I love to {word} all day long!")
    elif part_of_speech == 2:
        print(f"The sunset today looks absolutely {word}!")
    else:
        print("Oops! Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("Enter a noun, verb, or adjective: ")  
    part_of_speech = int(input("What type of word is this? (0 = noun, 1 = verb, 2 = adjective): "))  
    make_sentence(word, part_of_speech)

main()