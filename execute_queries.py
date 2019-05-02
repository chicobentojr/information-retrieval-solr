import untangle
import requests

RESULT_LIMIT = 100
SOLR_HOST = 'http://localhost:8983'
COLLECTION = 'informationRetrieval'


def get_query(topic):
    return topic.title.cdata.replace(':', '')


def show_query_result(number, docs, student='chicobentojr'):
    index = 0
    for doc in docs:
        doc_id = doc['docid']
        print('{}\tQ0\t{}\t{}\t{}\t{}'.format(
            number, doc_id[0], index, 0, student))
        index += 1


def execute_queries(collection):
    obj = untangle.parse('files/queries.xml')

    for topic in obj.root.top:
        query = get_query(topic)

        r = requests.get('{}/solr/{}/select'.format(SOLR_HOST, collection),
                         params={'q': 'text:{}'.format(query), 'rows': RESULT_LIMIT})
        result = r.json()
        docs = result['response']['docs']

        show_query_result(topic.num.cdata, docs)


if __name__ == "__main__":
    execute_queries(COLLECTION)
