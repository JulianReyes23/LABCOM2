import numpy as np
from gnuradio import gr

class e_Diff(gr.sync_block):
    def __init__(self, example_param=1.0):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name="e_Diff",  # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior = 0
        self.example_param = example_param

    def work(self, input_items, output_items):
        x = input_items[0]  # Input signal.
        y0 = output_items[0]  # Differential cumulative signal
        N = len(x)
        diff = np.cumsum(x) - self.acum_anterior
        self.acum_anterior = diff[-1]
        y0[:] = diff
        return len(y0)

