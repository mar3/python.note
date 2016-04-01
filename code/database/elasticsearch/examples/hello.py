#!/usr/bin/env python
# coding: utf-8
#
# elasticsearch はじめの一歩 with Python
#
#
# pip install elasticsearch
#

import sys
import time
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch
import json

def _main(argv):

	INDEX_NAME = 'sample_database_20151123'
	DOC_TYPE_NAME = 'sample_entry_20151123',



	# 接続設定
	# es = Elasticsearch()
	es = Elasticsearch(host = '127.0.0.1')

	# index に document(?) を追加
	for e in range(100):
		es.index(index = INDEX_NAME, doc_type = DOC_TYPE_NAME, id = str(uuid.uuid1()), body = {})
		print '.'

	# 強制コミット
	es.indices.refresh(index = INDEX_NAME)

        # time.sleep(0.5)

	# 全件検索
	# response = es.search(index = INDEX_NAME, body = {})
	response = es.search(index = INDEX_NAME, body={"query": {"match_all": {}}, "size": 9999})

	# 結果を表示
	for e in response['hits']['hits']:
		print json.dumps(e)

	# ヒット数
	print('hits: {0}'.format(response['hits']['total']))

	# index(=データベース？？)を破棄
	es.indices.delete(index = INDEX_NAME)

_main(sys.argv)
