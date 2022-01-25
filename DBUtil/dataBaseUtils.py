import pymongo


dBKey = "mongodb+srv://@cluster0.xxpat.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Replace <username>:<password> with your own username and password in mongoDB

dBName="searchmyTDB"
scrapedTenderDtlCol="scrapedtendersdtl"
customerDetailCol="customerMaster"
collectionNameDelta='siteDetail'
customerUID = "Cust123"
Epwd="SearchMyTenders@1234"
#incase of key uncomment below line
#client = MongoClient(dBKey)
client = pymongo.MongoClient()



#code to extract the sequencerCode from DB


#code to extract the Array of keywords
# Code for Keyword extraction starts here--------
smtDB = client[dBName]
colscrapedTenderDtl = smtDB[scrapedTenderDtlCol]
colName =smtDB[customerDetailCol]
# Declare a list variable to store whole string keyword in it.
keywordResults = colName.find() #removed customerUID as scraping require all customer keywords
keywordList = []
# Declare a set variable to store individual keyword in it and to avoid duplication
keywordListSet = set()
# Adding each keyword in set after removing white spaces before and after it
for keywordResult in keywordResults:
    keywordList = keywordResult['CustKeywords'].split(',')
    for l in keywordList:
        keywordListSet.add(l.strip())

# Set into a list. So we get a list of keywords without any duplication.
keywordArr = list(keywordListSet)



