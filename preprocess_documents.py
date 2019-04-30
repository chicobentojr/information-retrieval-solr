import xmltodict
import sys
import glob


def convert_sgml_to_xml(sgml_filename, xml_filename):
    with open(sgml_filename, encoding='iso-8859-1') as file:
        sgml_string = file.read()\
            .replace('&', '&amp;')\
            .replace('< ', '&lt;')\
            .replace(' <', '&lt;')
        doc_xml = '<root>{}</root>'.format(sgml_string)
        docs = xmltodict.parse(doc_xml)
        new_xml = {
            'add': {
                'doc': []
            }
        }

        for doc in docs['root']['DOC']:
            new_doc = {'field': []}
            for key in doc.keys():
                new_doc['field'].append({
                    '@name': key.lower(),
                    '#text': doc[key].encode('utf-8') if doc[key] else '',
                })

            new_xml['add']['doc'].append(new_doc)

        result_xml = xmltodict.unparse(new_xml, pretty=True)

        with open(xml_filename, "w") as result_file:
            result_file.write(result_xml)


if __name__ == "__main__":

    documents_folder = sys.argv[1]

    files = glob.glob("{}/*.sgml".format(documents_folder))

    for f in files:
        print('Converting ... {}'.format(f))
        convert_sgml_to_xml(f,  f.replace('.sgml', '.xml'))
