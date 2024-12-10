import flames_functions
from robot.api.deco import keyword, library

ROBOT_LIBRARY_SCOPE = 'TEST SUITE'


@keyword('Find Code Relation')
def find_code_relation(self, name1, name2):

    count = flames_functions.cancel_and_count(name1, name2)
    relation = flames_functions.find_relation(count)
    return relation