import xml.etree.ElementTree as ET
import os
import time


class ExpenseTracker(object):
    def __init__(self, user_name = 'RandomUsername'):
        # super(ExpenseTracker,__init__())
        self.xml_file = None
        self.xml_root = None
        self.xml_tree = None
        # general
        self.user_name = user_name
        # Time related
        self.curr_month = time.strftime("Month_%m")
        self.curr_day = time.strftime("Day_%d")

        # Current data in cache
        self.current_elem = None

    def check_xml_presence(self):
        if not os.path.exists(self.user_name + '_' + time.strftime("%Y") + '.xml'):
            self.init_xml()
        else:
            self.xml_file = self.user_name + '_' + time.strftime("%Y") + '.xml'
            self.xml_tree = ET.parse(self.xml_file)
            self.xml_root = self.xml_tree.getroot()

    def init_xml(self):
       self.xml_root = ET.Element(self.user_name + "_" +time.strftime("%Y"))
       self.xml_file = self.user_name + '_' + time.strftime("%Y" + '.xml')
       self.xml_tree = ET.ElementTree(self.xml_root)

    def append(self, parent_elem, tag_name):
        ET.SubElement(parent_elem, tag_name)

    def attrib_set(self, elem, attr_dict):
        pass
    
    def search(self, search_str):
        return self.xml_tree.findall(search_str)
   
    def write(self):
        self.xml_tree.write(self.xml_file, xml_declaration = True, encoding='utf-8')
        return 'XML saved. See it as '+ self.xml_file + '.' 

    def create_command(self, command):
        if 'today' in command: # today breakfast/lunch/dinner price
            data = command.split()
            
            

    def create_query(self, query_string): # dotaz bude vypadat asi takto - s BarterBot najdi mesic MESIC/E den DEN/-DEN nebo BarterBot dnes snidane/obed/vecere cena
        basic_query = '.'
        query_list = query_string.split()

        
