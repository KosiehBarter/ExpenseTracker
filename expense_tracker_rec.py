from expense_tracker import ExpenseTracker

class ExpenseTrackerRecognizer(object):
    def __init__(self, user_name, command, discount = 60, autosave = False):
        #super(ExpenseTrackerRecognizer, self).__init__()
        # General info
        self.user_name = user_name

        # Specifications
        self.time = self.recoznize_time(command)
        self.expense_name = self.recognize_expense(command)
        self.cost = self.recognize_cost(command.split()[2:])

        # Instance of ExpenseTracker itself
        self.ex_tr = ExpenseTracker(self.user_name)


    def recoznize_time(self, in_command):
        """
            Accepted input:
            09/29/2017 SomeExpense <value>
            29.09.2017 SomeExpense <value>
            today SomeExpense <value>
        """
        if '.' in in_command:
            return '/'.join(in_command[:10].replace(' ', '').split('.')[::-1])
        elif 'today' in in_command:
            return None
            in_command = in_command[5:]
        else: # The 'european' style formatting, without spaces
            tmp_list = in_command[:10].replace(' ', '').split('/')[::-1]
            tmp_tuple = (tmp_list[1], tmp_list[2])
            tmp_list[1] = tmp_tuple[1]
            tmp_list[2] = tmp_tuple[0]
            return '/'.join(tmp_list)

    def recognize_expense(self, in_command):
        return in_command.split()[1]

    def recognize_cost(self, in_cost_list):
        """
            Expected input:
            <value>
            <value> <discount_value>
            +<value> <discount_value>
            -<alue> <discount_value>
        """
        if '+' in in_cost_list[0]:
            pass
        elif '-' in in_cost_list[0]:
            pass
        else:
            return in_cost_list[0] # We can keep this one in str already

    def execute(self):
        self.ex_tr.check_xml_presence()
        elem = self.ex_tr.process(self.time)
        elem.set(self.expense_name, self.cost)
        self.ex_tr.write()
        # TODO: Complete expenses recognition

        return 'Your expense saved.'
    
    def return_expenses(self, date = None, end_date = None):
        """
            if date is None, then return today
        """
        
#
#    def recognize_cost(self):
#        """
#            Accepted input:
#            SomeExpense 30 <autosave>
#            SomeExpense 60 <discount_value> <autosave>
#            SomeExpense +<value> (adds) <discount_value> <autosave>
#            SomeExpense -<value> (substracts) <autosave>
#        """
#        if 'autosave' in self.command:
#            self.autosave = True
#        exp_data = self.command.split()
#        self.type = exp_data[0]
#        ## Distinguish between set, add and substract
#        if '+' in exp_data[1]:
#            pass
#        elif '-' in exp_data[1]:
#            pass
#        else:
#            self.cost = int(exp_data[1])

#
#    def get_elem(self):
#        self.elem = self.exp_tr.process(self.time)
#