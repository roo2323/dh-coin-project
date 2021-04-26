import pymongo

ip = '132.226.228.2'
port = 27017

# Connect MongoDB
connection = pymongo.MongoClient(ip, port)

print(connection.list_database_names())

database = connection.get_database('dhcoin')

print(database)

#collection = database.get_collection('test')

# Insert Data
# collection.insert_one(
#     {
#         "name" : "has3ong",
#         "age" : 26,
#     }
# )

# result = collection.find()
# for i in result:
#     print(i)