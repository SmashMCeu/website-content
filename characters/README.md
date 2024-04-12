# IMPORTANT

## How to add characters?
**Important:** the first 5 enties in the list will be displayed on the website as preview characters!

1.
    Open the characters.json and add following for your character:
    ```ts
    {
        ...
        "characterName": "characterName.json",
        ...
    }
    ```
    Keep in mind that characterName should always be **lowercase**!

2.
    Now create the `characterName.json` in the same directroy and add following information into it:
    ```ts
    {
        "name": string,
        "isPro": boolean,
        "skinImage": string, // name of the skin image in skins. E.g mario.png
        "isSlimSkin": boolean,
        "primaryColor": string, // Hex code
        "difficulty": 1 | 2 | 3, // 1 Easy - 2 Medium - 3 Hard
        "cooldownTime": string,
    }
    ```
3.
    Finally put your skin image into the skins directory. The name of your image has to be the exact one you used in characterName.json for "skinImage"
