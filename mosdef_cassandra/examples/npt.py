
import mbuild
import foyer
import mosdef_cassandra as mc

def run_npt():

    # Use mbuild to create molecules
    methane = mbuild.load('C',smiles=True)

    # Create an empty mbuild.Box
    box = mbuild.Box(lengths=[3.,3.,3.])

    # Load forcefields
    oplsaa = foyer.forcefields.load_OPLSAA()

    # Use foyer to apply forcefields
    typed_methane = oplsaa.apply(methane)

    # Create box and species list
    box_list = [box]
    species_list = [typed_methane]

    # Use Cassandra to insert some initial number of species
    species_to_add = [[5]]

    # Define the system object
    system = mc.System(box_list,species_list,
                       species_to_add=species_to_add)
    # Get the move probabilities
    moves = mc.Moves('npt', species_list)

    # Run a simulation with at 300 K with 10000 MC moves
    # Note we must define a pressure for an NPT simulation
    mc.run(system,moves,300.0,'equilibration',10000,
            pressure=1.0)

    # 'pressure' is a valid keyword argument. To see
    # all valid keyword arguments, call mc.print_valid_kwargs()

if __name__ == "__main__":
    run_npt()