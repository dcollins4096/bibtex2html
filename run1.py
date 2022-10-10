import pdb
import jinja2
import re
import sys
import b2h

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-b", "--bibtex", dest="bibtex",action="store",
                                    help = "bibtex file",
                                    default="export-bibtex.bib", type = str)
parser.add_option("-o", "--output", dest="output",action="store",
                                    help = "output file",
                                    default="output.html", type = str)
parser.add_option("-t", "--template", dest="template",action="store",
                                    help = "template",
                                    default="bib_template_2.html", type = str)
(options, args) = parser.parse_args()
print(options)
print('args',args)
sys.exit(0)

records = b2h.parse_bibtex( options.bibtex)

loader=jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=loader)
template = env.get_template(options.template)

optr=open(options.output,'w')
optr.write(template.render(records= records))
optr.close()

