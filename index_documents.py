import glob
import xmltodict
import json
import requests

SOLR_HOST = 'http://localhost:8983'


def post_documents_solr(collection, json_data):
    r = requests.post(
        '{}/solr/{}/update/json/docs?commit=true'.format(SOLR_HOST, collection), json=json_data)

    time = r.json()['responseHeader']['QTime']
    return time


def index_documents(documents_path, collection='informationRetrieval'):
    files = glob.glob('{}/*.xml'.format(documents_path))

    for f in files:
        print('Indexing ... {}'.format(f), end='')
        with open(f) as file:
            json_data = []
            xml_doc = xmltodict.parse(file.read())
            for doc in xml_doc['add']['doc']:
                fields = doc['field']
                json_doc = {}
                for field in fields:
                    json_doc[field['@name']
                             ] = field["#text"] if "#text" in field else ''
                json_data.append(json_doc)

            time = post_documents_solr(collection, json_data)

            print('... {} docs in {}ms'.format(
                len(xml_doc['add']['doc']), time))


if __name__ == "__main__":
    index_documents('files/documents')
