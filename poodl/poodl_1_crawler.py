#/urs/bin/python3
# -*- coding:utf-8 -*-

import requests
import SQL_util

page_flg = 1
target = 'http://api.popong.com/v0.1/bill/?api_key=test&page&per_page=100'

while(True):
		url = target.replace('&page', '&page='+str(page_flg))
		result = requests.get(url)
		page_flg = result.json()['next_page']

		for item in result.json()['items']:
				status = str(item['status'])
				is_processed = item['is_processed']
				if is_processed is True : is_processed = 1
				else: is_processed = 0
				status_id = int(item['status_id'])
				link_id = str(item['link_id'])
				status_ids = item['status_ids']
				decision_date = str(item['decision_date'])
				try:
					dyear = decision_date.split('-')[0]
					dmonth = decision_date.split('-')[1]
					ddate = decision_date.split('-')[2]
				except:
					print(decision_date)
					dyear = dmonth = ddate = 0
				
				d_dates = str(dyear) + ', ' + str(dmonth) + ', ' + str(ddate)
				
				bill_id = str(item['id'])
				proposed_date = item['proposed_date']
				try:
					pyear = proposed_date.split('-')[0]
					pmonth = proposed_date.split('-')[1]
					pdate = proposed_date.split('-')[2]
				except:
					print(proposed_date)
					pyear = pmonth = pdate = 0
				p_dates = str(pyear) + ', ' + str(pmonth) + ', ' + str(pdate)
				
				name = str(item['name'])
				assembly_id = int(item['assembly_id'])
				ids = ""	
				for s_id in status_ids:
						ids += str(s_id)+", "
				ids = ids[0:-2]

				print('\n', link_id)

				print(type(ids), type(decision_date), type(bill_id), type(proposed_date), type(name))
				
				try:
					dataset = "'"+status+"', "+str(is_processed)+", "+str(status_id)+", '"+link_id
					dataset += "', '"+ids+"', "+d_dates+", '"+bill_id+"', "+p_dates+", '"+name+"', "
					dataset += str(assembly_id)
					SQL_util.insert(dataset, 'bill_1')
				except:
					err = "'"+bill_id+"', '"+link_id+"'"
					SQL_util.insert(err, 'errs_1')

