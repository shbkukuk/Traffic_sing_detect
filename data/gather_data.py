from icrawler.builtin import BingImageCrawler

classes = ['turn right ahead sign']
number = 20

for c in classes:
    bing_crawler = BingImageCrawler(storage={'root_dir':f'p{c.replace(" ","")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)


"""classes=['roads','cars']
number=20
for c in classes:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'n/{c.replace(" ","")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)"""