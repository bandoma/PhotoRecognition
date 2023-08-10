import os
import csv
from sklearn.model_selection import train_test_split

# Đường dẫn đến thư mục chứa ảnh
folder_path = "D:/CuongHalovi/TestImage/cuong"

# Tạo hàm để chuyển đổi đường dẫn
def convert_path(path):
    return "cuong" + path.replace(folder_path, "").replace("\\", "/")

# Tỷ lệ train, test và val (6:2:2)
train_ratio = 0.8
test_ratio = 0.1
val_ratio = 0.1

# Lấy danh sách tất cả các tệp tin trong thư mục ảnh "chualinhung"
chualinhung_path = os.path.join(folder_path, "chualinhung")
chualinhung_files = os.listdir(chualinhung_path)

# Lấy danh sách tất cả các tệp tin trong thư mục ảnh "hienvat"
hienvat_path = os.path.join(folder_path, "hienvat")
hienvat_files = os.listdir(hienvat_path)

# Lấy danh sách tất cả các tệp tin trong thư mục ảnh "banahill"
banahill_path = os.path.join(folder_path, "banahill")
banahill_files = os.listdir(banahill_path)

# Lấy danh sách tất cả các tệp tin trong thư mục ảnh "caurong"
caurong_path = os.path.join(folder_path, "caurong")
caurong_files = os.listdir(caurong_path)

# Chia dữ liệu "chualinhung" thành train và (test + val)
chualinhung_train_files, chualinhung_test_val_files = train_test_split(chualinhung_files, test_size=(test_ratio + val_ratio), random_state=42)

# Chia dữ liệu "hienvat" thành train và (test + val)
hienvat_train_files, hienvat_test_val_files = train_test_split(hienvat_files, test_size=(test_ratio + val_ratio), random_state=42)

# chia dữ liệu "banahill" thành train và (test + val)
banahill_train_files,banahill_test_val_files = train_test_split(banahill_files,test_size=(test_ratio + val_ratio), random_state=42)

#chia dữ liệu "caurong" thành train và (test + val)
caurong_train_files,caurong_test_val_files = train_test_split(caurong_files,test_size=(test_ratio + val_ratio), random_state=42)


# Chia dữ liệu test_val của "chualinhung" thành test và val
chualinhung_test_files, chualinhung_val_files = train_test_split(chualinhung_test_val_files, test_size=(val_ratio / (test_ratio + val_ratio)), random_state=42)

# Chia dữ liệu test_val của "hienvat" thành test và val
hienvat_test_files, hienvat_val_files = train_test_split(hienvat_test_val_files, test_size=(val_ratio / (test_ratio + val_ratio)), random_state=42)

#chia dữ liệu test_val của "banahill" thành test và val
banahill_test_files,banahill_val_files=train_test_split(banahill_test_val_files,test_size=(val_ratio / (test_ratio + val_ratio)), random_state=42)

#chia dữ liệu test_val của "caurong" thành test và val
caurong_test_files,caurong_val_files=train_test_split(caurong_test_val_files,test_size=(val_ratio / (test_ratio + val_ratio)), random_state=42)

# Hàm ghi vào tệp tin CSV
def write_to_csv(file_paths, csv_file):
    writer = csv.writer(csv_file)
    writer.writerow(["path", "label"])  # Ghi hàng đầu tiên cho tiêu đề cột
    for file_path, label in file_paths:
        converted_path = convert_path(file_path)
        writer.writerow([converted_path, label])

# Ghi đường dẫn và nhãn vào tệp tin train.csv
with open("train.csv", 'w', newline='') as train_csv:
    write_to_csv([(os.path.join(chualinhung_path, path), "chualinhung") for path in chualinhung_train_files] + [(os.path.join(hienvat_path, path), "hienvat") for path in hienvat_train_files] + [(os.path.join(banahill_path,path),"banahill") for path in banahill_train_files]+ [(os.path.join(caurong_path, path), "caurong") for path in caurong_train_files], train_csv)

# Ghi đường dẫn và nhãn vào tệp tin test.csv
with open("test.csv", 'w', newline='') as test_csv:
    write_to_csv([(os.path.join(chualinhung_path, path), "chualinhung") for path in chualinhung_test_files] + [(os.path.join(hienvat_path, path), "hienvat") for path in hienvat_test_files] + [(os.path.join(banahill_path,path),"banahill") for path in banahill_test_files]+ [(os.path.join(caurong_path,path),"caurong") for path in caurong_test_files], test_csv)

# Ghi đường dẫn và nhãn vào tệp tin val.csv
with open("val.csv", 'w', newline='') as val_csv:
    write_to_csv([(os.path.join(chualinhung_path, path), "chualinhung") for path in chualinhung_val_files] + [(os.path.join(hienvat_path, path), "hienvat") for path in hienvat_val_files] + [(os.path.join(banahill_path,path),"banahill") for path in banahill_val_files]+ [(os.path.join(caurong_path,path),"caurong") for path in caurong_val_files], val_csv)
