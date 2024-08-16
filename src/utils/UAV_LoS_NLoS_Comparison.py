"""
This code implements path loss and SNR calculations based on formulas from:

[1] document TR36.777, “Enhanced LTE support for aerial vehicles.” 
The 3rd Generation Partnership Project (3GPP), Jan. 06, 2018. 
Accessed: Jul. 19, 2024. [Online]. Available: 
https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3231
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameter settings
distances = np.linspace(10, 200, 100)  # Distance range from 10 meters to 200 meters
frequencies = np.linspace(2.4e9, 28e9, 6)  # Frequency range from 2.4 GHz to 28 GHz
h_UT = 22.5  # User equipment height, example value
P_T_dBm = 20  # Transmission power of 20 dBm

# Thermal noise level is -174 dBm/Hz, with a noise figure of 7 dB considered
noise_figure_dB = 7  # Receiver noise figure of 7 dB
thermal_noise_dBm = -174 + 10 * np.log10(100*1e6)  # Thermal noise value at 100 MHz bandwidth

# Prepare the plot
fig, axs = plt.subplots(2, 3, figsize=(12, 8), sharex=True, sharey=True)
axs = axs.flatten()

# Iterate over each frequency to calculate and plot path loss and channel gain
for idx, fc in enumerate(frequencies):
    # Path loss using the UMa-AV LOS model
    uma_av_los_pl = 28.0 + 22 * np.log10(distances) + 20 * np.log10(fc / 1e9)

    # Path loss using the UMa-AV NLOS model
    uma_av_nlos_pl = -17.5 + (46 - 7 * np.log10(h_UT)) * np.log10(distances) + 20 * np.log10((40 * fc / 1e9) / 3)

    # Assume a simple distance attenuation model for channel gain
    channel_gain = -20 * np.log10(distances / 100)

    # Combine path loss and channel gain
    effective_los_pl = uma_av_los_pl + channel_gain
    effective_nlos_pl = uma_av_nlos_pl + channel_gain

    # Calculate received power
    P_R_los_dBm = P_T_dBm - effective_los_pl
    P_R_nlos_dBm = P_T_dBm - effective_nlos_pl

    # Calculate SNR
    SNR_los = P_R_los_dBm - (thermal_noise_dBm + noise_figure_dB)
    SNR_nlos = P_R_nlos_dBm - (thermal_noise_dBm + noise_figure_dB)

    # Plot the SNR, including channel gain
    axs[idx].plot(distances, SNR_los, label='UMa-AV LOS SNR')
    axs[idx].plot(distances, SNR_nlos, label='UMa-AV NLOS SNR')
    axs[idx].set_title(f'Frequency = {fc/1e9:.1f} GHz')
    axs[idx].set_xlabel('Distance (m)')
    axs[idx].set_ylabel('SNR (dB)')
    axs[idx].legend()
    axs[idx].grid(True)

# Adjust the layout of the plots
plt.tight_layout()

# # Save the figure to a file
# plt.savefig('UAV_SNR_Simulation.png')  # Save as PNG file

plt.show()
