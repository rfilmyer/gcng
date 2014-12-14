import random
import json

def load_json_names(filename):
    '''Loads a JSON file containing a pool of gated community names.

       >>> gcng.load_json_names('names.json')
       [['Palmetto', 'Bonita'], ['Springs', 'Shores']]

       JSON must contain at least two arrays, one titled `names`, and
       at least one array containing your pool of gated community names.
       `names` must contain the names of any arrays used in the naming
       pool.

       example: {"names": ["first", "second"],
           "first": ["Palmetto", "Bonita"],
           "second": ["Springs", "Shores"]}
    '''
    with open(filename, 'r') as fi:
       json_names = json.load(fi)
       namelist = []
       for pool in json_names['names']:
           namelist.append(json_names[pool])
       return namelist

if __name__ == '__main__':
    list_of_names = load_json_names('names.json')
    final_as_list = []
    for pool in list_of_names:
        final_as_list.append(random.choice(pool))
    output = ''
    for i in range(0, len(final_as_list)): #add a space if it's not the last item
        try:
            final_as_list[i + 1]
        except IndexError:
            space = ''
        else:
            space = ' '
        output = output + final_as_list[i] + space
    print(output)
