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
#  File    : file_types/material_file.py                         #
#  About   : Class for the generation of VAMPIRE material input  #
#            files (.mat)                                        #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 25/04/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


from file_base import File

class MaterialFile(File):
    def __init__(self):
        super().__init__()

    def generate_output(self, system, verbose=False):
        super().generate_output()

        if verbose:
            print('Calling function: file_types.material_file.MaterialFile.generate_output({})'
                       .format(system))

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
                           format(mat.id, param_name, delim, mat.params[param_name]))
            self.write('# ============================================================== #')
            self.write('\n')
