import requests, json, time, pickle
import lxml.etree, lxml.html

url = 'http://www.secondhandsongs.com'
app = '&sort=common_name&limit=30000&next=&offset=0'
parser = lxml.etree.HTMLParser(encoding='utf-8')

def get_links(url):
    tree = lxml.etree.parse(url+'/search/performance', parser)
    list = [node.attrib['href'] for node in tree.xpath('//a[@class="btn btn-mini"]')]
    return list

def get_performance_urls(letter_url):
    go_url = url + letter_url + app
    r = requests.get(go_url)
    tree = lxml.html.fromstring(r.content)
    list_name_links =  [(x.text, x.attrib['href']) for x in tree.xpath('//a') if x.attrib['href'].startswith('/performance/')]
    return list_name_links[:-10]


"""
links = get_links(url)

full_list=[]

for letter_url in links:
    temp = get_performance_urls(letter_url)
    full_list.extend(temp)
    print "letter done!"
print "Fully Done!! Tah-Dah!!"
"""


## Getting the json-files. Using requests, we want to specify the headers to get json-
## files and then read in the string the request returns as a json-file.
def get_url_as_json(url):
    r = requests.get(url, headers={'Accept': 'application/json'})
    output = json.loads(r.content)
    return output

def extract_sample_info(input_dict, output_dict, key):
# key is usesSamplesFrom or sampledBy
    if input_dict[key]:
        for j in input_dict[key]:
            output_dict[key].append((j['performance']['performer']['name'], j['performance']['title']))


def extract_cover_info(input_dict, output_dict):
# key is originals or covers
    try:
        if input_dict['covers']:
            for j in input_dict['covers']:
                output_dict['covers'].append((j['performer']['name'], j['title']))
        elif input_dict['originals']:
            for j in input_dict['originals'][0]:
                output_dict['original'].append((j['original']['performer']['name'], j['original']['title']))
    except:
        pass

def information_by_batch(start, end, list):
    batch_list = []
    i = 0
    for performance in list[start:end]:
        
        try:
            
            name = performance[0]
            
            performance_dict = {}
            performance_dict['song'] = name
            performance_dict['usesSamplesFrom'] = []
            performance_dict['sampledBy'] = []
            performance_dict['covers'] = []
            performance_dict['original'] = []
            
            go_url = url + performance[1]
            api_file = get_url_as_json(go_url)
            
            performance_dict['name'] = api_file['performer']['name']
            extract_sample_info(api_file, performance_dict, 'sampledBy')
            extract_sample_info(api_file, performance_dict, 'usesSamplesFrom')
            extract_cover_info(api_file, performance_dict)
            extract_cover_info(api_file, performance_dict)
            
            batch_list.append(performance_dict)
            
            print i
            i+=1
        
        except:
            api_file = get_url_as_json(go_url)
            print "Didn't go through!!"
        
        time.sleep(1)
        
    return batch_list


def write_to_file(data, output_name):
    pickle.dump(data, open(output_name, 'wb'))

def write_data_to_csv(input, output = 'dataset.csv'):
    f = open(output, 'wb')
    
    for dict in input:
        name = dict['name']
        if dict['covers']:
            for cover in dict['covers']:
                f.write('"%s","%s"\n' % (cover[0].encode('utf8'), name.encode('utf8')))
        elif dict['original']:
            for original in dict['original']:
                f.write('"%s","%s"\n' % (name.encode('utf8'), cover[0].encode('utf8')))
        else:
            f.write('"%s"\n' % (name.encode('utf8')))
    f.close()