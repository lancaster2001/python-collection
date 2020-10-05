alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
encrypt_alphabet = ("YZABCDEFGHIJKLMNOPQRSTUVWX")
message_encode = ("PLEASE_SEND_MORE_TROOPS")
message_decode = ("NJCYQC_QCLB_KMPC_RPMMNQ")
encoded_message_decoded = ("*********************")

for index in range (0,len(message_encode)):
    for index2 in range (0,len(alphabet)):
        if message_encode[index] == alphabet[index]:
            encoded_message_decoded[index] = encrypt_alphabet[index2]
        if message_encode[index] == ("_"):
            encoded_message_decoded[index] = ("-")

print(encoded_message_decoded)
