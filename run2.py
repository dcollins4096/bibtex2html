import pdb
import jinja2
import re
import sys
import b2h

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-b", "--bibtex", dest="bibtex",action="store",
                                    help = "bibtex file",
                                    default="main.bib", type = str)
parser.add_option("-o", "--output", dest="output",action="store",
                                    help = "output file",
                                    default="output.html", type = str)
parser.add_option("-t", "--template", dest="template",action="store",
                                    help = "template",
                                    default="bib_template_2.html", type = str)
(options, args) = parser.parse_args()

records = b2h.parse_bibtex( options.bibtex)

categories = b2h.get_categories( records)

loader=jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=loader)
template = env.get_template(options.template)

all_categories = list(categories.keys())
category_list = ['Star Formation','Supernova','Turbulence','Galaxies','CMB Foregrounds']
#make sure you got everything
aset = set(all_categories); bset=set(category_list)
category_list += list( aset-bset)
optr=open(options.output,'w')
optr.write(template.render(categories=categories, category_list=category_list))
optr.close()

