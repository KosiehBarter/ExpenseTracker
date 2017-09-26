import xml.etree.ElementTree as ET
import os
import time
import re


class ExpenseTracker(object):
    def __init__(self, user_name = 'RandomUsername', lunchcard_copay = 60):
        # super(ExpenseTracker,__init__())
        self.xml_file = None
        self.xml_root = None
        self.xml_tree = None
        # general
        self.user_name = user_name
        # Time related
        self.curr_month = time.strftime("Month_%m")
        self.curr_day = time.strftime("Day_%d")

        # Additional costs
        self.lunchcard_copay = lunchcard_copay

        # Current data in cache
        self.current_elem = None
        self.data_list = []

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

    def recognize_command(self, command):
        # start with 'generalizing'
        if 'today' in command: # today breakfast something
            command = time.strftime('%m/%d/%Y') + command[5:]
            print(command)
        if '.' in command:
            command = command.split('.')[1] + '/' + command.split('.')[0] + '/' + command[6:]

        tmp_list = re.split('\ |/', command) # Format 09 29 2017 breakfast 30 (lunchcard) (alter/delete)-this must be last!
        self.data_list.append(int(tmp_list[2]))
        self.data_list.append(int(tmp_list[0]))
        self.data_list.append(int(tmp_list[1]))
       
        # Arrange remaining data
        self.data_list.append(tmp_list[3])
        self.data_list.append(int(tmp_list[4]))
        # Additionally, additional commands
        if 'lunchcard' in command: # Substract employer's donation to see the real paid amount
            self.data_list[-1] = self.data_list[-1] - self.lunchcard_copay
        # Finally, add instructions
        if 'alter' in command or 'delete' in command:
            self.data_list.append(tmp_list[-1])
    
    def execute_command(self):
        pass