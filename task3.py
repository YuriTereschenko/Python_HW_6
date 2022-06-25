# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если в строку
# включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию,
# которая расшифровывает эту строку обратно
import string


def code_to_rot13(text):
    upper = string.ascii_uppercase * 2
    lowcase = string.ascii_lowercase * 2
    codeed_text = ''
    for i in text:
        if i in upper:
            temp = upper
        elif i in lowcase:
            temp = lowcase
        if i in upper or i in lowcase:
            for j in range(len(temp)):
                if temp[j] == i:
                    codeed_text += temp[j + 12]
                    break
        else:
            codeed_text += i
    return codeed_text


def decode_from_rot13(text):
    upper_letters = string.ascii_uppercase * 2
    upper_letters = upper_letters[::-1]
    lowcase_letters = string.ascii_lowercase * 2
    lowcase_letters = lowcase_letters[::-1]
    decodeed_text = ''
    for i in text:
        if i in upper_letters:
            temp = upper_letters
        elif i in lowcase_letters:
            temp = lowcase_letters
        if i in upper_letters or i in lowcase_letters:
            for j in range(len(temp)):
                if temp[j] == i:
                    decodeed_text += temp[j + 12]
                    break
        else:
            decodeed_text += i
    return decodeed_text


# It is possible to combine it into one function with a choice of action,
# but for easier verification, I left it in two different

string_of_the_song = "'Look, I was gonna go easy on you not to hurt your feelings')"
coded = code_to_rot13(string_of_the_song)
print(coded)
message = "Pup kag sgqee ftq eazs?)"
decoded = decode_from_rot13(message)
print(decoded)
