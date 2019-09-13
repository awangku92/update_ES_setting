import pandas as pd, numpy as np
import os, json

#index to elastics
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.helpers import bulk

# ES SETTING - change accordingly
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Use alias name
alias_index_name = 'yellow_reindex'


def closeIndex():
	# indices must be closed to update setting
	es.indices.close(index=alias_index_name)

	print('Closing '+alias_index_name+'...')
	

def updateIndexSetting():
	print('Updating setting for '+alias_index_name+'...')
	# get index setting
	# es_setting = es.indices.get_settings(index=alias_index_name)
	# print(es_setting)

	# update index setting
	setting = {
		"settings": {
				"analysis": {
					"analyzer": {
						"my_analyzer": {
							"type": "standard",
							# "type": "stop",
							# "stopwords": "_english_, https",
							"stopwords_path": "stopwords/custom_stopwords.txt"
						}
					}
				}
			}
		}

	es.indices.put_settings(body=setting , index=alias_index_name)
	# print(es_setting)
	

def openIndex():
	# open indices after updating setting
	es.indices.open(index=alias_index_name)

	# refresh indices after updating setting
	es.indices.refresh(index=alias_index_name)

	print('Opening '+alias_index_name+'...')

if __name__ == '__main__':
	print('Start')

	# UPDATE ANALYZER SETTING
	# 1) CLOSE INDEX 
	closeIndex()

	# 2) UPDATE INDEX SETTING
	updateIndexSetting()

	# 3) OPEN INDEX
	openIndex()

	print('Finish updating index setting..')