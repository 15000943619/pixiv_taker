import requests
def download_img(url):
    headers_download = {
        "referer": "https://www.pixiv.net/"
        # 这里携带referer因为p站的图片链接都是防盗链
        # 只要加上这个链接就会认为你是从p站访问过来的就会让你正常访问了
    }
    response = requests.get(url=url, headers=headers_download)#得到HTML内容
    name = url.split("/")[-1]
    # 将图片链接以斜杠分割后取最后面的信息作为名字，因为爬取的图片有jpg也有png
    with open("./files/" + name, "wb")as f:
        f.write(response.content)
    print(name + "下载成功")
j='https://i.pximg.net/img-originalter/img/2023/03/25/18/14/26/106545836_p0.jpg'
j_1='https://i.pximg.net/img-original/img/2023/03/20/08/51/32/106383133_p0.jpg'
j_2='https://i.pximg.net/img-original/img/2023/03/20/08/51/32/106383133_p0.png'
page_headers = {
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'cookie': 'first_visit_datetime_pc=2023-03-19+22:09:20; p_ab_id=8; p_ab_id_2=2; p_ab_d_id=1426367957; yuid_b=M4MiUic; PHPSESSID=92305565_NUeJMolMR8Nqi931pjP4vdKK9drgaX4K; device_token=aa6c080c4476f5285689770b804a421a; privacy_policy_agreement=5; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _ga=GA1.1.704326365.1679231439; login_ever=yes; __cf_bm=n9iv2xAQnTcUMnQ9LbuV1x5FaQRyjty19nUgQ3lj8Xk-1679492537-0-ASs1vKtNIAhZYOyr1cJoPmBfin2E6B8ZDdr+AMmpWRMhfM+D5+iu65Mynh4YETrRxiLTc9nLRyhYX+Qh7GcqMxpzDZFTFcMQIeub5KrEiSxjq2IBOoW/+J4+ZcebHiV9z0mYkpa0F12uSi8eux5yWZO/AfwpUvz4ZUjEt6JyOgZBNYIBsPv/g75AOWjsdfXYHQ==; tag_view_ranking=_EOd7bsGyl~Lt-oEicbBr~RTJMXD26Ak~ziiAzr_h04~sAwDH104z0~TqiZfKmSCg~U-RInt8VSZ~1yIPTg75Rl~IBMk1G0ITp~3W4zqr4Xlx~mUFTwA-J1U~60eEI9YvCU~ZhzlstzBJu~HqA-_UG50j~npWJIbJroU~OUF2gvwPef~GgHCEeIOHr~0Yr4YP25l8~Dp-Y5Ib1tT~DlTwYHcEzf~As0DAoQ1KZ~b_rY80S-DW~tgP8r-gOe_~Ie2c51_4Sp~99-dVV-h9A~BSlt10mdnm~ETjPkL0e6r~5oPIfUbtd6~pA1j4WTFmq~j3leh4reoN~pzZvureUki~LJo91uBPz4~pzzjRSV6ZO~eVxus64GZU~eLGuAzPy_R~9ODMAZ0ebV~DpO7Lofslr~HBlflqJjBZ~tK1rVKwWT5~uW5495Nhg-~faHcYIP1U0~CiSfl_AE0h~q3eUobDMJW~bvp7fCUKNH~-StjcwdYwv~jk9IzfjZ6n~IfWbVPYrW4~GHSY1lQ6BT~cFXtS-flQO~cryvQ5p2Tx~Kr7JNUy6TG~Ged1jLxcdL~01ilCGA69_~oYK4kF8L-4~IPIYIP0ASP~yQj24wGJWo~mFosrNEiIG~FrSumU5wXT~Mi4sJY-xXd~-KAz64Y_5p~J3ButEdVf3~4QveACRzn3~ap_AJk15dB~EQxf_UshiG~QqlTJrLZO5~EUwzYuPRbU~rXCTkjfG8N~aWHZYZcZDS~wssjDd32Z6~qtVr8SCFs5~vu8X1pzWO_~yPNaP3JSNF~kGYw4gQ11Z~miUNQvnr5u~LtW-gO6CmS~AfnLfHhcA4~o7hvUrSGDN~zIv0cf5VVk~aOGQhsapNP~OCvRKdT9WZ~7El14VK--S~m3EJRa33xU~L6MKMYowCm~ThlAk1fdQu~CrFcrMFJzz~Vxu4k2ki3N~WUjZNH_JD7~F8u6sord4r~7WfWkHyQ76~I5npEODuUW~d2oWv_4U1L~QYP1NVhSHo~UBwhLy7Ngq~pLS4i4zJjv~JrZT530U46~So7otvWMNl~UGH0V37rJQ~fg8EOt4owo~ay54Q_G6oX~YRDwjaiLZn; _ga_75BBYNYN9J=GS1.1.1679491487.3.1.1679492602.0.0.0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
        'Referer': 'https://www.pixiv.net/'
    }
download_img(j)
# if requests.get(url=j_1,headers=page_headers).status_code==200:
#     download_img(j_1)
# elif requests.get(url=j_2,headers=page_headers).status_code==200:
#     download_img(j_2)