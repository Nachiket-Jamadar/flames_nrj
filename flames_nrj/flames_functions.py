def cancel_and_count(n1, n2):
    n1, n2 = list(n1.lower()), list(n2.lower())
    if len(n2) > len(n1):
        n1, n2 = n2, n1

    for i in range(len(n1)):
        if n1[i] in n2 and n1[i] != 0:
            name_2_replace_index = n2.index(n1[i])
            n1[i], n2[name_2_replace_index] = 0, 0
    while 0 in n1: n1.remove(0)
    while 0 in n2: n2.remove(0)

    return len(n1)+len(n2)

def _get_nth_letter(count, flames):

    while len(flames) < count:
        flames = flames+flames
        flames_list = list(flames)
    return flames_list[count-1]

def find_relation(count):
    flames = "flames_nrj"
    while len(flames) > 1:
        nth_letter = _get_nth_letter(count, flames)
        flames = flames.replace(nth_letter, '')

    relations = {
        'f': 'Friend',
        'l': 'Love',
        'a': 'Affection',
        'm': 'Marriage',
        'e': 'Envy',
        's': 'Sibling'

    }
    return relations[flames]
