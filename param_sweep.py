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


import os

class ParametericSweeper:
    """Abstract parametric sweeper for use with VAMPIRE input files"""
    def __init__(self):
        self.ensemble = {}
        self.hierarchies = {}
        self.sorted_hierarchy_keys = None
        self.file_class = None
        self.file_num = 0 # For outputting files - refactor to naming convention

    def set_output_file(self, file_class):
        self.file_class = file_class

    def add_obj(self, vmpr_obj):
        self.ensemble[vmpr_obj.id] = vmpr_obj

    def add_hierarchy(self, hierarchy: int, steps: int):
        if hierarchy in self.hierarchies:
            print('[WARNING] Hierarchy {} exists in hierarchy stack with steps {} - overwriting with steps {}'
                  .format(hierarchy, self.hierarchies[hierarchy][0], steps))
        self.hierarchies[hierarchy] = (steps, [])

    def add_param_sweep(self, hierarchy: int, mat_id: int, param: str, func_arr):
        # Form sweeping tuple
        sw_tup = (mat_id, param, func_arr)

        # Check for existence of hierarchy and material
        if hierarchy not in self.hierarchies:
            print('[WARNING] Hierarchy {} does not exist in hierarchy stack - parameter sweep not added'
                  .format(hierarchy))
            return
        if mat_id not in self.ensemble:
            print('[WARNING] Material ID: {} does not exist in system ensemble - parameter sweep not added'
                  .format(mat_id))
            return
        # If checks pass then create new hierarchy
        self.hierarchies[hierarchy][1].append(sw_tup)

    def sw_hierarchies(self, h_id: int):
        if not self.sorted_hierarchy_keys: self.sorted_hierarchy_keys=sorted(self.hierarchies)
        try:
            # Step over sweep steps
            for i in range(self.hierarchies[h_id][0]):
                # Step over parameters to sweep
                for sweep_param in self.hierarchies[h_id][1]:
                    if sweep_param[2] : self.ensemble[sweep_param[0]] = sweep_param[2][i]

                # Recursively perform as needed
                if h_id != min(self.hierarchies.keys()):
                    self.sw_hierarchies(self.sorted_hierarchy_keys
                                        [self.sorted_hierarchy_keys.index(h_id)-1])

                # Generate output file here
                if self.file_class:
                    os.system('mkdir {}'.format(self.file_num))
                    self.file_class.write_file(system=self.ensemble.values(),
                                               output_location=('{}/CoFeB_MTJ.mat').format(self.file_num))
        except IndexError:
            print('[WARNING] IndexError: likely due to number of steps in parameter sweep > len(array)')
