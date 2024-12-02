import binascii

with open('rand_f', "rb") as f:
    data = f.read()
res = binascii.hexlify(data, " ", 4).decode().split()
for addr, i in enumerate(range(0, len(res),4)):
    print(f"{addr:08x}", ":", *res[i:i+4])