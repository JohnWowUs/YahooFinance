from yahoo_finance import utils
from collections import OrderedDict
import json

def test_write_dict_to_csv():
    entry1 = OrderedDict([('Field1','entry1-field1-value'), ('Field2','entry1-field2-value')])
    entry2 = OrderedDict([('Field1','entry2-field1-value'), ('Field2','entry2-field2-value')])
    test_dict = OrderedDict([(1,entry1),(2,entry2)])
    teststring = utils.write_dict_to_csv(test_dict)
    assert teststring=='"Field1","Field2"\n"entry1-field1-value","entry1-field2-value"\n"entry2-field1-value","entry2-field2-value"\n'

def test_write_dict_to_json():
    entry1 = OrderedDict([('Field1','entry1-field1-value'), ('Field2','entry1-field2-value')])
    entry2 = OrderedDict([('Field1','entry2-field1-value'), ('Field2','entry2-field2-value')])
    test_dict = OrderedDict([(1,entry1),(2,entry2)])
    teststring = utils.write_dict_to_json(test_dict)
    testdict = json.loads(teststring)
    assert testdict.keys() == ['world_indices']
    assert len(testdict['world_indices']) == 2
    testdict['world_indices'][0]['Field1'] == 'entry1-field1-value'
    testdict['world_indices'][0]['Field2'] == 'entry1-field2-value'            
    testdict['world_indices'][1]['Field1'] == 'entry2-field1-value'
    testdict['world_indices'][1]['Field2'] == 'entry2-field2-value' 
    

