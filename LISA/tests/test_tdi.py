import numpy as np
import unittest
from LISA.tdi_processor import TDIProcessor # Assumes your file is in a LISA folder

class TestLISAComponents(unittest.TestCase):
    def setUp(self):
        class MockConfig:
            sampling_rate = 10.0
            arm_length = 2.5e9
            c = 299792458.0
        self.processor = TDIProcessor(MockConfig())

    def test_tdi_cancellation(self):
        # If all laser noise is identical (perfectly correlated), 
        # TDI X should be zero (perfect cancellation)
        measurements = {k: 1.0 for k in ['12', '13', '21', '23', '31', '32']}
        # Fill buffers to ensure delayed values are also 1.0
        for _ in range(self.processor.delay_samples + 1):
            obs = self.processor.compute_tdi_observables(measurements)
        
        self.assertAlmostEqual(obs['X'], 0.0, places=7)
        print("TDI X Cancellation Test: PASSED")

if __name__ == '__main__':
    unittest.main()