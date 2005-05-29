from m5 import *
from Device import PioDevice

class AlphaConsole(PioDevice):
    type = 'AlphaConsole'
    cpu = Param.BaseCPU(Parent.any, "Processor")
    disk = Param.SimpleDisk("Simple Disk")
    num_cpus = Param.Int(1, "Number of CPUs")
    sim_console = Param.SimConsole(Parent.any, "The Simulator Console")
    system = Param.BaseSystem(Parent.any, "system object")
