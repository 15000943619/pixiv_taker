import asyncio
import aiohttp


async def download_imgs(img_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=img_url, headers={"referer": "https://www.pixiv.net/"}) as res:
            if res.status == 200:
                name = img_url.split("/")[-1]
                with open(f'./files/{name}', 'wb')as f:
                    f.write(await res.read())


def main():
    url_list = [  # 要下载图片的链接
        'https://i.pximg.net/img-original/img/2023/04/01/00/13/08/106741192_p0.jpg',
        'https://i.pximg.net/img-original/img/2023/03/28/00/00/43/106623242_p0.jpg',
        'https://i.pximg.net/img-master/img/2022/05/16/13/51/24/98386370_p0_master1200.jpg',
        'https://i.pximg.net/img-master/img/2022/05/22/00/18/12/98508889_p0_master1200.jpg',
        'https://i.pximg.net/img-original/img/2022/05/22/00/18/12/98508889_p0.jpg',
        'https://i.pximg.net/img-original/img/2017/03/29/16/21/53/62149090_p0.png',


    ]

    # 异步爬取
    task_list = [download_imgs(img_url=img_url)
                 for img_url in url_list]
    loop = asyncio.new_event_loop()
    tasks = [loop.create_task(i) for i in task_list]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
