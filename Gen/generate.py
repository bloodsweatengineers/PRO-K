import csv

def token_table(token):
    string = "#ifndef __PRO_K_TOKEN_TABLE_H__\n"
    string += "#define __PRO_K_TOKEN_TABLE_H__\n\n"
    index = 0
    string += "enum tok_t {\n\t"
    for i in range(0, len(token) -1):
        if index == 5:
            index = 0
            string += "\n\t"
        string += "{},".format(token[i])
        index += 1
    string += token[-1]
    string += "\n};\n\n"

    string += "#endif"
    return string

def main():
    token = list()
    with open("token.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            token.append(row['token'])
    with open("token_table.h","w") as File:
        File.write(token_table(token))
    #with open("token_retrieve.c", "r") as File:
    #    File.write(retrieve_bin_command())
    #    File.write(retrieve_bin_channel())
    #    File.write(retrieve_str_command())
    #    File.write(retrieve_str_value())

if __name__ == "__main__":
    main()
