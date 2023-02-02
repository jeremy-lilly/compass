from compass.testcase import TestCase
from compass.ocean.tests.nonhydro.solitary_wave.initial_state import \
    InitialState
from compass.ocean.tests.nonhydro.solitary_wave.forward import Forward
from compass.ocean.tests.nonhydro.solitary_wave.visualize import Visualize


class SolitaryWave(TestCase):
    """
    The default test case for the baroclinic channel test group simply creates
    the mesh and initial condition, then performs a short forward run on 4
    cores.
    """

    def __init__(self, test_group):
        """
        Create the test case

        Parameters
        ----------
        test_group : compass.ocean.tests.nonhydro.Nonhydro
            The test group that this test case belongs to
        """
        name = 'solitary_wave'
        super().__init__(test_group=test_group, name=name)

        self.add_step(
            InitialState(test_case=self))
        self.add_step(
            Forward(test_case=self, nonhydro_mode=False, name='hydro'))
        self.add_step(
            Forward(test_case=self, nonhydro_mode=True, name='nonhydro'))
        self.add_step(
            Visualize(test_case=self))

    # no run() is needed because we're doing the default: running all steps
