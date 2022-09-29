import base64

my_enc_data = base64.b64encode(b'This is my data!')

print(my_enc_data)

my_dec_data = base64.b64decode(my_enc_data)

print(my_dec_data)
