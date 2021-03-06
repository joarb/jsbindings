#!/usr/bin/python
# ----------------------------------------------------------------------------
# Plugin to generate better enums for cocos2d
#
# Author: Ricardo Quesada
# Copyright 2013 (C) Zynga, Inc
#
# License: MIT
# ----------------------------------------------------------------------------
'''
Plugin to generate better enums for cocos2d
'''

__docformat__ = 'restructuredtext'


# python modules
import re

# plugin modules
from generate_jsb import JSBGenerateEnums


#
#
# Plugin to generate better enums for cocos2d
#
#
class JSBGenerateEnums_CC(JSBGenerateEnums):
    pass

    def get_name_for_enum(self, name):
        ok = False
        if name.startswith('kCC'):
            name = name[3:]
            ok = True

        if name.startswith('CC'):
            name = name[2:]
            ok = True

        if ok:
            n = []
            array = re.findall('[A-Z][^A-Z]*', name)
            if array and len(array) > 0:
                prev = ''
                for e in array:
                    e = e.upper()
                    if re.match('[A-Z][_0-9]?$', e) and len(n) >= 1:
                        prev = prev + e
                        n[-1] = prev
                    else:
                        n.append(e)
                        prev = e
            name = '_'.join(n)
        else:
            name = None

        return name
