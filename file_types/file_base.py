# ============================================================== #
#                                                                #
#        ##     ##    ###    ##     ## ########  ##    ##        #
#        ##     ##   ## ##   ###   ### ##     ##  ##  ##         #
#        ##     ##  ##   ##  #### #### ##     ##   ####          #
#        ##     ## ##     ## ## ### ## ########     ##           #
#         ##   ##  ######### ##     ## ##           ##           #
#          ## ##   ##     ## ##     ## ##           ##           #
#           ###    ##     ## ##     ## ##           ##           #
#                                                                #
# ============================================================== #
#                                                                #
#  VAMPY is a Python library for driving VAMPIRE atomistic       #
#  magnetization dynamics simulations.                           #
#                                                                #
# -------------------------------------------------------------- #
#  File    : file_types/file_base.py                             #
#  About   : Base class for the generation of VAMPIRE input      #
#            files                                               #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 25/04/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #

from abc import ABC, abstractmethod

class File(ABC):
    ver = 0.01 # Refactor for general VAMPY version

    def __init__(self):
        # Strings
        self.output_store = []
        self.full_output = ''

    def write(self, line):
        self.output_store.append(line)

    def load_template(self, template_location)
         # Read whole template file
        template_file = open(template_location, mode='r')
        
        # Iterate through file and write to output store
        lines = list(template_file)
        for line in lines:
            self.write(line)
        
        template_file.close()

    @abstractmethod
    def generate_output(self):
        pass

    def write_header(self, header_str=None):
        if header_str:
            if header_str == 'default':
                # Standard VAMPY header output
                try:
                    vampy_header = open('../docs/about').read()
                    self.output_store.insert(0,vampy_header)
                except FileNotFoundError:
                    print("[Warning] Default VAMPY header not found: '../docs/about'")
            else:
                # User defined header
                try:
                    assert type(header_str) == str
                    self.output_store.insert(0,header_str)
                    self.write('\n')
                except AssertionError:
                    print('[Warning] User header is not type(str)')
                    print('No header defined')


    def write_file(self, system, output_location, header_str=None, verbose=False):
        if verbose:
            print('Calling function: file_types.file_base.File.write_file({},{})'
                       .format(system, output_location))

        # Pass header flag
        self.write_header(header_str)

        # Generate output string
        self.full_output = '\n'.join(self.output_store)

        # Perform write
        output_file = open(output_location, mode='w')
        output_file.write(self.full_output)
        output_file.close()