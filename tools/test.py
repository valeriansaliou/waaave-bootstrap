#!/bin/sh
# -*- coding: utf-8 -*- 
''''exec python2 -u -- "$0" ${1+"$@"} # '''

##############
#### TEST ####
##############

# Note: used for development to launch Unit tests
# Mostly called by a GitLab CI Runner instance

import os, sys


# Go to project root
os.chdir(os.path.join(os.path.dirname(__file__), '../'))


# Run tests
module_ns = "test"
trace_code = ""
return_code = 0

tests = [
    ["compass", [
        ["compile", "export PATH=\"$(ruby -e 'puts Gem.user_dir')/bin:$PATH\"; compass compile"],
    ]],
]

for cur_test in tests:
    cur_test_name = cur_test[0]

    for cur_test_task in cur_test[1]:
        if return_code is 0:
            cur_test_ns = "%s:%s" % (cur_test_name,cur_test_task[0],)

            print "--(%s)[RUN:%s]--" % (module_ns,cur_test_ns,)
            cur_test_code = os.system(cur_test_task[1])
            print "--(%s)[DONE:%s]--\n" % (module_ns,cur_test_ns,)

            if cur_test_code is not 0:
                return_code = 1
        else:
            cur_test_code = -1

        trace_code += "--(%s)[STATUS:%s:%s → %s]--\n" % (module_ns,cur_test_name,cur_test_task[0],cur_test_code,)

print trace_code


# Exit with proper return code
sys.exit(return_code)