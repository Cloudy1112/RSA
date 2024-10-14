import os

def find_word_files(starting_directory):
    word_files = []
    
    # Duyệt qua các thư mục và tệp
    for dirpath, _, filenames in os.walk(starting_directory):
        for filename in filenames:
            # Kiểm tra các tệp có đuôi .docx
            if filename.lower().endswith('.docx'):
                # Thêm đường dẫn đầy đủ của tệp vào danh sách
                full_path = os.path.join(dirpath, filename)
                word_files.append(full_path)
    
    return word_files

# Thư mục bắt đầu tìm kiếm - Thay đổi đường dẫn theo nhu cầu của bạn
starting_directory = "C:\\"  # Để tìm trong toàn bộ ổ đĩa C, hoặc có thể là "D:\\folder" tùy vào ổ đĩa hoặc thư mục cụ thể

# Gọi hàm để tìm các tệp Word
word_files = find_word_files(starting_directory)

# Xuất ra các tệp đã tìm thấy
if word_files:
    print("Các tệp Word (.docx) được tìm thấy:")
    for file in word_files:
        print(file)
else:
    print("Không tìm thấy tệp Word nào trong thư mục được chỉ định.")

path =os.path.dirname(os.path.abspath(__file__)) + "/word_files_list.txt" #đường dẫn đến thư mục

    # Lưu kết quả vào một tệp văn bản
with open(path, "w") as f:
    for file in word_files:
        f.write(file + "\n")
    print("Đã lưu danh sách tệp Word vào 'word_files_list.txt'.")

