import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
db=c["college"]
coll=db["stud_list"]
#for s in coll.find({"gender":"female","course":"MCA"},{"name":1,"mark":1,"_id":0}):
   #print(s)
#for s in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
   #print(s["name"]["fname"]+" "+s["name"]["lname"])+'\n'+(s["address"]["house_name"]+" "+s["address"]["city"])+'\n'+(s["gender"]+'\n'+(s["course"])+'\n'+str(s["mark"])+'\n'+s["grade"]+'\n'+s["phone"]["type"]+" "+str(s["phone"]["no"]))
#for s in coll.find({"gender":"male","grade":"A+"}):
    #print(s["name"]["fname"]+" "+s["name"]["lname"])
#for s in coll.find({"course":"Mechanical"}).sort("mark",-1).limit(3):
    #print(s["name"]["fname"]+" "+s["name"]["lname"])
#for s in coll.find({"mark":{"$gt":90},"gender":"female"}):
    #print(s["name"]["fname"]+" "+s["name"]["lname"]+'\n'+str(s["mark"])+'\n'+str(s["phone"]["no"]))
#for s in coll.find({"mark":{"$gt":80,"$lt":90}}):
    #print(s["name"]["fname"]+" "+s["name"]["lname"])+'\n'+(s["address"]["house_name"]+" "+s["address"]["city"])+'\n'+(s["gender"]+'\n'+(s["course"])+'\n'+str(s["mark"])+'\n'+s["grade"]+'\n'+s["phone"]["type"]+" "+str(s["phone"]["no"]))
#for s in coll.find({"name.fname":{ "$regex": "^V" }}):
	#print(s["name"]["fname"]+" "+s["name"]["lname"])
	#print(s["address"]["house_name"]+" "+s["address"]["city"])
	#print(s["gender"]+'\n'+(s["course"])+'\n'+str(s["mark"]))
	#print(s["grade"]+'\n'+s["phone"]["type"]+" "+str(s["phone"]["no"])+'\n')

#for s in coll.find({"address.city":"Kollam"}):
	#print(s["name"]["fname"]+" "+s["name"]["lname"])
	#print(s["address"]["house_name"]+" "+s["address"]["city"])
	#print(s["gender"]+'\n'+(s["course"])+'\n'+str(s["mark"]))	
	#print(s["grade"]+'\n'+s["phone"]["type"]+" "+str(s["phone"]["no"]))

# for s in coll.find({"$nor":[{"address.city":"Thiruvananthapuram"},{"address.city":"Kollam"}]}):
	#print(s["name"]["fname"]+" "+s["name"]["lname"])
	#print(s["address"]["house_name"]+" "+s["address"]["city"]+'\n')
	#print(s["gender"]+'\n'+(s["course"])+'\n'+str(s["mark"]))
	#print(s["grade"]+'\n'+s["phone"]["type"]+" "+str(s["phone"]["no"])+'\n')

#for s in coll.find({"address.city":{"$in":["Thiruvananthapuram","Kollam"]}}):
	#print(s["name"]["fname"]+" "+s["name"]["lname"])
	#print(s["address"]["house_name"]+" "+s["address"]["city"])
	#print(s["gender"]+'\n'+(s["course"])+'\n'+str(s["mark"]))
	#print(s["grade"]+'\n'+s["phone"]["type"]+" "+str(s["phone"]["no"])+'\n')


