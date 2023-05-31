import lcb


key = None

with open("key.txt", "r") as myfile:
    key = lcb.removeArmor(myfile.read())

lcb.encrypt(key)