#!/usr/bin/env python

from time import gmtime, strftime
from string import Template
import sys
import os

os.system('scons -c -Q')
source = sys.argv[1]
data = ''
if len(sys.argv) == 3:
    data = ' < ' + sys.argv[2]
name = 'app' + strftime("%Y%m%d%H%M%S", gmtime())
d = {'name':name,'source':source, 'data':data}

ofile = open('SConstruct', 'w')

ofile.write("dbg = Environment(CCFLAGS='-g')" + '\n')

program = Template("$name = dbg.Program('build/$name', '$source')")
ofile.write(program.substitute(d)+'\n')

alias = Template("Alias('$name', 'build/$name')")
ofile.write(alias.substitute(d) + '\n')

run = Template("run_$name = Command('run_$name', [] , 'build/$name $data')")
ofile.write(run.substitute(d) + '\n')

depends = Template("Depends(run_$name, $name)")
ofile.write(depends.substitute(d) + '\n')


always = Template("AlwaysBuild(run_$name)")
ofile.write(always.substitute(d) + '\n')

default = Template("Default(run_$name)")
ofile.write(default.substitute(d) + '\n')

ofile.close()
