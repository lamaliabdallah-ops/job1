def chiffrer_cesar(message, decalage):
    resultat = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nouvelle_position = (ord(char) - base + decalage) % 26
            nouveau_char = chr(base + nouvelle_position)
            resultat += nouveau_char
        else:
            resultat += char

    return resultat


if __name__ == "__main__":
    message = "Salut Jules Cesar !"
    decalage = 4
    message_chiffre = chiffrer_cesar(message, decalage)
    print("Message chiffré :", message_chiffre)
