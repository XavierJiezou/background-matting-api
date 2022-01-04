import requests  # pip install requests


def matting_picup(api: str, token: str, inp_path: str, out_path: str):
    """Matting api from http://www.picup.shop/currencyBatch.html

    Args:
        api (str): Matting api from http://www.picup.shop/currencyBatch.html
        token (str): After logging in with WeChat, you will get a token
        inp_path (str): Path of the image to be matted
        out_path (str): Save path of background removed image
    """
    headers = {'token': token}
    files = {'file': open(inp_path, 'rb')}
    params = {'mattingType': 6}
    res = requests.post(api, headers=headers, files=files, params=params)
    if res.status_code == 200:
        bgRemoved_url = res.json()['data']['bgRemoved']
        bgRemoved_res = requests.get(bgRemoved_url)
        with open(out_path, 'wb') as f:
            f.write(bgRemoved_res.content)
    else:
        print(f'Status Code: {res.status_code}')


if __name__ == '__main__':
    matting_picup(
        api='http://restapi.picup.shop/webMatting/matting2',  # api接口地址
        token='90c4442bc30941eeb66137b842d4213b',  # 登录网站后获得的token
        inp_path='2.jpg',  # 输入待抠图图片的路径
        out_path='bgRemoved3.png'  # 输出背景去除图片的保存路径
    )
