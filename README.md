# Information Retrieval - Apache Solr

Work developed for Information Retrieval discipline of Postgraduate in Computer Science course, at UFRGS.
The objective is to practice the topics teached in class using a Information Retrieval software.
We have chosen [Apache Solr](https://lucene.apache.org/solr/).

## Requirements

* [Apache Solr installation](https://lucene.apache.org/solr/guide/7_7/installing-solr.html)
* Python 3.6+
* PIP Packages: untangle; xmltodict; requests.

## Steps to run
Considering that Solr have already been started.

### 1. Pre-processing documents

Convert all collection files from SGML to XML before indexing. All files should be located at `files/documents` folder.

```
$ python3 preprocess_documents.py files/documents
```

### 2. Indexing documents

```
$ python3 index_documents.py
```

### 3. Executing queries
```
$ python3 execute_queries.py > results.txt
```
