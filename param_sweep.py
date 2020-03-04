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
#  File    : param_sweep.py                                      #
#  About   : Parametric sweeper wrapper for the generation of    #
#            VAMPIRE input files                                 #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 21/02/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


class ParametericSweeper:
    """Abstract parametric sweeper for use with VAMPIRE input files"""
    def __init__(self):
        self.ensemble = []
        self.hierarchies = {}

    def add_obj(self, vmpr_obj, sw_dict=None):
        if sw_dict:
            try:
                assert type(sw_dict) == dict
                self.ensemble.append((vmpr_obj, sw_dict))
            except AssertionError:
                print('[ERROR] Sweep parameter type must be dict')
                print('[ERROR] Object not added')
        else:
            self.ensemble.append(vmpr_obj)

    def generate_output_files(self, file_class, naming_convention='default'):
        import os

        # Step over objects again to find sweep variables
        for obj in self.ensemble:
            # Test for sweeping
            if len(obj) > 1:
                for param_val in obj[-1]['function'](*obj[-1]['input']):
                    obj[0].set_param(obj[-1]['param'], param_val)
                    if naming_convention == 'default':
                        param_val_str = str(param_val)
                        os.system('mkdir ' + param_val_str)
                        file_class.write_file(system=[item[0] for item in self.ensemble], output_location=(param_val_str+'/CoFeB_MTJ.mat'))