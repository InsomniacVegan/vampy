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

from typing import Generator

class ParametericSweeper:
    """Abstract parametric sweeper for use with VAMPIRE input files"""
    def __init__(self):
        self.ensemble = {}
        self.hierarchies = {}

    def add_obj(self, vmpr_obj):
        self.ensemble[vmpr_obj.id] = vmpr_obj

    def add_hierarchy(self, hierarchy: int, steps: int):
        if hierarchy in self.hierarchies:
            print('[WARNING] Hierarchy {} exists in hierarchy stack with steps {} - overwriting with steps {}'
                  .format(hierarchy, self.hierarchies[hierarchy][0], steps))
        self.hierarchies[hierarchy] = (steps, [])

    def add_param_sweep(self, hierarchy: int, mat_id: int, param: str, sw_func: Generator):

        # Form sweeping tuple
        sw_tup = (mat_id, param, sw_func)

        # Check for hierarchy existence
        if hierarchy not in self.hierarchies:
            print('[WARNING] Hierarchy {} does not exist in hierarchy stack - parameter sweep not added'
                  .format(hierarchy))
            return
        self.hierarchies[hierarchy][1].append(sw_tup)

    def sw_hierarchies(self, h_id: int):
        # Step over sweep steps
        for i in range(self.hierarchies[h_id][0]):
            # Step over parameters to sweep
            for j in range(len(self.hierarchies[h_id][1])):
                self.ensemble[param_sweep[0]] = self.hierarchies[h_id][1][j][2]
            # Recursively perform as needed
            if h_id != min(self.hierarchies.keys()):
                self.sw_hierarchies(h_id-1)





    def generate_output_files(self, file_class, naming_convention='default'):
        import os

        # REFACTOR

        # Step over objects again to find sweep variables
        for obj in self.ensemble:
            # Test for sweeping
            if len(obj) > 1:
                for param_val in obj[-1]['function'](*obj[-1]['input']):
                    obj[0].set_param(obj[-1]['param'], param_val)

                        if naming_convention == 'default':
                        param_val_str = str(param_val)
                        os.system('mkdir ' + param_val_str)
                        file_class.write_file(system=[item[0] for item in self.ensemble],
                                              output_location=(param_val_str+'/CoFeB_MTJ.mat'))