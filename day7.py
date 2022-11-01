tvShow = input("What is your favorite tv show? ")
if tvShow == "rick and morty":
    print("I love that show!")
    faveCharacter = input("Who is your favorite character? ")
    if faveCharacter == "rick":
        print("My favorite rick is pickle rick!")
    elif faveCharacter == "morty":
        print("He's such a crybaby!")
    else:
        print("If you choose anyone besides rick or morty, you're lame!")
elif tvShow == "the simpsons":
    print("That show has been out for decades!")
else:
    print("I don't think I've heard of that one..")
