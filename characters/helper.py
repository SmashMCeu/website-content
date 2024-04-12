import json

def collect_info():
    data = {}
    file_name = input("File: ")
    data['name'] = input("Name: ")
    data['isPro'] = input("isPro (True/False): ").lower() == 'true'
    data['skinImage'] = file_name + ".png"
    data['primaryColor'] = input("primaryColor: ")
    data['difficulty'] = int(input("difficulty: "))
    data['cooldownTime'] = input("cooldownTime: ")
    data['isSlimSkin'] = input("isSlimSkin: ") == 'true'

    save_to_file(file_name, data)
    return data

def save_to_file(file_name, data):
    with open(file_name + ".json", 'w') as file:
        json.dump(data, file, indent=4)


    characters_file = "characters.json"
    with open(characters_file, 'r') as f:
        characters = json.load(f)

    # Add new entry
    characters[file_name] = file_name + ".json"

    # Save characters data back to file
    with open(characters_file, 'w') as f:
        json.dump(characters, f, indent=4)



    print("Data written to", file_name + ".json")

def main():
    data = collect_info()

    input("[next]")
    main()

if __name__ == "__main__":
    main()