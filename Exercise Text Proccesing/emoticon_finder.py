text = input()

for i in range(len(text)):
    if text[i] == ':':
        if i + 1 < len(text):
            emote = text[i] + text[i+1]
            print(emote)
