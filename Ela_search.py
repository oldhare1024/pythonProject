from elasticsearch5 import Elasticsearch

es = Elasticsearch([{'host':'10.101.12.19','port':9200}], timeout=3600)

