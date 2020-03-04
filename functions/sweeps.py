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
#  File    : functions/sweeps.py                                 #
#  About   : A collection of functions for performing parametric #
#            sweeps                                              #
#                                                                #
#  Author  : Luke Elliott <luke.elliott@york.ac.uk>              #
#  Date    : 04/03/2020                                          #
#                                                                #
#  License :                                                     #
#                                                                #
# ============================================================== #


def linear(start, stop, n, endpoint=False):
    div  = (n - 1) if endpoint else n
    span = stop-start
    dy   = span/div
    y = start
    for i in range(n):
        yield y
        y += dy


