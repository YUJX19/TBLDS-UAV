# TBLDS-UAV

## Urban Scenarios

<p align="center">
  <img src="./assets/CIRYs1.png" alt="CIRYs1 Scenario" width="400"/>
  <img src="./assets/CIRYs2.png" alt="CIRYs2 Scenario" width="400"/>
</p>

The results presented in Fig.1 and Fig.2 illustrate the effectiveness of our algorithm in maintaining Line of Sight (LoS) communication between UAVs under different simulated scenarios.

In the straightforward scenario depicted in Fig.1, UAV B and C maintained 100% LoS communication using our algorithm. In contrast, the more complex scenario shown in Fig.2 demonstrated LoS communication probabilities of 95.47% and 96.17% for the UAVs, respectively.

These results underscore the robustness of our LoS-optimized spatiotemporal persistence approach, which significantly outperforms scenarios lacking LoS constraints, where UAVs frequently lose communication opportunities.

For further visualization, we have included real-time flight GIFs of the UAVs: a 2D animation corresponding to the left side of Fig.1 and another to the right side of Fig.2.

<p align="center">
  <img src="./assets/CITY50.gif" alt="City50 Scenario" width="400"/>
  <img src="./assets/CITY100.gif" alt="Complex Scenario" width="400"/>
</p>



## Reference

This UAV control algorithm is based on the work of J. Yu, J. Wu, and H. Jiang, “Spatio-Temporal Trajectory Design for UAVs: Enhancing URLLC and LoS Transmission in Communications,” IEEE Wireless Commun. Lett., pp. 1–1, 2024.

## About

If our repo helps your academic projects, please cite our paper. Thank you!

```bibtex
@article{yuSpatioTemporalTrajectoryDesign2024b,
  title = {Spatio-Temporal Trajectory Design for UAVs: Enhancing URLLC and LoS Transmission in Communications},
  shorttitle = {Spatio-Temporal Trajectory Design for UAVs},
  author = {Yu, Jingxiang and Wu, Juntao and Jiang, Hong},
  year = {2024},
  journal = {IEEE Wireless Communications Letters},
  pages = {1--1},
  issn = {2162-2337, 2162-2345},
  doi = {10.1109/LWC.2024.3416742},
  urldate = {2024-07-11},
  copyright = {https://ieeexplore.ieee.org/Xplorehelp/downloads/license-information/IEEE.html},
  langid = {english}
}
