valores = [911, 1178, 1356, 483, 1513, 898, 1293, 648, 1447, 1281, 964, 1511, 498, 1125, 1223, 1176, 1162, 1528, 249, 742, 941, 699, 796]
meta = 1000
qnt_bt_meta = 0

for num in valores:
    if num > 1000:
        qnt_bt_meta += 1 #Sempre que o contador encontrar um que bateu a meta, ele vai somar mais um

print(qnt_bt_meta)

        

