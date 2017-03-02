# -*- coding:utf-8 -*-

import requests
import SQL_util

page_flg = 1
target = 'http://api.popong.com/v0.2/bill/?api_key=test&page&per_page=100'

while(True):
		url = target.replace('&page', '&page='+str(page_flg))
		result = requests.get(url)
		page_flg = result.json()['next_page']

		for item in result.json()['items']:
				spons = str(item['sponsor'])
				stt = str(item['status'])
				d_date = str(item['decision_date'])
				try:
					#dyear = d_date.split('-')[0]
					#dmonth = d_date.split('-')[1]
					#ddate = d_date.split('-')[2]
					d_date = int(d_date.replace('-',''))
				except:
					#dyear = dmonth = ddate = 0
					d_date = 0
					#d_date = str(dyear) + ', ' + str(dmonth) + ', ' + str(ddate)
				
				bill_id = str(item['id'])
				p_date = item['proposed_date']
				try:
					#pyear = p_date.split('-')[0]
					#pmonth = p_date.split('-')[1]
					#pdate = p_date.split('-')[2]
					p_date = int(p_date.replace('-',''))
				except:
					p_date = 0
				
				name = str(item['name']).replace("'", '"')
				a_id = int(item['assembly_id'])
				cospon = item['cosponsors']
				spondata = ''
				for spon in cospon:
						idv = str(spon['id'])
						sponsor = str(spon['name'])
						spondata += idv+'/'+sponsor+';'
				spondata = spondata[0:-2]

				dataset = "'"+spons+"', "+str(p_date)+", '"+name+"', "+str(a_id)+", "+str(d_date)+", '"+spondata+"', '"+bill_id+"', '"+stt+"'"

				SQL_util.insert(dataset, 'bills_2')

				
				
					
