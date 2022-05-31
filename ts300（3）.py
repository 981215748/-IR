import requests
import parsel

bass_url='http://www.zhongguoshici.com/shici/list?cate=%E5%94%90%E8%AF%97%E4%B8%89%E7%99%BE%E9%A6%96&p='
base_url2 = 'http://www.zhongguoshici.com'
#url='http://www.zhongguoshici.com/shici/list?cate=%E5%94%90%E8%AF%97%E4%B8%89%E7%99%BE%E9%A6%96'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
for i in range(1,21):
    url=bass_url+str(i)
    response=requests.get(url,headers=headers)
    html_str=response.text
    html=parsel.Selector(html_str)
    poets_url=html.xpath('//div[@class="every_day"]/ul/a/@href').extract()
    for poet_url in poets_url:
        poet_url2 = base_url2+poet_url
        response2 = requests.get(poet_url2,headers=headers)
        html_str2 = response2.text
        html2 = parsel.Selector(html_str2)
        poet = html2.xpath('//div[@class="poem_right"]')
        the_title = poet.xpath('./div[@class="poem_title"]/span/text()').extract()
        f = open("D:\Classes\大三下\信息检索\唐诗三百首\\"+the_title[0].replace('/',' ')+".txt", "a")
        the_man = poet.xpath('./div[@class="poem_info"]//span/text()').extract()
        the_poet = poet.xpath('./div[@class="poem_content"]//p/text()').extract()
        for i in the_poet:
            f.write(str(i.replace(u'\xa0 ', u' ')))
        f.close()
