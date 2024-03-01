# *************************************************************
#                  bytes and bytearray                        #
# *************************************************************

equation = b'\xcf\x80r\xc2\xb2'
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=', ')
print()

print(equation.decode('utf-8'))
