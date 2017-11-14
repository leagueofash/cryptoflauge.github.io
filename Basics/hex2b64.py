hex_value = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#Decode the hex value
hex_decode =  hex_value.decode('hex')

#encode it to base64
b64_encode = hex_decode.encode('base64')

#can be done in a single command
#print hex_value.decode('hex').encode('base64')

print b64_encode
