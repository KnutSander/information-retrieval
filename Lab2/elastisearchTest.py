#!usr/bin/env python3

"""Small program to test that Elasticsearch is working"""

# Import elasticsearch
from elasticsearch import Elasticsearch

# Establish a connection to it
es = Elasticsearch("http://localhost:9200")

# Custom analyzer
body = ('{"settings":{'
'"analysis":{'
'"analyzer":{'
'"my_english_analyzer":{"type":"standard","stopwords":"_english_"}'
'}}},'
'"mappings":{'
'"account":{'
'"properties":{'
'"address":{"type":"text","analyzer":"my_english_analyzer"}'
'}}}}')

# Add the analaxyr to the bank index
es.indices.create("bank", body=body)

# Documents to be added
docs = ('{"index":{"_id":"1"}}\n'
'{"account_number":1,"balance":39225,"firstname":"Amber","lastname":"Duke","age":32,"gender":"M","address":"880 Holmes Lane","employer":"Pyrami","email":"amberduke@pyrami.com","city":"Brogan","state":"IL"}\n'
'{"index":{"_id":"6"}}\n'
'{"account_number":6,"balance":5686,"firstname":"Hattie","lastname":"Bond","age":36,"gender":"M","address":"671 Bristol Street","employer":"Netagy","email":"hattiebond@netagy.com","city":"Dante","state":"TN"}\n'
'{"index":{"_id":"13"}}\n'
'{"account_number":13,"balance":32838,"firstname":"Nanette","lastname":"Bates","age":28,"gender":"F","address":"789 Madison Street","employer":"Quility","email":"nanettebates@quility.com","city":"Nogal","state":"VA"}\n'
'{"index":{"_id":"18"}}\n'
'{"account_number":18,"balance":4180,"firstname":"Dale","lastname":"Adams","age":33,"gender":"M","address":"467 Hutchinson Court","employer":"Boink","email":"daleadams@boink.com","city":"Orick","state":"MD"}\n'
'{"index":{"_id":"20"}}\n'
'{"account_number":20,"balance":16418,"firstname":"Elinor","lastname":"Ratliff","age":36,"gender":"M","address":"282 Kings Place","employer":"Scentric","email":"elinorratliff@scentric.com","city":"Ribera","state":"WA"}\n')

# Add the documents to the collection
# Bulk allows executing multiple elastic search commends in batches
es.bulk(docs, index="bank", doc_type="account")

# Query we will send to elasticsearch
query = '{"query": {"match":{"lastname":"Bond"}}}'

# Pass the query to elasticsearch
res = es.search(body=query, index="bank")

print(res)
