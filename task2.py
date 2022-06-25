# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в
# отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).

def rle():
    way = input("Enter the path/names for the file for compress\nDon't use ''\n")
    with open(way, 'r') as txt:
        text = txt.read()
        txt.close()
    count = 1
    rle_text = text[0]
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count != 1:
                rle_text += str(count)
            rle_text += text[i]
            count = 1
    if count != 1:
        rle_text += str(count)
    way = input("Enter the path/names for the compressed file\nDon't use ''")
    with open(way, 'w') as txt:
        txt.write(rle_text)
        txt.close()
    print('The file has been compressed')

def unrle():
    way = input("Enter the path/name of the compressed file\nDon't use ''\n")
    with open(way, 'r') as txt:
        ziped_text = txt.read()
        txt.close()
    num = ''
    unrle_text = ''
    current_letter = ziped_text[0]
    for i in range(1, len(ziped_text)):
        if ziped_text[i].isdigit():
            num = str(num) + str(ziped_text[i])
        else:
            if num == '':
                num = 1
            unrle_text = unrle_text + (current_letter * int(num))
            current_letter = ziped_text[i]
            num = ''
    way = input("Enter the path/name to save the recovered file\nDon't use ''")
    with open(way, 'w') as txt:
        txt.write(unrle_text)
        txt.close()
    print('The file has been restored')


action = input('Enter "1" to compress, "2" to recover\n')
if action == "1":
    rle()
elif action == "2":
    unrle()
else:
    print('You can only choose 1 or 2')


