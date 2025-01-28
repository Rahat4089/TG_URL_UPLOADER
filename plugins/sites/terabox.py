import requests
import json
import logging
import re
from urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_terabox_direct_link(terabox_url):
    try:
        pattern = r"/s/(\w+)|surl=(\w+)"
        
        if not re.search(pattern, terabox_url):
            return terabox_url

        
        netloc = urlparse(terabox_url).netloc
        terabox_url = terabox_url.replace(netloc, "1024tera.com")
        
        
        api_url = f'https://terabox.udayscriptsx.workers.dev/?url={terabox_url}'
        
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            direct_link = data.get('link')
            if direct_link:
                terabox_url = direct_link
                return terabox_url
            else:
                return None
        else:
            logger.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error fetching Terabox link: {e}")
        return None