import materials

# CONSTANT MASSES
BATTERY_MASS = 2.584          # kg
FUSE_EMPENNAGE_MASS = 2.5     # kg

# MATERIAL DENSITY (from main)
def get_density(mat):

    if mat == 'pla':
        material = materials.pla()

    elif mat == 'xps':
        material = materials.xps()

    elif mat == 'aluminum_6061':
        material = materials.aluminum_6061()

    elif mat == 'carbon':
        material = materials.carbon()

    return material.rho

# STRUCTURAL MASS
def structural_mass(spar_volume, skin_volume, spar_mat, skin_mat):

    rho_spar = get_density(spar_mat)
    rho_skin = get_density(skin_mat)

    mass_spar = spar_volume * rho_spar
    mass_skin = skin_volume * rho_skin

    return mass_spar, mass_skin

# TOTAL AIRCRAFT MASS (KG)
def total_mass(spar_volume,
               skin_volume,
               spar_mat,
               skin_mat):

    mass_spar, mass_skin = structural_mass(
        spar_volume,
        skin_volume,
        spar_mat,
        skin_mat
    )

    total = (
        mass_spar +
        mass_skin +
        BATTERY_MASS +
        FUSE_EMPENNAGE_MASS
    )