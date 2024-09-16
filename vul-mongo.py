from pymongo import MongoClient

# ruleid: python-mongo-hardcoded-secret
MongoClient("mongodb://pretty:shop1234@ds139942.mlab.com:39942/moviebot")
# ok: python-mongo-hardcoded-secret
MongoClient("mongodb://a:<password>@.mlab.com:39942/moviebot")
# ok: python-mongo-hardcoded-secret
MongoClient("mongodb://<user>:a@aaaa.mlab.com:39942/moviebot")
# ok: python-mongo-hardcoded-secret
MongoClient("mongodb://user@aaaa.mlab.com:39942/moviebot")
