from xml.etree import ElementTree as ET
from os.path import exists as ospathexists
import time
import re

class ExpenseTracker(object):
    def __init__(self, user_name = 'RandomUsername'):
        # super(ExpenseTracker,__init__())
        self.xml_file = None
        self.xml_root = None
        self.xml_tree = None
        # general
        self.user_name = user_name
        self.current_time = time.strftime('Year_%Y/Month_%m/Day_%d') # format already in reverse

    def check_xml_presence(self):
        if not ospathexists(self.user_name + '.xml'):
            self.init_xml()
        else:
            self.xml_file = self.user_name + '.xml'
            self.xml_tree = ET.parse(self.xml_file)
            self.xml_root = self.xml_tree.getroot()

    def init_xml(self):
       self.xml_root = ET.Element(time.strftime(self.user_name))
       self.xml_file = self.user_name + ".xml"
       self.xml_tree = ET.ElementTree(self.xml_root)

    def append(self, parent_elem, tag_name):
        return ET.SubElement(parent_elem, tag_name)

    def attrib_set(self, elem, data, data_val):
        elem.set(data, str(data_val))
    
    # Search specified element
    def search(self, search_str, in_elem):
        search_res = in_elem.findall(search_str)
        if search_res != []:
            return search_res[0]
        else:
            return [in_elem.findall('.')[0]] # Return parent in list instead
   
    def write(self):
        self.indent(self.xml_root)
        self.xml_tree.write(self.xml_file, xml_declaration = True, encoding='utf-8')
        return 'XML saved. See it as '+ self.xml_file + '.' 

    def process(self, in_time = None):
        if in_time is None:
            in_time = self.current_time
        return self._process_rec(self.xml_root, in_time)
    
    def _process_rec(self, in_elem, path_string, search_ind = 0):
        tmp_path = path_string.split('/')
        # Try to search subelement
        if search_ind < len(tmp_path):
            elem = self.search('./' + tmp_path[search_ind], in_elem)
        else:
            return in_elem
        # Continue, if we haven't reached end of the list
        if type(elem) is not list:
            return self._process_rec(elem, path_string, search_ind + 1)
        elif type(elem) is list:
            elem = self.append(elem[0], tmp_path[search_ind])
            return self._process_rec(elem, path_string, search_ind + 1)
            
    # Tools - Indent
    def indent(self, elem, level=0):
        i = "\n" + level*"  "
        j = "\n" + (level-1)*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                self.indent(subelem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = j
        return elem