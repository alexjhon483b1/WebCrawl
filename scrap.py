from urllib.parse import urlparse
from bs4 import BeautifulSoup

link_list = []
def extract_links(html_content, domain):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link['href']
        if not href.startswith(('http://', 'https://')):
            # Relative link, make it absolute using the specified domain
            link_list.append(domain+href)
            
        parsed_domain = urlparse(domain)
        parsed_url = urlparse(href)
        if parsed_url.netloc == parsed_domain.netloc:
            link_list.append(href)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)
    fp='x.html'
    with open(fp, 'r') as file:
          html_x = file.read()
    html_content = html_x
    domain = sys.argv[1]

    extract_links(html_content, domain)
    if domain in link_list:
        link_list.remove(domain)
    unique_list = list(set(link_list))
    print(unique_list)

