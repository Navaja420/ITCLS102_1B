name = input("Enter your name -- >")
print(f"---Anime List Maker, {name}---")

anime_list = []
while True:
    anime = input("Emter the name of a Anime (type 'exit' to stop): ")
    if anime.lower() == 'exit':
        break
    anime_list.append(anime)
    print(f"'{anime}' has been added to the list. Continue,")
else:
    print("Error!")

print(f"\nanime List ofc {name.upper()}:")
for i in range(1, len(anime_list)+ 1):
    print(f" {i} - {anime_list[i - 1]}")

print("\nThank You for Trying the Anime List Maker!!")
