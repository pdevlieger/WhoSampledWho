import requests
import lxml.html

url = 'http://www.secondhandsongs.com'
app = '&sort=common_name&limit=10000&next=&offset=0'
parser = lxml.etree.HTMLParser(encoding='utf-8')

def get_links(url):
    tree = lxml.etree.parse(url+'/search/artist', parser)
    list = [node.attrib['href'] for node in tree.xpath('//a[@class="btn btn-mini"]')]
    return list

def get_artist_urls(letter_url):
    go_url = url + letter_url + app
    r = requests.get(go_url)
    tree = lxml.html.fromstring(r.content)
    list_name_links =  [(x.text, x.attrib['href']) for x in tree.xpath('//a') if x.attrib['href'].startswith('/artist/')]
    return list_name_links[:-18]


"""
links = get_links(url)

full_list=[]

for letter_url in links:
    temp = get_artist_urls(letter_url)
    full_list.extend(temp)
"""


def get_sampled_songs_links(tree):
    sampled_song_links = [x.attrib['href'] for x in tree.xpath('//td[@class="field-covered_by"]//a') if 'performance' in x.attrib['href']]
    return list(set(sampled_song_links))

def sampled_node_checker(node):
    return 'Sampled by' in [x.text for x in node.getparent().getparent().getparent().getparent().getparent().getchildren()]

def get_samplers(tree):
    song_urls = get_sampled_songs_links(tree)
    samplers = []
    for song_url in song_urls:
        r = requests.get(url + song_url[1])
        tree = lxml.html.fromstring(r.content)
        temp = [(x.text, x.attrib['href']) for x in tree.xpath('//td[@class="field-performer"]//a') if sampled_node_checker(x)]
        samplers.extend(list)
    return samplers

def sample_node_checker(node):
    return 'Uses samples from' in [x.text for x in node.getparent().getparent().getparent().getparent().getparent().getchildren()]

def get_samples(tree):
    song_samples = [(x.text, x.attrib['href']) for x in tree.xpath('//td[@class="field-extra"]//a') if 'artist' in x.attrib['href']]
    temp = [x.attrib['href'] for x in tree.xpath('//td[@class="field-extra"]//a') if 'performance' in x.attrib['href']]
    for link in temp:
        r = requests.get(link)
        tree = lxml.html.fromstring(r.content)
        samples_list = [(x.text, x.attrib['href']) for x in tree.xpath('//td[@class="field-performer"]//a') if sample_node_checker(x)]        
        song_samples.extend(samples_list)
    return song_samples


"""
full_list = full list of tuples (names, links)

for name_link_tup in full_list:
    go_url = url+name_link_tup[1]
    r = requests.get(go_url)
    tree = lxml.html.fromstring(r.content)
    samplers = get_samplers(tree)
    samples = get_samples(tree)
    return samplers, samples
"""
