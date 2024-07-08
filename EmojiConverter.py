msg = input(">")
tokens = msg.split(" ")
emoji = tokens[-1]

emoji_mapping = {
    ":(": "😔",
    ":)": "😃",
    ":D": "😜"
}
print(msg.replace(emoji, emoji_mapping.get(emoji)))