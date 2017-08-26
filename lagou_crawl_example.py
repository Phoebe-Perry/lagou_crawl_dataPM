# coding=utf-8

import requests
import re

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/60.0.3112.101 Safari/537.36'
    }
    # 只是一句话没有必要用方法封装起来

    for i in range(1,31):
        url_list="https://www.lagou.com/shenzhen-zhaopin/shujuchanpinjingli/"+str(i)
        req = requests.get(url_list, headers=headers)
        print(req.content)
    #req = requests.get('https://www.lagou.com/shenzhen-zhaopin/shujuchanpinjingli/2/?filterOption=3',headers=headers)
    # 把内容转换成字符串
    #text1=str(req.content)

    '''
    正则
    #part2='<div class="s_position_list.*?<div class="recommend-comp-city>'
    #part1='<li class="con_list_item default_list.*?<li class="con_list_item default_list'
    part3='<ul class="item_con_list">'
    #匹配
    job_list=re.compile(part3).findall(text1)
    print(job_list)
    '''

    #print(req.content)