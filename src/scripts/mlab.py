from pymongo import MongoClient

def connect():

    try:
        # Python 3.x
        from urllib.parse import quote_plus
    except ImportError:
        # Python 2.x
        from urllib import quote_plus

    uri = "mongodb://%s:%s@%s" % (
        quote_plus("eliga_user"), quote_plus("pepejatireiavela"), "ds143151.mlab.com:43151/eliga")
    client = MongoClient(uri)
    return client.eliga
