# LWD-YOLO: A Lightweight Framework for Robust Plum Maturity Grading in Unstructured Orchards
# Abstract
Accurate plum maturity grading serves as a cornerstone for intelligent orchard management, facilitating critical tasks ranging from yield forecasting and autonomous harvesting to supply chain optimization. However, robust in-field maturity grading remains a formidable challenge, primarily due to subtle chromatic variations, severe occlusion, and the stringent computational constraints of edge devices. To address these challenges, we propose LWD-YOLO, a lightweight detection framework tailored for precise maturity grading on resource-constrained deployment. 	
Specifically, the framework comprises: (1) the Gated Feature Modulation Backbone (GFMB) to emphasize subtle chromatic transitions; (2) the Spatial Context Aggregation Neck (SCAN) to enhance robustness to severe occlusion; and (3) the Shared Weight Detection Head (SWDH) to reduce parameter overhead while preserving precision.	
Experimental results on an orchard dataset demonstrate that the proposed method achieves 87.4\% mAP@50 with 1.506M parameters, while maintaining real-time performance at 125 FPS, indicating a favorable balance between accuracy and efficiency. The proposed algorithm not only offers a viable technical solution for precise yield estimation in unstructured orchards but also provides a lightweight paradigm for visual recognition on resource-constrained devices.
# Architecture of LWD-YOLO <img width="4781" height="2618" alt="fig3_architecture_overview" src="https://github.com/user-attachments/assets/2c9bf201-ae8c-49d6-9f69-10d9b26c8ca2" />
# Visualization of Effective Receptive Fields (ERF) <img width="3164" height="1770" alt="Visualization of Effective Receptive Fields (ERF)" src="https://github.com/user-attachments/assets/0a3f0fff-f41e-4d0d-b489-8d588084710e" />
# Detection under occlusion <img width="4441" height="2862" alt="fig12_detection_occluded" src="https://github.com/user-attachments/assets/79fa5857-d122-485e-8423-f618208afacf" />





