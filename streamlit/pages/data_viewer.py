import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import numpy as np
from utils.data_loader import DataLoader
from utils.mask_generator import MaskGenerator
from utils.visualization import Visualizer

st.title("데이터 뷰어 📊")

def get_image_pairs(image_files):
    """폴더별로 이미지 쌍을 찾아서 반환하는 함수"""
    pairs = {}
    for file in image_files:
        # 파일의 디렉토리 경로와 파일명을 분리
        dir_path = os.path.dirname(file)
        file_name = os.path.basename(file)
        
        # 같은 폴더에 있는 파일들을 쌍으로 묶음
        if dir_path not in pairs:
            pairs[dir_path] = {'L': None, 'R': None}
        
        # 파일명에 따라 L/R 구분
        # 예시: 첫 번째 파일을 L, 두 번째 파일을 R로 지정
        if pairs[dir_path]['L'] is None:
            pairs[dir_path]['L'] = file
        else:
            pairs[dir_path]['R'] = file
            
    # L과 R 이미지가 모두 있는 쌍만 반환
    return {k: v for k, v in pairs.items() if v['L'] is not None and v['R'] is not None}

def main():
    # 데이터 로더 초기화
    data_loader = DataLoader("../data/")
    
    # 이미지 파일 목록 가져오기
    image_files = data_loader.get_image_list()
    
    # 이미지 쌍 찾기
    image_pairs = get_image_pairs(image_files)
    
    # 이미지 쌍 선택
    selected_pair = st.selectbox("이미지 쌍 선택", list(image_pairs.keys()))
    
    if selected_pair:
        # Left, Right 이미지를 나란히 표시하기 위한 컬럼 생성
        col1, col2 = st.columns(2)
        
        # Left 이미지 처리
        with col1:
            st.subheader("Left Image")
            image_l = data_loader.load_image(image_pairs[selected_pair]['L'])
            json_path_l = data_loader.get_json_path(image_pairs[selected_pair]['L'])
            
            if os.path.exists(json_path_l):
                json_data_l = data_loader.load_json(json_path_l)
                mask_l = MaskGenerator.create_mask_from_json(json_data_l, np.array(image_l).shape)
                rgb_mask_l = MaskGenerator.mask_to_rgb(mask_l)
                Visualizer.display_image_and_mask(image_l, rgb_mask_l)
            else:
                st.error("Left 이미지의 어노테이션 파일을 찾을 수 없습니다.")
        
        # Right 이미지 처리
        with col2:
            st.subheader("Right Image")
            image_r = data_loader.load_image(image_pairs[selected_pair]['R'])
            json_path_r = data_loader.get_json_path(image_pairs[selected_pair]['R'])
            
            if os.path.exists(json_path_r):
                json_data_r = data_loader.load_json(json_path_r)
                mask_r = MaskGenerator.create_mask_from_json(json_data_r, np.array(image_r).shape)
                rgb_mask_r = MaskGenerator.mask_to_rgb(mask_r)
                Visualizer.display_image_and_mask(image_r, rgb_mask_r)
            else:
                st.error("Right 이미지의 어노테이션 파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    main()