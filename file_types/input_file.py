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
#  File    : file_types/input_file.py                            #
#  About   : Class for the generation of VAMPIRE  main input     #
#            files                                               #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 25/04/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


from file_base import File

class InputFile(File):
    def __init__(self):
        super().__init__()

    def generate_output(self, system, verbose=False):
        super().generate_output()

        if verbose:
            print('Calling function: file_types.input_file.InputFile.generate_output({})'
                       .format(system))

        # TODO: INPUT FILE GENERATION