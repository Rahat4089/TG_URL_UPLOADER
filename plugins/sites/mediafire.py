import requests
from bs4 import BeautifulSoup
import urllib.parse
import http.client
from io import BytesIO
from gzip import GzipFile
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Encoding": "gzip",
}
def get_mediafire_direct_link(mediafire_url):
    """
    Fetch the direct download link from a Mediafire page.
    """
    try:
        parsed_url = urllib.parse.urlparse(mediafire_url)
        conn = http.client.HTTPConnection(parsed_url.netloc)
        conn.request("GET", parsed_url.path, headers=HEADERS)
        response = conn.getresponse()

        if response.getheader("Content-Encoding") == "gzip":
            compressed_data = response.read()
            with GzipFile(fileobj=BytesIO(compressed_data)) as f:
                html = f.read().decode("utf-8")

            soup = BeautifulSoup(html, "html.parser")
            download_button = soup.find("a", {"id": "downloadButton"})
            if download_button:
                return download_button.get("href")
        else:
            return mediafire_url 
    except Exception as e:
        logger.error(f"Error fetching Mediafire link: {e}")
        return None
