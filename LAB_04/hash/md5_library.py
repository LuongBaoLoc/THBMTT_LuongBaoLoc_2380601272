import hashlib

def calculate_md5_hash(data):
    # Khởi tạo đối tượng md5 từ thư viện hashlib
    md5_hash = hashlib.md5()
    
    # Cập nhật dữ liệu (cần chuyển chuỗi sang định dạng bytes bằng encode)
    md5_hash.update(data.encode('utf-8'))
    
    # Trả về kết quả dưới dạng chuỗi thập lục phân (hexadecimal)
    return md5_hash.hexdigest()

def main():
    # Nhập chuỗi từ bàn phím
    input_string = input("Nhập chuỗi cần băm: ")
    
    # Gọi hàm tính toán
    result = calculate_md5_hash(input_string)
    
    # In kết quả ra màn hình
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {result}")

if __name__ == "__main__":
    main()