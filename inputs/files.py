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
#  File    : inputs/files.py                                     #
#  About   : Class for the generation of VAMPIRE material files  #
#            (.mat)                                              #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 21/02/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


# Datetime is used to provide the date in any material file generated
import datetime


class MaterialFile:
    ver = 0.01 # Refactor for general VAMPY version

    def __init__(self):
        # Strings
        self.output_store = []
        self.full_output = ''

    def write(self, line):
        self.output_store.append(line)

    def generate_output(self):
        self.full_output = '\n'.join(self.output_store)

    def write_file(self, system, output_location, header_str=None, verbose=False):
        self.output_store = []

        # Standard VAMPY header output
        #vampy_header = open('../docs/about').read()
        #self.write(vampy_header)

        if verbose:
            self.write('Calling function: files.MaterialFile.write_material_file({},{})'
                       .format(system, output_location))
        self.write('# Creation date: %s' % str(datetime.datetime.now()))
        self.write('\n')

        # User-defined header
        if header_str:
            try:
                assert type(header_str) == str
                self.write(header_str)
                self.write('\n')
            except AssertionError:
                print('[Warning] User header is not type(str)')
                print('No header defined')

        # Number of infrastructure
        self.write('# Number of materials')
        self.write('')
        self.write('material:num-materials={}'.format(len(system)))
        self.write('\n')

        # Add each material
        # %_REFACTOR_%
        for mat in system:
            self.write('# ============================================================== #')
            self.write('# Material: {}: {}'.
                       format(mat.id, mat.params['material-name']))
            self.write('# ============================================================== #')
            for param_name in mat.params:
                if mat.params[param_name] == '':
                    delim = ''
                    # self.write('material[%d]:%s%s' % (system.index(mat)+1, param_name, mat.params[param_name]))
                else:
                    delim = '='
                self.write('material[{}]:{}{}{}'.
                           format(system.index(mat)+1, param_name, delim, mat.params[param_name]))
            self.write('# ============================================================== #')
            self.write('\n')

        # Generate output string
        self.generate_output()

        # Perform write
        output_file = open(output_location, mode='w')
        output_file.write(self.full_output)
        output_file.close()