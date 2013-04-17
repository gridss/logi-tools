from distutils.core import setup, Extension
 
module1 = Extension('mark1Rpi', sources = ['mark1-rpi.c', '../fifo_lib/rpi-fifolib.c'], include_dirs=['../fifo_lib'])
 
setup (name = 'PackageName',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [module1])
