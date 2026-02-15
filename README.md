# Lightweight Plum Maturity Grading in Unstructured Orchards via Occlusion-Robust Sparse Semantic Modeling
# Abstract
Accurate plum maturity grading serves as a cornerstone for precision orchard management, facilitating critical tasks ranging from yield forecasting and autonomous harvesting to supply chain optimization. However, robust in-field maturity grading remains a challenge, primarily due to subtle chromatic variations, severe occlusion, and limited computational resources on edge devices. To address these issues, we propose LR-YOLO, a lightweight and robust detection framework tailored for precise maturity grading under resource-constrained conditions. 	
The framework incorporates the Gated Feature Modulation Backbone (GFMB) to emphasize subtle chromatic transitions, the Sparse Semantic Continuity Neck (SSCN) to enhance robustness to severe occlusion, and the Shared Weight Detection Head (SWDH) to reduce parameter overhead while preserving precision.	
To evaluate the approach, we constructed a plum orchard dataset from three Chongqing orchards covering the full growth cycle, comprising 932 images with 10,952 annotated Fruitlet, Hard, and Mature instances. The dataset captures key challenges of unstructured orchards, including class imbalance, scale variation, occlusion, and complex lighting.
Experimental results show that the proposed method achieves 87.4\% mAP@50 with 1.506M parameters, while maintaining real-time performance at 125 FPS, indicating a favorable balance between accuracy and efficiency.
# Architecture of LWD-YOLO <img width="4781" height="2618" alt="fig3_architecture_overview" src="https://github.com/user-attachments/assets/2c9bf201-ae8c-49d6-9f69-10d9b26c8ca2" />
# Visualization of Effective Receptive Fields (ERF) <img width="3164" height="1770" alt="Visualization of Effective Receptive Fields (ERF)" src="https://github.com/user-attachments/assets/0a3f0fff-f41e-4d0d-b489-8d588084710e" />
# Detection under occlusion <img width="4441" height="2862" alt="fig12_detection_occluded" src="https://github.com/user-attachments/assets/79fa5857-d122-485e-8423-f618208afacf" />





