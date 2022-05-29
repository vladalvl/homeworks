a = b'r\xc3\xa9sum\xc3\xa9'

a_decode = a.decode()
print(a_decode)

a_encode = a_decode.encode('latin-1')
print(a_encode)

a_encode_latin_1 = a_encode.decode('latin-1')
print(a_encode_latin_1)
