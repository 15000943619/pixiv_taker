def manage_url(url):
        a=[url]
        page_number=int(input('请输入爬取页数:'))
        i=1
        for i in range(1,page_number+1):
            a.append(a[i-1].replace('p='+str(i),'p='+str(i+1)))
        return a

url='aksjflksfdjalfjl/p=1'
a=manage_url(url=url)
print(a)