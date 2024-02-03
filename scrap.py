from urllib.parse import urlparse
from bs4 import BeautifulSoup

link_list = []
def extract_links(html_content, domain):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link['href']
        parsed_url = urlparse(href)
        if not href.startswith(('http://', 'https://')):
            # Relative link, make it absolute using the specified domain
            if not href.startswith(('//', '//')):
                  link_list.append(domain+href)
            else:
                  link_list.append(parsed_domain.scheme+":"+href)
               
        if parsed_url.netloc == parsed_domain.netloc:
            if not href.startswith(('http://', 'https://')):
                   if not href.startswith(('//', '//')):
                            link_list.append(parsed_domain.scheme+"://"+href)
                   if not href.startswith(('/', '/')):
                            link_list.append(parsed_domain.scheme+"://"+parsed_domain.netloc+"/"+href)
                   else: 
                          link_list.append(parsed_domain.scheme+":"+href)       
            if href.startswith(('http://', 'https://')):
                          link_list.append(href)


def extract_path(html_content, ndomain):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)   
    for link in links:
        href = link['href']
        parsed_url = urlparse(href)
        if href.startswith(('http://', 'https://')):
              if parsed_url.netloc == parsed_domain.netloc:
                   link_list.append(href)
        if not href.startswith(('http://', 'https://')): 
               if parsed_url.netloc == parsed_domain.netloc:
                       if href.startswith(('//', '//')):
                             link_list.append(parsed_domain.scheme+":"+href)    
                       if not href.startswith(('/', '/')):
                            link_list.append(parsed_domain.scheme+"://"+parsed_domain.netloc+parsed_domain.path+"/"+href)
                       else:
                             link_list.append(parsed_domain.scheme+":"+href)
                            
               
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
    parsed_domain = urlparse(domain)
    if parsed_domain.path != "":
           ndomain = parsed_domain.netloc
           extract_path(html_content, ndomain)
    if parsed_domain.path == "":
            extract_links(html_content, domain)
    unique_list = list(set(link_list))
    if domain in unique_list:
        unique_list.remove(domain)
    a =parsed_domain.scheme+"://"+parsed_domain.netloc+"/"
    if a in unique_list:
        unique_list.remove(a)
    for item in unique_list:
        if item != '' and item != ',':
              print(item)

