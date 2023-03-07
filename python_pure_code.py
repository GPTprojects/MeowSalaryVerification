import requests
def check_url_status(url):
    try:
        response = requests.get(url, allow_redirects=False)
    except requests.exceptions.RequestException:
        pass
    if response.status_code >= 300 and response.status_code < 400:
        return '薪水'
    else:
        return "瑜伽小姐"
url = 'https://ludia.gg/JWA23_0305'
check_url_status(url)    
