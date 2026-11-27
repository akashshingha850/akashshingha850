<div align="center">

<h1>Akash Shingha Bappy</h1>

<a href="https://akashshingha850.github.io">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&duration=3200&pause=900&color=14B8A6&center=true&vCenter=true&width=560&lines=Robotics+Researcher+%40+University+of+Oulu;Autonomous+drones+%C2%B7+Digital+twins;Perception+models+on+NVIDIA+Jetson;From+raw+data+to+field+deployment" alt="Robotics researcher — autonomous drones, digital twins, edge AI" />
</a>

<p>
  <a href="https://akashshingha850.github.io"><img src="https://img.shields.io/badge/Portfolio-0f766e?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/akashshingha"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://akashshingha850.github.io/#publications"><img src="https://img.shields.io/badge/Publications-1c1917?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Publications" /></a>
  <img src="https://img.shields.io/badge/Oulu,_Finland-57534e?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Oulu, Finland" />
</p>

</div>

I build robots that see and fly on their own — and take perception models from raw data to field deployment on embedded hardware. Project Researcher in the [Biomimetics and Intelligent Systems Group](https://www.oulu.fi/en/research-groups/biomimetics-and-intelligent-systems-group), University of Oulu; previously at VTT Technical Research Centre of Finland.

🏆 **2nd prize, [NNF Master Thesis Prize 2025](https://www.nornav.org/winner-of-the-2025-nnf-master-thesis-prize.6748922-27945.html)** (Nordic Institute of Navigation) for my M.Sc. thesis on real-time UAV road intersection detection on edge devices.

<table>
  <tr>
    <td width="50%" valign="top">
      <b>🛸 Autonomous UAVs</b><br />
      GPS-denied PX4 flight, visual-inertial odometry, EKF2 fusion, onboard mission logic
    </td>
    <td width="50%" valign="top">
      <b>🧪 Digital twins</b><br />
      Isaac Sim + Pegasus twins where sim and real drones run the same ROS 2 containers
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <b>👁️ Perception & datasets</b><br />
      Detection and segmentation on RGB and LiDAR; dataset design and benchmarks
    </td>
    <td width="50%" valign="top">
      <b>⚡ Edge deployment</b><br />
      TensorRT, DeepStream and ONNX on NVIDIA Jetson — real-time and on-device
    </td>
  </tr>
</table>

### Featured work

<table>
  <tr>
    <td colspan="2" valign="top">
      <a href="https://akashshingha850.github.io/roadsight/"><b>ROADSIGHT</b></a> &nbsp;<sub><code>dataset · award-winning</code></sub><br />
      First multi-season UAV dataset for road intersection detection: <b>1,416</b> images from 62 Finnish sites across summer, autumn and winter. YOLO26n runs at <b>98 FPS</b> on Jetson Orin NX. Accepted at <i>CVC 2027</i>; grew out of my <a href="https://www.nornav.org/winner-of-the-2025-nnf-master-thesis-prize.6748922-27945.html">NNF prize-winning</a> thesis. <a href="https://akashshingha850.github.io/roadsight/">Project page</a> · <a href="https://doi.org/10.5281/zenodo.24274498">Dataset</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/akashshingha850/bisg_isaac"><b>bisg_isaac</b></a> &nbsp;<sub><code>digital twin</code></sub><br />
      Isaac Sim + PX4 twin of a ZED drone fleet. EKF2 holds within <b>1.76 m</b> of ground truth over a 359 m flight.
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/akashshingha850/kinetix"><b>Kinetix</b></a> &nbsp;<sub><code>active 3D capture</code></sub><br />
      Next-best-view photogrammetry: a monocular drone reconstructs whole rooms in fewer flights, <b>8 cm</b> camera error.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/akashshingha850/ultrahack2026"><b>RAPTOR @ UltraHack 2026</b></a> &nbsp;<sub><code>autonomy</code></sub><br />
      Fully autonomous GPS-denied search-and-detect drone at Nokia Arena — all perception on board.
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/akashshingha850/SENSEYE-Resource-Aware-Visionary-Framework"><b>SENSEYE</b></a> &nbsp;<sub><code>edge AI</code></sub><br />
      On-device assistant for visually impaired users, published in <i>Scientific Reports</i>.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/akashshingha850/raptor"><b>raptor</b></a> &nbsp;<sub><code>vision stack</code></sub><br />
      Real-time YOLO + DeepStream detection, tracking and MAVLink gimbal control on Jetson.
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/akashshingha850/local-coder"><b>local-coder</b></a> &nbsp;<sub><code>local LLM</code></sub><br />
      Private coding agent on local GPUs with vLLM, wired into VS Code.
    </td>
  </tr>
</table>

### Recent publications

- **ROADSIGHT** — multi-season UAV dataset for road intersection detection, 98 FPS on Jetson Orin NX · *CVC 2027* · [project page](https://akashshingha850.github.io/roadsight/) · [dataset](https://doi.org/10.5281/zenodo.24274498)
- **RangeGen PoleSight** — LiDAR range-image benchmark for roadside pole detection · *IVCNZ 2026* · [dataset](https://zenodo.org/records/23339206)
- **SENSEYE** — resource-aware edge-AI framework for people with visual disabilities · *Scientific Reports 2026* · [paper](https://www.nature.com/articles/s41598-026-51257-9)

### Recently active

<!-- REPOS:START -->
- [**ultrahack2026**](https://github.com/akashshingha850/ultrahack2026) <sub>Python · updated Nov 2026</sub>
- [**roadsight**](https://github.com/akashshingha850/roadsight) <sub>HTML · updated Nov 2026</sub>
- [**bisg_isaac**](https://github.com/akashshingha850/bisg_isaac) <sub>Python · updated Nov 2026</sub>
- [**kinetix**](https://github.com/akashshingha850/kinetix) <sub>Python · updated Nov 2026</sub>
- [**polesight**](https://github.com/akashshingha850/polesight) <sub>HTML · updated Nov 2026</sub>
<!-- REPOS:END -->

<sub>Updated daily by a GitHub Action.</sub>

### Stack

<p>
  <img src="https://skillicons.dev/icons?i=py,cpp,pytorch,tensorflow,opencv,ros,docker,linux,ubuntu,raspberrypi,arduino,bash&perline=12" alt="Python, C++, PyTorch, TensorFlow, OpenCV, ROS, Docker, Linux, Ubuntu, Raspberry Pi, Arduino, Bash" />
</p>
<p>
  <img src="https://img.shields.io/badge/PX4-1c1917?style=flat-square&logo=px4&logoColor=white" alt="PX4" />
  <img src="https://img.shields.io/badge/MAVLink-1c1917?style=flat-square" alt="MAVLink" />
  <img src="https://img.shields.io/badge/Isaac_Sim-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="Isaac Sim" />
  <img src="https://img.shields.io/badge/Jetson-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="NVIDIA Jetson" />
  <img src="https://img.shields.io/badge/TensorRT-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="TensorRT" />
  <img src="https://img.shields.io/badge/DeepStream-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="DeepStream" />
  <img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white" alt="ONNX" />
  <img src="https://img.shields.io/badge/YOLO-111F68?style=flat-square" alt="YOLO" />
  <img src="https://img.shields.io/badge/Gazebo-F58113?style=flat-square" alt="Gazebo" />
  <img src="https://img.shields.io/badge/ZED_SDK-1c1917?style=flat-square" alt="ZED SDK" />
</p>
