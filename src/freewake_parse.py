# Script to create an input file for Freewake 2018, based on SW117 aircraft
# Inputs: wingspan, wing area, aircraft weight
import subprocess
import pandas as pd

def freewake_input(span, area, weight):
    # area = 
    # span = 
    # weight = 
    wing_y_left = -span/2
    wing_y_right = span/2

    # HARDCODED: filepath of Freewake input file
    path = r"C:\Users\mayar\Documents\Ryerson\AALOFT\Freewake(in_use)\input.txt"

    with open(path, "w") as f:

        f.write("Relaxed wake (yes 1, no 0): relax = 0 \n")
        f.write("Steady (1) or unsteady (2): aerodynamics = 1 \n")
        f.write("Viscous solutions (1) or inviscid (0) viscous = 1 \n")
        f.write("Symmetrical geometry (yes 1, no 0): sym = 0 \n")
        f.write("Longitudinal trim (yes 1, no 0): trim = 0 \n \n")


        f.write("Max. number of time steps:	maxtime = 3 \n")
        f.write("Width of each time step (sec):	deltime = 100.1 \n")
        f.write("Convergence delta-span effic.:	deltae = 0.00 \n \n")


        f.write("Freestream velocity (leave value 1): Uinf = 1.0 \n")
        f.write("AOA beginning, end, step size [deg]: alpha	= 0 10 1 \n")
        f.write("Sideslip angle [deg]: beta	= 0.0 \n")
        f.write("Density: density =	1.225 \n")
        f.write("Kinematic viscosity: nu = 1.4600000e-05 \n \n")


        f.write(f"Reference area: S = {area} \n")
        f.write(f"Reference span: b = {span} \n \n")


        f.write(f"Mean aerodynamic chord: cmac = 0.4 \n")
        f.write(f"Aircraft weight (N): W = {weight} \n")
        f.write("CG location (x y z): cg = 0.140 0.000000000 0.000000000 \n")
        f.write("CMo of wing: CMo = 0.000000000 \n \n")


        f.write("No. of wings (max. 5): wings = 2 \n")
        f.write("No. of panels:	panels = 4 \n")
        f.write("No. of chordwise lifting lines: m = 1 \n")
        f.write("No. of airfoils (max. 15):	airfoils = 10 \n \n")


        f.write("Panel #:1. Number of spanwise elements (n) = 40 \n")
        f.write("Neighbouring panels (0 for none) left: 0 right: 0 \n")
        f.write("xleft	yleft	zleft	chord	epsilon	Bound.Cond. Airfoil \n")
        f.write(f"0.000	{wing_y_left}	0.000	0.4		0.00	100			7 \n")
        f.write("xright	yright	zright	chord	epsilon	Bound.Cond. Airfoil \n")
        f.write(f"0.000	{wing_y_right}	0.000	0.4		0.00	100			7 \n \n")


        # f.write("Panel #:2. Number of spanwise elements (n) = 20 \n")
        # f.write("Neighbouring panels (0 for none) left: 1 right: 3 \n")
        # f.write("xleft	yleft	zleft	chord	epsilon	Bound.Cond. Airfoil \n")
        # f.write("0.000	-1.655	0.000	0.4		0.00	220			7 \n")
        # f.write("xright	yright	zright	chord	epsilon	Bound.Cond. Airfoil \n")
        # f.write("0.000	1.655	0.000	0.4		0.00	220			7 \n")


        # f.write("Panel #:2. Number of spanwise elements (n) = 10 \n")
        # f.write("Neighbouring panels (0 for none) left: 2 right: 0 \n")
        # f.write("xleft	yleft	zleft	chord	epsilon	Bound.Cond. Airfoil \n")
        # f.write("0.000	0	0.000	0.4		0.00	220			8 \n")
        # f.write("xright	yright	zright	chord	epsilon	Bound.Cond. Airfoil \n")
        # f.write("0.000	2.625	0.000	0.4		0.00	100			8 \n")

        f.write("Tail area is 0.2265 m^2 \n \n")

        f.write("Panel #:2. Number of spanwise elements (n) = 4 \n")
        f.write("Neighbouring panels (0 for none) left: 0 right: 3 \n")
        f.write("xleft	yleft	zleft	chord	epsilon	Bound.Cond. airfoil \n")
        f.write("1.805	-0.5	0.00	0.200	0.000	100			9 \n")
        f.write("xright	yright	zright	chord	epsilon	Bound.Cond. airfoil \n")
        f.write("1.78	-0.03	0.000	0.250	0.000	220			9 \n \n")

        f.write("Panel #:3. Number of spanwise elements (n) = 4 \n")
        f.write("Neighbouring panels (0 for none) left: 2 right: 4 \n")
        f.write("xleft	yleft	zleft	chord	epsilon	Bound.Cond. airfoil \n")
        f.write("1.78	-0.03 	0.00	0.250	0.000	220			9 \n")
        f.write("xright	yright	zright	chord	epsilon	Bound.Cond. airfoil \n")
        f.write("1.78	0.03	0.000	0.250	0.000	220			9 \n \n")

        f.write("Panel #:4. Number of spanwise elements (n) = 4 \n")
        f.write("Neighbouring panels (0 for none) left: 3 right: 0 \n")
        f.write("xleft	yleft	zleft	chord	epsilon	Bound.Cond. airfoil \n")
        f.write("1.78	0.03 	0.00	0.250	0.000	220			9 \n")
        f.write("xright	yright	zright	chord	epsilon	Bound.Cond. airfoil \n")
        f.write("1.805	0.5		0.000	0.200	0.000	100			9 \n \n")


        f.write("%<- special identifier \n")
        f.write("Vertical tail information: \n")
        f.write("Number of panels (max 5) = 4 \n")
        f.write("no. chord area	airfoil \n")
        f.write("no. chord area airfoil \n")
        f.write("1 0.4625 0.0636 10 \n")
        f.write("2 0.3875 0.0533 10 \n")
        f.write("3 0.3125 0.0430 10 \n")
        f.write("4 0.2375 0.0327 10 \n \n")


        f.write("Fuselage information: \n")
        f.write("Number of sections (max 20) = 41 \n")
        f.write("Width of each section = 0.0725904 \n")
        f.write("Panel where transition occurs = 6 \n")
        f.write("No. Diamter \n")
        f.write("1	0.093546819 \n")
        f.write("2	0.128235912 \n")
        f.write("3	0.155029647 \n")
        f.write("4	0.174918604 \n")
        f.write("5	0.188844343 \n")
        f.write("6	0.197714366 \n")
        f.write("7	0.20239575 \n")
        f.write("8	0.206559243 \n")
        f.write("9	0.212245212 \n")
        f.write("10	0.21689572 \n")
        f.write("11	0.221040115 \n")
        f.write("12	0.221412537 \n")
        f.write("13	0.220117334 \n")
        f.write("14	0.21904463 \n")
        f.write("15	0.216430669 \n")
        f.write("16	0.198557251 \n")
        f.write("17	0.165482307 \n")
        f.write("18	0.12237901 \n")
        f.write("19	0.083966328 \n")
        f.write("20	0.062541208 \n")
        f.write("21	0.054694869 \n")
        f.write("22	0.053106185 \n")
        f.write("23	0.052232742 \n")
        f.write("24	0.052199638 \n")
        f.write("25	0.052199638 \n")
        f.write("26	0.052199638 \n")
        f.write("27	0.052199638 \n")
        f.write("28	0.052199638 \n")
        f.write("29	0.052199638 \n")
        f.write("30	0.052199638 \n")
        f.write("31	0.052199638 \n")
        f.write("32	0.052199638 \n")
        f.write("33	0.052199638 \n")
        f.write("34	0.052199638 \n")
        f.write("35	0.052199638 \n")
        f.write("36	0.052199638 \n")
        f.write("37	0.052199638 \n")
        f.write("38	0.052199638 \n")
        f.write("39	0.052199638 \n")
        f.write("40	0.052199638 \n")
        f.write("41	0.052199638 \n \n")


        f.write("Interference drag = 0.0% \n")
        f.write("############## \n")
    
    return

def freewake_run():

    # HARDCODED: filepath of Freewake executable

    fw_folder = r"C:\Users\mayar\Documents\Ryerson\AALOFT\Freewake(in_use)"
    fw_exe = "fw_2025.exe"
    result_check = subprocess.run([fw_exe], cwd=fw_folder, capture_output=True, text=True, shell=True)
    print("Freewake ran successfully if 0: \n", result_check.returncode)

    # Get output Performance.txt file
    output_path = "C:/Users/mayar/Documents/Ryerson/AALOFT/Freewake(in_use)/output/Performance.txt"
    df_performance = pd.read_csv(output_path, sep=r'\s+', skiprows=3)

    return df_performance


