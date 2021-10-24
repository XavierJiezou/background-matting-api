import requests


def matting_picup(api: str, token: str, fname: str, save_path: str):
    """Matting api from http://www.picup.shop/currencyBatch.html

    Args:
        api (str): Matting api from http://www.picup.shop/currencyBatch.html
        token (str): After logging in with WeChat, you will get a token
        fname (str): Path of the image to be matted
        save_path (str): Save path of background removed image
    """
    headers = {'token': token}
    files = {'file': open(fname, 'rb')}
    params = {'mattingType': 6}
    res = requests.post(api, headers=headers, files=files, params=params)
    print(res.status_code)
    bgRemoved_url = res.json()['data']['bgRemoved']
    bgRemoved_res = requests.get(bgRemoved_url)
    with open(save_path, 'wb') as f:
        f.write(bgRemoved_res.content)


if __name__ == '__main__':
    matting_picup(
        api='http://restapi.picup.shop/webMatting/matting2',
        token='90c4442bc30941eeb66137b842d4213b',
        fname='test.jpg',
        save_path='bgRemoved.png'
    )
