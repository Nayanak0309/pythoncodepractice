marks={
    "nayu":200,
    "nayana":30,
    "na":32


}
#print(marks,type(marks))
#print(marks.items()) #dict_items([('nayu', 200), ('nayana', 30), ('na', 32)])
#print(marks.keys()) #dict_keys(['nayu', 'nayana', 'na'])
#print(marks.values()) dict_values([200, 30, 32])

#marks.update({"harry":30})
#print(marks)  {'nayu': 200, 'nayana': 30, 'na': 32, 'harry': 30}

#print(marks.get("nsyu2")) it will gives none because it not found
#print(marks.get("nayu")) 200
#print(marks["nayu"]) 200
#print(marks["nayuu"]) it gives error

"""marks.pop("nayu")
print(marks)"""

"""marks.popitem()
print(marks)""" #it will delete the last item

"""marks.setdefault("age",33)
print(marks)"""

keys = ["a", "b", "c"]
print(dict.fromkeys(keys, 0))
