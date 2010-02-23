from __future__ import absolute_import
from __future__ import print_function
from __future__ import with_statement
from __future__ import division

import evdaemon.config

def read_line(relpath):
    path = os.path.join(evdaemon.config.PATH_CONF, relpath)
    with open(path) as f:
        return f.readline().strip()

def write_line(line, relpath):
    path = os.path.join(evdaemon.config.PATH_CONF, relpath)
    with open(path, "w") as f:
        f.write(line)
        f.write("\n")

def line_to_values(line):
    line.split()
