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
#  File    : infrastructure/base.py                              #
#  About   : General purpose VAMPIRE object class                #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 01/03/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


class VampireObject:
    """Vampire base object used for input files"""

    def __init__(self):

        # Object attributes
        self.params = {}

    def set_param(self, param_name, param_value):

        self.params[param_name] = param_value
