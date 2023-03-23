import requests
from lxml import etree


def download_img(url):
    headers_download = {
        "referer": "https://www.pixiv.net/"
        # 这里携带referer因为p站的图片链接都是防盗链
        # 只要加上这个链接就会认为你是从p站访问过来的就会让你正常访问了
    }
    response = requests.get(url=url, headers=headers_download)
    name = url.split("/")[-1]
    # 将图片链接以斜杠分割后取最后面的信息作为名字，因为爬取的图片有jpg也有png
    with open("./files/" + name, "wb")as f:
        f.write(response.content)
    print(name + "下载成功")


if __name__ == '__main__':
    download_img(
        'https://i.pximg.net/img-master/img/2023/03/20/08/00/04/106382556_p0_master1200.jpg')
