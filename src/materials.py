# list of materials

class pla:
    def __init__(self):
        self.name = self.__class__.__name__
        self.price = 12 # USD/kg
        self.E = 3e9 # Pa
        self.rho = 1.24e3 # kg/m^3
        self.sigma_allow = 83e6 # Pa
        self.nu = 0.35

class xps:
    def __init__(self):
        self.name = self.__class__.__name__
        self.price = 8 # USD/kg
        self.E = 3.25e9 # Pa
        self.rho = 0.048e3 # kg/m^3
        self.sigma_allow = 0.7e6 # Pa
        self.nu = 0.3

class aluminum_6061:
    def __init__(self):
        self.name = self.__class__.__name__
        self.price = 4 # USD/kg
        self.E = 69e9 # Pa
        self.rho = 2.7e3 # kg/m^3
        self.sigma_allow = 276e6 # Pa
        self.nu = 0.33

class carbon:
    def __init__(self):
        self.name = self.__class__.__name__
        self.price = 12 # USD/kg
        self.E = 110e9 # Pa
        self.rho = 1.7e3 # kg/m^3
        self.sigma_allow = 1379e6 # Pa
        self.nu = 0.25
