# import os
#
# from msl import loadlib
# from msl.examples.loadlib import Cpp64
# from msl.examples.loadlib import EXAMPLES_DIR
# from msl.loadlib import Client64
# from msl.loadlib import LoadLibrary
# from msl.loadlib import Server32
#
# LOADLIB_DIR = os.path.normpath(os.path.join(EXAMPLES_DIR, os.pardir, os.pardir, 'loadlib'))
#
# paths = [
#     os.path.join(LOADLIB_DIR, 'py4j-wrapper.jar'),
#     os.path.join(EXAMPLES_DIR, 'dotnet_lib32.dll'),
#     os.path.join(EXAMPLES_DIR, 'dotnet_lib64.dll'),
#     os.path.join(EXAMPLES_DIR, 'java_lib.jar'),
#     os.path.join(EXAMPLES_DIR, 'Trig.class'),
# ]
#
# if loadlib.IS_MAC:
#     paths.extend([
#         os.path.join(EXAMPLES_DIR, 'cpp_lib64.dylib'),
#         os.path.join(EXAMPLES_DIR, 'fortran_lib64.dylib'),
#     ])
# else:
#     paths.extend([
#         os.path.join(LOADLIB_DIR, loadlib.SERVER_FILENAME),
#         os.path.join(LOADLIB_DIR, loadlib.SERVER_FILENAME + '.config'),
#         os.path.join(EXAMPLES_DIR, 'cpp_lib32' + loadlib.DEFAULT_EXTENSION),
#         os.path.join(EXAMPLES_DIR, 'cpp_lib64' + loadlib.DEFAULT_EXTENSION),
#         os.path.join(EXAMPLES_DIR, 'fortran_lib32' + loadlib.DEFAULT_EXTENSION),
#         os.path.join(EXAMPLES_DIR, 'fortran_lib64' + loadlib.DEFAULT_EXTENSION),
#     ])
#
# if loadlib.IS_WINDOWS:
#     paths.extend([
#         os.path.join(EXAMPLES_DIR, 'labview_lib32.dll'),
#         os.path.join(EXAMPLES_DIR, 'labview_lib64.dll'),
#     ])
#
# for path in paths:
#     if not os.path.isfile(path):
#         raise OSError('Cannot find: {!r}'.format(path))
