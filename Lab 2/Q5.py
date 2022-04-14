#to concatenate three dictionaries into one

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4={}

for d in (dic1,dic2,dic3):
    dic1.update(d)
print(dic1)