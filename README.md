# Trifilar-pendulum
Trifilar pendulum for MoI measurements, Marker tracker software and GUI

## What can you find on this repository
This repository is complementary to the 10.17632/zww548rfbn.4 repository where the Hardware components of this project are outlined.
To use the software the user should run the file named: Moi_calculatrion_automatic_vXX.py. This will enable a GUI designed to perform a video track on two markers on an oscillating platform. by analysing the oscillation the Mass Moment of Inertia of the platform can be determined. The Software outputs, the MoI, the period of oscillation and a plot of the oscillation. 


Furthermore, the user will find two images (marker_N=4.png and marker_N=5.png) on this repo, they are the markers that the software uses for the video tracking, the N=5 marker should be placed in the centre of the platform. refer to the building instructions which can be found at 10.17632/zww548rfbn.4. The N=4 marker should be placed as far from the centre as possible whilst still fitting into the frame captured by the camera.

## How to use the software
Requires Python 3.9 or newer.

```bash
pip install -r requirements.txt
python Moi_calculation_automatic_v3.py

For installing Python packages refer to: https://packaging.python.org/en/latest/tutorials/installing-packages/

Once all the packages are installed the user should run the "Moi_calculation_automatic_v3.py", this will take a little time and then a GUI window will appear. Now the user can use the document Trifilar Pendulum User manual.DOCX to operate the GUI.

This Software can be used to calculate the MOI of an object without the manufacturing of a platform to put the object on if the object can be suspended from three wires/lines. The software can also be used to measure the period of oscillation of any oscillating object as long as the markers can be placed on the same plane (weight can be put in as any number as it doesn't affect the period measurement) 
