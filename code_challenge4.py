print("Welcome to the anime Recommender!")
print("Answer a few question to find your next anime to watch.")
genre_want = str(input("What genre you want to read? (action, romance, horror)"))
if genre_want == "action":
    genre = "action"
    print("your prefer genre is:", genre)
    how_long = str(input("How long should the anime be? (short, medium, long)"))
    if how_long == "short":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: Bleach!!")
        elif decade == 2010:
            print("We recommend: Redu of the healer!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "medium":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: Naruto!!")
        elif decade == 2010:
            print("We recommend: Shield Hero!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "long":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: One Piece!!")
        elif decade == 2010:
            print("We recommend: Demon Slayer!!")
        else:
            print("maybe there's something wrong?")
    else:
        print("maybe there's something wrong")

if genre_want == "romance":
    genre = "romance"
    print("your prefer genre is:", genre)
    how_long = str(input("How long should the anime be? (short, medium, long)"))
    if how_long == "short":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
                print("We recommend: Silent Voice!!")
        elif decade == 2010:
            print("We recommend: I Want to Eat Your Pancreas!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "medium":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: His and Her Circumstances!!")
        elif decade == 2010:
            print("We recommend: Golden TIme!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "long":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: Kimi ni Todoke!!")
        elif decade == 2010:
            print("We recommend: Kaguya-sama: Love is War!!")
        else:
            print("maybe there's something wrong?")
    else:
        print("maybe there's something wrong")

if genre_want == "horror":
    genre = "horror"
    print("your prefer genre is:", genre)
    how_long = str(input("How long should the anime be? (short, medium, long)"))
    if how_long == "short":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: Vampire Hunter!!")
        elif decade == 2010:
            print("We recommend: Tokyo Ghoul!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "medium":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: Ghost Stories!!")
        elif decade == 2010:
            print("We recommend: Parasite The Maxim!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "long":
        decade = int(input("Which year do you want to watch? (2000s, 2010s)"))
        if decade == 2000:
            print("We recommend: Paranoia Agent!!")
        elif decade == 2010:
            print("We recommend: Attack on Titan!!")
        else:
            print("maybe there's something wrong?")
    else:
        print("maybe there's something wrong")
else:
    print("You type something wrong")
