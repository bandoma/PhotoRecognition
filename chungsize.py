import cv2
import os

def resize_image(image, target_size):
    """
    Chuyển đổi kích thước ảnh đến kích thước mục tiêu.
    Args:
        image (ndarray): Ảnh ban đầu.
        target_size (tuple): Kích thước mục tiêu (width, height).
    Returns:
        ndarray: Ảnh sau khi được chuyển đổi kích thước.
    """
    resized_image = cv2.resize(image, target_size)
    return resized_image

# Đường dẫn đến thư mục chứa ảnh
folder_path = "D:/CuongHalovi/TestImage/ResizedImages"

# Kích thước mục tiêu cho các ảnh
target_size = (128,128)  # Đặt kích thước mục tiêu của bạn tại đây

# Lấy danh sách tất cả các tệp tin trong thư mục ảnh "chualinhung"
chualinhung_path = os.path.join(folder_path, "chualinhung")
chualinhung_files = os.listdir(chualinhung_path)

# Lấy danh sách tất cả các tệp tin trong thư mục ảnh "hienvat"
hienvat_path = os.path.join(folder_path, "hienvat")
hienvat_files = os.listdir(hienvat_path)
#lấy danh sách tất cả các tệp tin trong thư mục ảnh "banahill"
banahill_path= os.path.join(folder_path, "banahill")
banahill_files=os.listdir(banahill_path)

#lấy danh sách tất cả các tệp tin trong thư mục  ảnh "caurong"
caurong_path= os.path.join(folder_path, "caurong")
caurong_files=os.listdir(caurong_path)
# Tạo thư mục đầu ra
output_path = "D:/CuongHalovi/TestImage/thaydoikichthuoc"
os.makedirs(output_path, exist_ok=True)

# Chuyển đổi kích thước các ảnh trong thư mục "chualinhung" và lưu vào thư mục đầu ra
for file_name in chualinhung_files:
    file_path = os.path.join(chualinhung_path, file_name)
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    resized_image = resize_image(image, target_size)
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, resized_image)

# Chuyển đổi kích thước các ảnh trong thư mục "hienvat" và lưu vào thư mục đầu ra
for file_name in hienvat_files:
    file_path = os.path.join(hienvat_path, file_name)
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    resized_image = resize_image(image, target_size)
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, resized_image)
#banahill
for file_name in banahill_files:
    file_path = os.path.join(banahill_path, file_name)
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    resized_image = resize_image(image, target_size)
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, resized_image)

#caurong
for file_name in caurong_files:
    file_path = os.path.join(caurong_path, file_name)
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    resized_image = resize_image(image, target_size)
    output_file_path = os.path.join(output_path, file_name)
    cv2.imwrite(output_file_path, resized_image)