import os
from optparse import OptionParser
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import json
from gherkin.stream.gherkin_events import GherkinEvents
from gherkin.stream.source_events import SourceEvents

parser = OptionParser()
parser.add_option("--no-source",  action="store_false", dest="print_source",  default=True, help="don't print source events")
parser.add_option("--no-ast",     action="store_false", dest="print_ast",     default=True, help="don't print ast events")
parser.add_option("--no-pickles", action="store_false", dest="print_pickles", default=True, help="don't print pickle events")

(options, args) = parser.parse_args()

source_events = SourceEvents(args)
gherkin_events = GherkinEvents(
    GherkinEvents.Options(
        print_source=options.print_source,
        print_ast=options.print_ast,
        print_pickles=options.print_pickles,
    )
)

for source_event in source_events.enum():
    for event in gherkin_events.enum(source_event):
        print(json.dumps(event))
