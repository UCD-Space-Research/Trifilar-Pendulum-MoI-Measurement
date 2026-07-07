"""
Self-test for the Trifilar Pendulum MoI OpenCV pipeline.

Run:
    python self_test.py

Expected:
    PASS: OpenCV/MoI processing chain completed successfully.
"""

import os
import sys
import math
import shutil
import tempfile
from datetime import datetime

import cv2

# Prevent OpenCV GUI windows during command-line self-test
cv2.imshow = lambda *args, **kwargs: None
cv2.waitKey = lambda *args, **kwargs: 1
cv2.destroyAllWindows = lambda *args, **kwargs: None

# Import processing functions from the main GUI script
from Moi_calculation_automatic_v3 import (
    no_audio,
    output_file_generation,
    track_all,
    Find_Moment_Of_Inertia,
    print_tau,
)

# ----------------- Baseline test values -----------------
VIDEO_FILE = "self_test_video.mp4"

PLATFORM_MOI_KGM2 = 0.009798
EXPECTED_OBJECT_MOI_KGM2 = 0.001123
EXPECTED_TAU_S = 0.87

MASS_TABLE_G = 616.5
MASS_OBJECT_G = 808.9
FPS = 30.0
R_MM = 225.0
L_MM = 1250.0

CENTRE_MARKER_N = 5
OUTER_MARKER_N = 4
KERNEL_SIZE = 180

# Tolerances for an installation/self-test, not metrology validation
TAU_TOL_S = 0.05
MOI_TOL_KGM2 = 2.0e-4


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    if not os.path.exists(VIDEO_FILE):
        fail(f"Could not find {VIDEO_FILE}. Place it in the same folder as self_test.py.")

    out_root = tempfile.mkdtemp(prefix="moi_self_test_")

    try:
        print("Running MoI OpenCV self-test...")
        print(f"Temporary output folder: {out_root}")

        m_total_g = MASS_TABLE_G + MASS_OBJECT_G

        cap = no_audio(VIDEO_FILE, out_root)
        output_file_generation()
        track_all(
            cap,
            CENTRE_MARKER_N,
            OUTER_MARKER_N,
            KERNEL_SIZE,
            progress_cb=None,
        )

        I_total_mm2g, frame, angle = Find_Moment_Of_Inertia(
            out_root,
            FPS,
            m_total_g,
            R_MM,
            L_MM,
        )

        tau = print_tau(out_root, FPS)

        I_total_kgm2 = I_total_mm2g / 1e9
        I_object_kgm2 = I_total_kgm2 - PLATFORM_MOI_KGM2

        tau_error = abs(tau - EXPECTED_TAU_S)
        moi_error = abs(I_object_kgm2 - EXPECTED_OBJECT_MOI_KGM2)

        print("\nSelf-test results")
        print("-----------------")
        print(f"Measured period:       {tau:.4f} s")
        print(f"Expected period:       {EXPECTED_TAU_S:.4f} s")
        print(f"Measured object MoI:   {I_object_kgm2:.6f} kg m^2")
        print(f"Expected object MoI:   {EXPECTED_OBJECT_MOI_KGM2:.6f} kg m^2")
        print(f"Excitation angle:      {angle:.2f} deg")

        if not math.isfinite(tau):
            fail("Period calculation returned a non-finite value.")

        if not math.isfinite(I_object_kgm2):
            fail("MoI calculation returned a non-finite value.")

        if tau_error > TAU_TOL_S:
            fail(f"Period outside tolerance: error = {tau_error:.4f} s")

        if moi_error > MOI_TOL_KGM2:
            fail(f"MoI outside tolerance: error = {moi_error:.6f} kg m^2")

        print("\nPASS: OpenCV/MoI processing chain completed successfully.")

    except Exception as exc:
        fail(f"Self-test crashed with error: {exc}")

    finally:
        shutil.rmtree(out_root, ignore_errors=True)


if __name__ == "__main__":
    main()