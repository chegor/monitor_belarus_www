import requests
import time
import csv
from datetime import datetime



links = open('links.txt', 'r')
#links = open('test_links.txt', 'r')

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')


for link in links:
    link = link.strip()
    try:
        res = requests.get('http://' + link)
        print(link)
        status_code = res.status_code
        result_url = res.url


        if link in res.url:
            result_status = 'ok'
        else:
            result_status = 'BLOCKED'


        #print("\n\r")
        #time.sleep(1)

        updated_rows = [link, result_url, result_status, now, status_code]
        with open("www_results.csv", "a") as filecsv:
            writer = csv.writer(filecsv,  delimiter=',')
            writer.writerow(updated_rows)
    except OSError:
        print(link)
        result_status = 'BLOCKED'
        result_url = 'BLOCKED'
        status_code = 'BLOCKED'
        updated_rows = [link, result_url, result_status, now, status_code]
        with open("www_results.csv", "a") as filecsv:
            writer = csv.writer(filecsv, delimiter=',')
            writer.writerow(updated_rows)
