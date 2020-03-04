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
#  File    : infrastructure/material.py                          #
#  About   : General purpose VAMPIRE material class              #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 21/02/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


from infrastructure.base import VampireObject


class Material(VampireObject):
    """Vampire material class for use with generation of material files"""
    def load_template(self, template_location):

        # Read whole template file
        template_file = open(template_location, mode='r')

        # Main file iteration loop
        lines = list(template_file)
        for line in lines:

            if line[0] == '#' or line == '':
                continue

            # Capture parameter name and value
            param_name = line.split(':')[-1].split('=')[0].strip('\n')
            if '=' in line:
                param_val = line.split('=')[-1].strip('\n')
            else:
                param_val = ''
            self.set_param(param_name, param_val)

        # Check for no tags
        if 'material-name' not in self.params:
            print('[Warning] No material name present in file: ' + template_location)
            print('Defaulting to material name: Co')
            self.params['material-name'] = 'Co'
        if 'material-element' not in self.params:
            print('[Warning] No material element present in file: ' + template_location)
            print('Defaulting to material element: Co')
            self.params['material-element'] = 'Co'

        template_file.close()

