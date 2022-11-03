import pandas as pd

print(pd.__version__)

a = "141:dogs_bablu:dog:09785"

ls = a.split(":")[1:] 
 
count = 1

try:
	with open("database.csv", "r") as file:
		count = len(file.readlines()) 
		data = {"index": count, "img_id" : [ls[0]], "object_class" : [ls[1]], "accuracy": [ls[2]]}
		df = pd.DataFrame.from_dict(data)

		df.to_csv("database.csv", mode='a', index=False, header=False)
		#print("HERE")
except:
	with open("database.csv", "w") as file:
		data = {"index": count, "img_id" : [ls[0]], "object_class" : [ls[1]], "accuracy": [ls[2]]}
		df = pd.DataFrame.from_dict(data)

		df.to_csv("database.csv", mode='a', index=False, header=True)




print(df)
