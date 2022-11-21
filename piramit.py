deger = int(input("Bir sayı giriniz = "))

for i in range(deger):
    print(" " * (i + 1) + "*" * ( deger -i ) + "*" * ( deger - i -1 ))
    print(f"' ' * {i + 1} + '*' * ({deger} - {i}) + '*' * ({deger} - {i} -1)")

""" for i in range(deger, 0, -1):
    print(" " * i + "*" * (deger - i+1) + "*" * (deger - i)) """
    # print(f"' ' * {i} + '*' * ({deger} - {i}+1) + '*' * ({deger} - {i})")
#*********
# *******
#  *****
#   ***
#    *
#    *
#   ***
#  *****
# *******
#*********

#xxxxx
#|
#|
#|
#|   x