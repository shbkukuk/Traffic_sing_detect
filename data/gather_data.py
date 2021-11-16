from icrawler.builtin import BingImageCrawler

classes = ['girilmez trafik levhası']
number = 15

for c in classes:
    bing_crawler = BingImageCrawler(storage={'root_dir':f'p{c.replace(" ","")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)