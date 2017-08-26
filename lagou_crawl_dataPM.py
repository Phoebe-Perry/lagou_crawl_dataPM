# coding=utf-8
# __author__ = 'Phoebe'

# coding=utf-8

import requests
import re

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/60.0.3112.101 Safari/537.36'
    }

    #req = requests.get('https://www.lagou.com/shenzhen-zhaopin/shujuchanpinjingli/3/', headers=headers)
    #print(req.content)

    all_job_url = []
    for i in range(1,31):
        url_list='https://www.lagou.com/shenzhen-zhaopin/shujuchanpinjingli/'+str(i)
        req=requests.get(url_list, headers=headers)
        pattern1 = "https://www.lagou.com/jobs/.*?html"
        html1 = str(req.content)
        job_url = re.compile(pattern1).findall(html1)
        job_url.pop()
        all_job_url.extend(job_url)
    #print(all_job_url)

#for i=1:
req2 =requests.get(all_job_url[1], headers=headers)
print(req2.content)


