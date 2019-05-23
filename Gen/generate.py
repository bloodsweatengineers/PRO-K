import csv
import sys

def token_table(token):
    string = "#ifndef __PRO_K_TOKEN_TABLE_H__\n"
    string += "#define __PRO_K_TOKEN_TABLE_H__\n\n"
    index = 0
    string += "enum tok_t {\n\t"
    for i in range(0, len(token)):
        if index == 5:
            index = 0
            string += "\n\t"
        string += "{},".format(token[i])
        index += 1
    string += "REJECT"
    string += "\n};\n\n"

    string += "#endif"
    return string

def retrieve_bin_command(token, binary, channel):
    string = "\tenum tok_t retrieve_bin_command(uint8_t command) {\n"
    with_channel = list()
    without_channel = list()
    for i in range(0, len(binary)):
        if int(channel[i]) > 0:
            with_channel.append([token[i],binary[i]])
        else:
            without_channel.append([token[i],binary[i]])
    string += "\t\tswitch(command) {\n"
    for i in range(0, len(without_channel)):
        string += "\t\t\tcase {}:\n".format(without_channel[i][1])
        string += "\t\t\t\treturn {};\n".format(without_channel[i][0])
    string += "\t\t}\n"
    string += "\t\tswitch(command&0x0F) {\n"
    for i in range(0, len(with_channel)):
        string += "\t\t\tcase {}:\n".format(with_channel[i][1])
        string += "\t\t\t\treturn {};\n".format(with_channel[i][0])
    string += "\t\t}\n"
    string += "\t\treturn REJECT;\n"
    string += "\t}\n"
    return string

def retrieve_bin_channel(binary, channel):
    string = "\tint8_t retrieve_bin_channel(uint8_t command) {\n"
    with_channel = list()
    without_channel = list()
    for i in range(0, len(binary)):
        if int(channel[i]) > 0:
            with_channel.append(binary[i])
        else:
            without_channel.append(binary[i])
    string += "\t\tswitch(command) {\n"
    for i in without_channel:
        string += "\t\t\tcase {}:\n".format(i)
    string += "\t\t\t\treturn -1;\n"
    string += "\t\t\tdefault:\n"
    string += "\t\t\t\tbreak;\n"
    string += "\t\t}\n"

    string += "\n"

    string += "\t\tif(command&0x0F > 3) {\n"
    string += "\t\t\treturn -1;\n"
    string += "\t\t} else {\n"
    string += "\t\t\treturn command&0x0F\n"
    string += "\t\t}\n"
    string += "\t}"
    return string

def token_file(token, command, channel):
    string = '#include "token.h"\n\n'
    string += retrieve_bin_command(token, command, channel)
    string += "\n"
    string += retrieve_bin_channel(command,channel)
    return string

def main():
    token = list()
    command = list()
    channel = list()
    with open("{}/{}".format(sys.argv[1], sys.argv[2]), "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            token.append(row['token'])
            command.append(row['binary'])
            channel.append(row['channel'])
    with open("{}/token_table.h".format(sys.argv[1]),"w") as File:
        File.write(token_table(token))
    with open("{}/token.c".format(sys.argv[1]), "w") as File:
        File.write(token_file(token, command, channel))
    #with open("token_retrieve.c", "r") as File:
    #    File.write(retrieve_bin_command())
    #    File.write(retrieve_bin_channel())
    #    File.write(retrieve_str_command())
    #    File.write(retrieve_str_value())

if __name__ == "__main__":
    main()
