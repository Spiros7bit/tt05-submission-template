import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def tt_um_mlhdlc_sfir_fixpt(dut):
    dut._log.info("start")
