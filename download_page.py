import requests


def get_img_url(page_url):
    page_headers = {
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'first_visit_datetime_pc=2023-03-19+22:09:20; p_ab_id=8; p_ab_id_2=2; p_ab_d_id=1426367957; yuid_b=M4MiUic; PHPSESSID=92305565_NUeJMolMR8Nqi931pjP4vdKK9drgaX4K; device_token=aa6c080c4476f5285689770b804a421a; privacy_policy_agreement=5; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _ga=GA1.1.704326365.1679231439; login_ever=yes; __cf_bm=n9iv2xAQnTcUMnQ9LbuV1x5FaQRyjty19nUgQ3lj8Xk-1679492537-0-ASs1vKtNIAhZYOyr1cJoPmBfin2E6B8ZDdr+AMmpWRMhfM+D5+iu65Mynh4YETrRxiLTc9nLRyhYX+Qh7GcqMxpzDZFTFcMQIeub5KrEiSxjq2IBOoW/+J4+ZcebHiV9z0mYkpa0F12uSi8eux5yWZO/AfwpUvz4ZUjEt6JyOgZBNYIBsPv/g75AOWjsdfXYHQ==; tag_view_ranking=_EOd7bsGyl~Lt-oEicbBr~RTJMXD26Ak~ziiAzr_h04~sAwDH104z0~TqiZfKmSCg~U-RInt8VSZ~1yIPTg75Rl~IBMk1G0ITp~3W4zqr4Xlx~mUFTwA-J1U~60eEI9YvCU~ZhzlstzBJu~HqA-_UG50j~npWJIbJroU~OUF2gvwPef~GgHCEeIOHr~0Yr4YP25l8~Dp-Y5Ib1tT~DlTwYHcEzf~As0DAoQ1KZ~b_rY80S-DW~tgP8r-gOe_~Ie2c51_4Sp~99-dVV-h9A~BSlt10mdnm~ETjPkL0e6r~5oPIfUbtd6~pA1j4WTFmq~j3leh4reoN~pzZvureUki~LJo91uBPz4~pzzjRSV6ZO~eVxus64GZU~eLGuAzPy_R~9ODMAZ0ebV~DpO7Lofslr~HBlflqJjBZ~tK1rVKwWT5~uW5495Nhg-~faHcYIP1U0~CiSfl_AE0h~q3eUobDMJW~bvp7fCUKNH~-StjcwdYwv~jk9IzfjZ6n~IfWbVPYrW4~GHSY1lQ6BT~cFXtS-flQO~cryvQ5p2Tx~Kr7JNUy6TG~Ged1jLxcdL~01ilCGA69_~oYK4kF8L-4~IPIYIP0ASP~yQj24wGJWo~mFosrNEiIG~FrSumU5wXT~Mi4sJY-xXd~-KAz64Y_5p~J3ButEdVf3~4QveACRzn3~ap_AJk15dB~EQxf_UshiG~QqlTJrLZO5~EUwzYuPRbU~rXCTkjfG8N~aWHZYZcZDS~wssjDd32Z6~qtVr8SCFs5~vu8X1pzWO_~yPNaP3JSNF~kGYw4gQ11Z~miUNQvnr5u~LtW-gO6CmS~AfnLfHhcA4~o7hvUrSGDN~zIv0cf5VVk~aOGQhsapNP~OCvRKdT9WZ~7El14VK--S~m3EJRa33xU~L6MKMYowCm~ThlAk1fdQu~CrFcrMFJzz~Vxu4k2ki3N~WUjZNH_JD7~F8u6sord4r~7WfWkHyQ76~I5npEODuUW~d2oWv_4U1L~QYP1NVhSHo~UBwhLy7Ngq~pLS4i4zJjv~JrZT530U46~So7otvWMNl~UGH0V37rJQ~fg8EOt4owo~ay54Q_G6oX~YRDwjaiLZn; _ga_75BBYNYN9J=GS1.1.1679491487.3.1.1679492602.0.0.0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    res = requests.get(url=page_url, headers=page_headers)
    # 记得先创建文件夹
    with open('./files/html/a.json', 'w', encoding='utf-8') as f:
        f.write(res.text)
    # 得到是是json文件，图片的信息在/body/illustManga/data
    # 中文编码有问题，显示的是utf-8源码


if __name__ == '__main__':
    # 女の子 是tag值
    # order=date 是由旧到新排序，order=date_d 是由新到旧排序
    # mode=safe 是全年龄，mode=all 是全部，mode=r18 是R18
    # p=1 是页码
    # lang=zh 是中文
    # 其他标签不知道用处
    get_img_url('https://www.pixiv.net/ajax/search/artworks/女の子?word=女の子&order=date_d&mode=safe&p=1&s_mode=s_tag_full&type=all&lang=zh&version=850f2ba8204f5e6a8a2e36c323bb4ec1a792f255')
