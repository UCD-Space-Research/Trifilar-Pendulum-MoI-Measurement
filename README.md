# Trifilar-pendulum
Trifilar pendulum for MoI measurements, Marker tracker software and GUI

## What can you find on this repository
This repository is complementary to the https://data.mendeley.com/drafts/zww548rfbn repository where the Hardware components of this project are outlined.
To use the software the user should run the file named: Moi_calculatrion_automatic_vXX.py. This will enable a GUI designed to perform a video track on two markers on an oscillating platform. by analysing the oscillation the Mass Moment of Inertia of the platform can be determined. The Software outputs, the MoI, the period of oscillation and a plot of the oscillation. 


Furthermore, the user will find two images (marker_N=4.png and marker_N=5.png) on this repo, they are the markers that the software uses for the video tracking, the N=5 marker should be placed in the centre of the platform. refer to the building instructions which can be found at https://data.mendeley.com/drafts/zww548rfbn. The N=4 marker should be placed as far from the centre as possible whilst still fitting into the frame captured by the camera.

## How to use the software
In order to run this file and use the related function files the following Python packages should be installed:
  * OpenCV (cv2)
  * Tkinter
  * Matplotlib

 If not installed with the devices Python version one also needs:
 
  * Time
  * OS
  * DateTime

For installing Python packages refer to: https://packaging.python.org/en/latest/tutorials/installing-packages/

Once all the packages are installed the user should run the "Moi_calculation_automatic_v3.py", this will take a little time and then a GUI window will appear. Now the user can use the document Trifilar Pendulum User manual.DOCX to operate the GUI.

This Software can be used to calculate the MOI of an object without the manufacturing of a platform to put the object on if the object can be suspended from three wires/lines. The software can also be used to measure the period of oscillation of any oscillating object as long as the markers can be placed on the same plane (weight can be put in as any number as it doesn't affect the period measurement) 

### Command-line self-test

A command-line self-test is provided to verify that the Python/OpenCV processing chain has been installed correctly.

Place the file `self_test_video.mp4` in the same folder as `self_test.py` and run:

```bash
python self_test.py
```

or, on some macOS/Linux installations:

```bash
python3 self_test.py
```

The test processes the reference video using the same functions as the graphical interface. It checks marker tracking, period extraction, and MoI calculation against a known baseline.

Expected output:

```text
PASS: OpenCV/MoI processing chain completed successfully.
```

The reference values used by the test are:

| Parameter           |          Value |
| ------------------- | -------------: |
| Platform MoI        | 0.009798 kg m² |
| Expected object MoI | 0.001123 kg m² |
| Expected period     |         0.87 s |
| Platform mass       |        616.5 g |
| Object mass         |        808.9 g |
| Frame rate          |         30 fps |
| Suspension radius   |         225 mm |
| Suspension length   |        1250 mm |
| Centre marker       |          N = 5 |
| Outer marker        |          N = 4 |
| Kernel size         |            180 |

The self-test is intended as an installation and reproducibility check rather than a replacement for experimental calibration.
