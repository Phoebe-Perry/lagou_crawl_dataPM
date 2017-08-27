# coding=utf-8
# __author__ = 'Phoebe'

import requests
import re
import time

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/60.0.3112.101 Safari/537.36'
    }

    #req = requests.get('https://www.lagou.com/shenzhen-zhaopin/shujuchanpinjingli/3/', headers=headers)
    #print(req.content)

    #得到所有的职位网址
    all_job_url = []
    for i in range(1,31):
        url_list='https://www.lagou.com/beijing-zhaopin/shujuchanpinjingli/'+str(i)
        req=requests.get(url_list, headers=headers)
        pattern1 = "https://www.lagou.com/jobs/[0-9]+\.html"
        html1 = str(req.content)
        job_url = re.compile(pattern1).findall(html1)
        #job_url.pop()
        all_job_url.extend(job_url)
    #print(all_job_url)

    #得到网址的内容
    j = 1
    for i in all_job_url:
        req2 =requests.get(i, headers=headers)
        print(j)
        j = j+1
        #print(all_job_url[i])

        pat_salary = '<span class="salary">(.*?)</span>'
        #pat_job_lables = 'position-label(.*?)'
        pat_job_bt = '<h3 class="description">([\s\S]*?)</div>'
        pat_company = '<h2 class="fl">([\s\S]*?)<i class'
        pat_job_name = '<span class="name">([\s\S]*?)</span>'

        salary = re.compile(pat_salary).findall(str(req2.content))
        job_bt = re.compile(pat_job_bt).findall(str(req2.content))
        company = re.compile(pat_company).findall(str(req2.content))
        job_name = re.compile(pat_job_name).findall(str(req2.content))

        if len(company)>0:
            print(company[0].decode('utf-8'))
            print(job_name[0].decode('utf-8'))
            print(salary[0])
            print(job_bt[0].decode('utf-8'))
        else:
            print(i)

        time.sleep(15)



