import csv, json, io, sys
from collections import OrderedDict

def write_dict_to_json(data):
    """This function pretty prints an input dictionary and returns
        its string representation i.e. a json string
    """
    jsonstring = json.dumps({"world_indices": [data[k] for k in data]}, indent=4)
    return jsonstring

def write_dict_to_csv(data):
    """This function formats an input dictionary into CSV and returns
       it as a string. Note that this assumes compatibility i.e. that the
       input is a dictionary of dictionaries and each of the sub-dictionaries 
       have same keys as every other sub-dictionary
    """
    if sys.version_info[0] > 2:
        output = io.StringIO()
    else:
        output = io.BytesIO()
    writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
    header_written = False
    for akey in data:
        if not header_written:
            writer.writerow([a for a in data[akey]])
            header_written = True
        writer.writerow([data[akey][x] for x in data[akey]])
    return output.getvalue()
