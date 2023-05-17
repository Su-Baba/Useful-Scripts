from pymongo import MongoClient
from algoliasearch import algoliasearch

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['my_database']
mongo_collection = mongo_db['my_collection']

# Export data from MongoDB
data = [document for document in mongo_collection.find()]

# Connect to Algolia
algolia_client = algoliasearch.Client('YOUR_APP_ID', 'YOUR_API_KEY')
algolia_index = algolia_client.init_index('my_index')

# Add data to Algolia
algolia_index.add_objects(data)
