from dataclasses import dataclass
from typing import Union

from fpgaconvnet.hls.generate.modules import Module
from fpgaconvnet.models.modules import Fork

@dataclass
class GenerateFork(GenerateModule):
    batch_size: Union[int,str]
    rows: Union[int,str]
    cols: Union[int,str]
    channels: Union[int,str]
    coarse: Union[int,str]
    kernel_size_x: Union[int,str]
    kernel_size_y: Union[int,str]
    fork_t: str = "data_t"
    name: str = "fork"

    def __post_init__(self):
        # create reference fork module from models
        self.ref = Fork(
                self.rows,
                self.cols,
                self.channels,
                [
                    self.kernel_size_x,
                    self.kernel_size_y
                ],
                self.coarse
        )

    def create_module(self, input_stream, output_stream, indent=0):
        indent_tabs = "\t"*indent
        return f"""
{indent_tabs}fork<
{indent_tabs}    {self.batch_size},
{indent_tabs}    {self.rows},
{indent_tabs}    {self.cols},
{indent_tabs}    {self.channels},
{indent_tabs}    {self.coarse},
#if {self.kernel_size_x} > 1 || {self.kernel_size_y} > 1
{indent_tabs}    {self.kernel_size_x},
{indent_tabs}    {self.kernel_size_y},
#endif
{indent_tabs}    {self.fork_t}
{indent_tabs}>({input_stream},{output_stream});
        """

