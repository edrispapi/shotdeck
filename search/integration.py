from elasticsearch import Elasticsearch

def get_es_client():
    return Elasticsearch(['localhost:9200'])

def search_images(query, filters):
    es = get_es_client()
    must = []
    if query:
        must.append({'multi_match': {'query': query, 'fields': ['title', 'description', 'movie_title', 'tags']}})
    for fkey, fval in filters.items():
        must.append({'term': {fkey: fval}})
    body = {"query": {"bool": {"must": must}}}
    res = es.search(index='images', body=body)
    return [hit['_source'] for hit in res['hits']['hits']]
