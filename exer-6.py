import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
db=c["student2"]
coll=db["cov"]
print(" 3)","\n")

for s in coll.find({"Vaccination_status":"not vaccinated"}):
	print(s["Name"]+'\n'+str(s["Phone"]))
print(" 4)","\n")

for s in coll.find({"Department":"MCA"}).sort("Lab_mark.External",-1).limit(2):
	print(s["Name"]+"\n"+str(s["Phone"]))
print(" 5)","\n")

for s in coll.find({"Name":{"$regex":"^A"}}):
	print(str(s["_id"])+"\n"+s["Name"]+"\n"+s["Department"])
print(" 6)","\n")

myq={"_id":4}
upd={"$set":{"Vaccination_status":"Both vaccinated"}}
coll.update_one(myq,upd)
print(" 7)","\n")
for s in coll.find().sort("Lab_mark.External",-1):
	print(s["Name"])

