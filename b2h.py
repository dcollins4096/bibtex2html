import pdb
import jinja2

def key_trim(key):
    output=key.strip()
    print(output+".")
    if key.startswith('\t'):
        output = key[1:]
    output=output.strip()
    return output
def trim_title(title):
    output=title.strip()
    output=output.strip('""')
    output=output.strip('{}')
    return output
def trim_authors(authors):
    return 'boo'

def nothing(key):
    return key

doers = {'title':trim_title,
         'authors':trim_authors}
class record():
    def __init__(self,the_type,name):
        self.the_type=the_type
        self.name=name
        self.items={}
    def eat_line(self,line):
        values = line.split(",")
        for kvp in values:
            if '=' in kvp:
                key,value = kvp.split('=')
                key = key_trim(key)
                print(key)
                doit = doers.get(key, nothing)
                self.items[key]=doit(value)

fptr = open('export-bibtex.bib','r')
this_record=None
records={}

for line in fptr.readlines():
    if line.startswith('@'):
        sploot = line.split('{')
        the_type = sploot[0][1:]
        name = sploot[1].split(',')[0]

        this_record = record(the_type,name)
        print(the_type,name)
        records[name]=this_record
    if this_record is not None:
        this_record.eat_line(line)

fptr.close()


loader=jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=loader)
template = env.get_template('bib_template_1.html')

optr=open('output.html','w')
optr.write(template.render(records= records))
optr.close()

