def create_first_row():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' "
    first_row = []
    for c in characters:
        first_row.append(c)
    return first_row

def create_grid(first_row):
    grid = []
    for i in range(len(first_row)):
        new_row = first_row[i:] + first_row[:i]
        grid.append(new_row)
    return grid

def create_index_dict(first_row):
    index_dict = {}
    index = 0
    for c in first_row:
        index_dict[c] = index
        index += 1
    return index_dict
#Convert text
def convert_string_to_list(string):
    list_of_characters = []
    for c in string:
        list_of_characters.append(c)
    return list_of_characters

def encrypt(key, plain_text, grid, index_dict):
    key_list = convert_string_to_list(key)
    plain_text_list = convert_string_to_list(plain_text)
    cipher_text_list = []
    index = 0
    for t in plain_text_list:
        row_index = index_dict[t]
        col_index = index_dict [key_list[index]]

        cipher_text_list.append(grid[row_index][col_index])

        index +=1
        if index == len(key_list):
            index = 0


    return "".join(cipher_text_list)

def decrypt(key, cipher_text, grid, index_dict):
    key_list = convert_string_to_list(key)
    plain_text_list = []
    index = 0
    for c in cipher_text:
        k = key_list[index]
        k_index = index_dict[k]
        row = grid[k_index]
        plain_text_index = row.index(c)
        plain_text_character = grid[0][plain_text_index]
        plain_text_list.append(plain_text_character)

        index += 1
        if index == len(key_list):
            index = 0

    return "".join(plain_text_list)

#Main
def main():
    first_row = create_first_row()
    grid = create_grid(first_row)
    index_dict = create_index_dict(first_row)
    while True:
        cmd = input("Enter e => encrypt, Enter d => decrypt: ")
        key_string = input("Enter Key: ")
        if cmd == 'e':
            plain_text_string = input("Enter plain text: ")
            cipher_text = encrypt(key_string, plain_text_string, grid, index_dict)
            print("Cipher text: " + cipher_text + "'")
        else:
            cipher_text_string = input("Enter cipher text: ")
            plain_text = decrypt(key_string, cipher_text_string, grid, index_dict)
            print("Plain text: '" + plain_text + "'")

main()