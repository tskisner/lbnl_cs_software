#!/usr/bin/env python

import os
import glob
import re
import pprint as pp

entries_dir = 'entries'
templates_dir = 'source_templates'
source_dir = 'source'


packages = {}

linereg = re.compile('^\s*(.*)\s+=\s+(.*)$')
commentreg = re.compile('^#.*$')

for entryfile in glob.glob( '{}/*.txt'.format( entries_dir ) ):

    # parse the file
    
    pkg = {}
    with open( entryfile, 'r' ) as file:
        for line in file:
            if ( not commentreg.match ( line ) ):
                keyval = linereg.match ( line )
                if keyval:
                    pkg[ keyval.group(1) ] = keyval.group(2)
    
    # add pkg info to global dictionary

    if pkg[ 'CATEGORY' ] not in packages:
        packages[ pkg[ 'CATEGORY' ] ] = {}
    packages[ pkg[ 'CATEGORY' ] ][ pkg[ 'NAME' ] ] = pkg

# now go through all categories and generate the rst files

for ( category, pkgs ) in packages.iteritems():
    pp.pprint ( category )
    pp.pprint ( pkgs )


reg = re.compile('^(.*)@PACKAGES@(.*)$')

for rstfile in glob.glob( '{}/*.rst'.format( templates_dir ) ):
    category = re.sub ( '\.rst', '', rstfile )
    outrst = open ( '{}/{}'.format( source_dir, rstfile ), "w" )
    with open( rstfile, 'r' ) as file:
        for line in file:
            if ( reg.match ( line ) ):
                for ( pkgname, pkg ) in packages[ category ].iteritems():
                    outrst.write ( '{}\n'.format(pkgname) )
                    for key, val in pkg.iteritems():
                        outrst.write ( '{} = {}\n'.format( key, val ) )
            else:
                outrst.write ( line )
    outrst.close()

