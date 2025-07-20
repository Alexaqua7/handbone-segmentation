# ✋ Hand Bone Image Segmentation
<img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/PyTorch-E34F26?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/Segmentation-Medical-green?style=for-the-badge">

> 본 프로젝트는 **손 뼈 X-ray 이미지**를 기반으로, 딥러닝을 활용한 **정확한 뼈 구조 세분화(Segmentation)** 모델을 개발합니다.  
> 이는 질병 진단, 수술 계획, 의료장비 설계 등 다양한 의료 분야에 실질적인 기여를 목표로 합니다.

---

## 📌 프로젝트 개요

정확한 뼈 분할은 다음과 같은 다양한 의료 목적에 활용됩니다:

✅ **질병 진단**: 골절, 기형 등 이상 여부 탐지  
✅ **수술 계획**: 수술 방법 및 재료 선택을 위한 구조 분석  
✅ **의료장비 제작**: 인공관절, 임플란트 등에 필요한 뼈 형상 정보 제공  
✅ **의료 교육**: 병변 및 손상 이해, 수술 시뮬레이션 등에 활용  

<div align="center">
  <img src="https://github.com/user-attachments/assets/f7ee7a87-b032-4c5e-b391-438d08b79fe9" width="600"/>
</div>

---

## 🗂️ Data Description

- **Input**  
  - 손 뼈 X-ray 이미지  
  - 각 이미지에 대한 segmentation annotation (JSON 형식)

- **Output**  
  - 29개 클래스에 대한 **multi-channel probability map**  
  - 최종 예측은 **pixel-level classification**

- **Submission Format**  
  - 예측 결과는 **Run-Length Encoding (RLE)** 형식의 `.csv` 파일로 제출  

---

## 🚀 How to Use

### 1. Installation

```bash
git clone https://github.com/boostcampaitech7/level2-cv-semanticsegmentation-cv-01-lv3.git
cd level2-cv-semanticsegmentation-cv-01-lv3
```

필요한 라이브러리는 `requirements.txt`에서 설치하세요:

```bash
pip install -r requirements.txt
```

---

### 2. Training

```bash
python train.py --data_dir=./data --batch_size=8 --learning_rate=1e-6 --max_epoch=50
```

- 하이퍼파라미터는 자유롭게 조정 가능합니다!

---

### 3. Inference

```bash
python inference.py --data_dir=./data --batch_size=8
```

- 결과는 `submission.csv` 파일로 저장됩니다.

---

## 📁 Project Structure

```
level2-cv-semanticsegmentation-cv-01-lv3/
│
├── data/
│   ├── train/
│   │   ├── DCM/
│   │   └── output_json/
│   └── test/
│       └── DCM/
│
├── utils/
│   ├── dataset.py
│   ├── method.py
│   ├── augmentation.py
│   ├── handrotation.py
│   ├── hard_voting.py
│   ├── trainer.py
│   └── visualization.py
│
├── train.py
├── inference.py
├── requirements.txt
└── README.md
```

---

## 🧠 사용된 모델

본 프로젝트에서는 다양한 실험을 거쳐 **다음의 세 가지 딥러닝 기반 세분화(Semantic Segmentation) 모델**을 최종적으로 사용하였습니다:

-  **UPerNet (Unified Perceptual Parsing Network)**  
  - 다양한 레벨의 feature 정보를 효과적으로 통합하는 **Feature Pyramid 방식** 사용  
  - 복잡한 뼈 구조의 전반적 문맥 정보를 잘 포착하여 **우수한 전반 성능** 확보  

-  **UNet++**  
  - Dense Skip Connections 구조로 **디테일한 경계 추정**에 효과적  
  - 얇고 미세한 뼈 구조에 대해 높은 **정밀도와 복원력** 확보  

-  **DeepLab V3+**  
  - Atrous Spatial Pyramid Pooling(ASPP) 기반으로 **다양한 수용 영역** 반영  
  - 복잡한 배경 속에서도 뼈 구조를 잘 구분하며 **강인한 성능** 발휘  

> 각 모델은 독립적으로 학습되며, 성능 비교 및 앙상블 실험을 통해 최종 예측을 도출하였습니다.  
> 의료 영상의 특성과 뼈 구조의 복잡성을 고려하여 **모델별 장점을 상호 보완적으로 활용**하였습니다.

---

## 👥 팀원 소개

<table>
  <tr>
     <td align="center">
      <img src="https://github.com/user-attachments/assets/fc431d0d-51d5-4774-b900-67bc6a2bb2b5" width="130px;" alt="김홍주"/><br />
      <b>김홍주</b><br />
      📌 PM, Confusion Matrix 구현, UNet++, Ensemble
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/7c44b0c5-927a-4c65-8d21-8e240bcf1618" width="130px;" alt="강대민"/><br />
      <b>강대민</b><br />
      📌 DeepLabV3+, SegFormer, 실험환경 구성
    </td>
     <td align="center">
      <img src="https://github.com/user-attachments/assets/ddebfbe1-317d-4bf7-915c-524e51e5bd69" width="130px;" alt="박나영"/><br />
      <b>박나영</b><br />
      📌 Curriculum Learning
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/b17ce868-5498-4acf-8831-31829f8f7cbd" width="130px;" alt="서승환"/><br />
      <b>서승환</b><br />
      📌 UPerNet, Loss 실험, WandB Sweep 적용
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/d155ec79-8d03-45d4-b703-44a848b9b463" width="130px;" alt="이종서"/><br />
      <b>이종서</b><br />
      📌 UPerNet, Loss 실험, 후처리 실험
    </td>
     <td align="center">
      <img src="https://github.com/user-attachments/assets/9a15231a-b69d-447f-9070-f58b29ccdcec" width="130px;" alt="이한성"/><br />
      <b>이한성</b><br />
      📌 UNet++, 오분류 픽셀 시각화, 커스텀 증강 구현
    </td>
  </tr>
</table>

---
