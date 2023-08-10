import os
import cv2
import numpy as np

# Đường dẫn đến thư mục chứa ảnh gốc
input_folder = "cuong"

# Đường dẫn đến thư mục để lưu ảnh đã tăng cường
output_folder = "ResizedImages"

# Kiểm tra xem thư mục đầu vào có tồn tại không
if not os.path.exists(input_folder):
    print("Thư mục đầu vào không tồn tại")
    exit()

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lặp qua tất cả các tệp tin trong thư mục đầu vào
for filename in os.listdir(input_folder):
    input_image_path = os.path.join(input_folder, filename)
    output_image_path = os.path.join(output_folder, filename)

    # Đọc ảnh gốc
    image = cv2.imread(input_image_path)

    # Kiểm tra xem ảnh có tồn tại không
    if image is None:
        print(f"Không thể đọc ảnh {input_image_path}")
        continue

    # Tạo danh sách chứa các biến đổi để tăng cường dữ liệu
    transformations = [
        lambda img: cv2.flip(img, 0),  # Lật ảnh theo chiều ngang
        lambda img: cv2.flip(img, 1),  # Lật ảnh theo chiều dọc
        cv2.transpose,  # Chuyển vị ảnh
        lambda img: cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE),  # Xoay ảnh 90 độ theo chiều kim đồng hồ
        lambda img: cv2.rotate(img, cv2.ROTATE_180),  # Xoay ảnh 180 độ theo chiều kim đồng hồ
        lambda img: cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE),  # Xoay ảnh 270 độ theo chiều kim đồng hồ
        lambda img: cv2.GaussianBlur(img, (5, 5), 0),  # Làm mờ ảnh bằng Gaussian Blur
                                                        # Thay đổi kích thước ảnh
        lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Thay đổi không gian màu
    ]

    # Lặp qua danh sách các biến đổi và tạo ra các ảnh mới
    for i, transform in enumerate(transformations):
        transformed_image = transform(image)
        output_image_path_augmented = f"{output_image_path}{i+1}.jpg"
        cv2.imwrite(output_image_path_augmented, transformed_image)

        print(f"Ảnh mới được lưu tại {output_image_path_augmented}")