import os
import time
import datetime
import json

# Khởi tạo dữ liệu
danh_sach_mon_an = []
danh_sach_che_do_an = []
danh_sach_thuc_don = []

# Đường dẫn file lưu trữ
file_mon_an = "mon_an.json"
file_che_do_an = "che_do_an.json"
file_thuc_don = "thuc_don.json"

# Hàm xóa màn hình
def xoa_man_hinh():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hàm hiển thị tiêu đề
def hien_thi_tieu_de():
    xoa_man_hinh()
    print("=======================================================")
    print("      CHƯƠNG TRÌNH QUẢN LÝ THỰC ĐƠN ĂN UỐNG")
    print("=======================================================")

# Hàm chuyển đổi thời gian sang chuỗi
def thoi_gian_sang_chuoi(thoi_gian):
    return datetime.datetime.fromtimestamp(thoi_gian).strftime('%d/%m/%Y %H:%M:%S')

# Hàm tìm món ăn theo mã
def tim_mon_an_theo_ma(ma):
    for i, mon_an in enumerate(danh_sach_mon_an):
        if mon_an["ma_mon_an"] == ma:
            return i
    return -1  # Không tìm thấy

# Hàm tìm chế độ ăn theo mã
def tim_che_do_an_theo_ma(ma):
    for i, che_do_an in enumerate(danh_sach_che_do_an):
        if che_do_an["ma_che_do_an"] == ma:
            return i
    return -1  # Không tìm thấy thoát chương trình

# Hàm tìm thực đơn theo mã
def tim_thuc_don_theo_ma(ma):
    for i, thuc_don in enumerate(danh_sach_thuc_don):
        if thuc_don["ma_thuc_don"] == ma:
            return i
    return -1  # Không tìm thấy

# 1. Thêm món ăn mới
def them_mon_an():
    hien_thi_tieu_de()
    print("THÊM MÓN ĂN MỚI")
    print("------------------------------------------------------")
    
    mon_an_moi = {}
    
    # Tự động tạo mã món ăn mới
    if not danh_sach_mon_an:
        mon_an_moi["ma_mon_an"] = 1001
    else:
        mon_an_moi["ma_mon_an"] = danh_sach_mon_an[-1]["ma_mon_an"] + 1
    
    print(f"Mã món ăn: {mon_an_moi['ma_mon_an']}")
    
    mon_an_moi["ten_mon_an"] = input("Tên món ăn: ")
    mon_an_moi["gia"] = float(input("Giá (VNĐ): "))
    mon_an_moi["mo_ta"] = input("Mô tả: ")
    mon_an_moi["calo"] = int(input("Calo: "))
    mon_an_moi["loai_mon_an"] = input("Loại món ăn (Khai vị, Món chính, Tráng miệng, Đồ uống): ")
    
    danh_sach_mon_an.append(mon_an_moi)
    luu_du_lieu_mon_an()
    
    print("\nĐã thêm món ăn thành công!")       
    input("Nhấn Enter để tiếp tục...")

# 2. Hiển thị danh sách món ăn
def hien_thi_danh_sach_mon_an():
    hien_thi_tieu_de()
    print("DANH SÁCH MÓN ĂN")
    print("------------------------------------------------------")
    
    if not danh_sach_mon_an:
        print("Danh sách món ăn trống!")
    else:
        print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
        print("------------------------------------------------------")
        
        for mon_an in danh_sach_mon_an:
            print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    print("\nNhấn Enter để tiếp tục...")
    input()

# 3. Cập nhật thông tin món ăn
def cap_nhat_mon_an():
    hien_thi_tieu_de()
    print("CẬP NHẬT THÔNG TIN MÓN ĂN")
    print("------------------------------------------------------")
    
    ma_mon_an = int(input("Nhập mã món ăn cần cập nhật: "))
    
    vi_tri = tim_mon_an_theo_ma(ma_mon_an)
    
    if vi_tri == -1:
        print(f"Không tìm thấy món ăn có mã {ma_mon_an}!")
    else:
        print("Thông tin món ăn hiện tại:")
        print(f"Mã: {danh_sach_mon_an[vi_tri]['ma_mon_an']}")
        print(f"Tên: {danh_sach_mon_an[vi_tri]['ten_mon_an']}")
        print(f"Giá: {danh_sach_mon_an[vi_tri]['gia']} VNĐ")
        print(f"Mô tả: {danh_sach_mon_an[vi_tri]['mo_ta']}")
        print(f"Calo: {danh_sach_mon_an[vi_tri]['calo']}")
        print(f"Loại món ăn: {danh_sach_mon_an[vi_tri]['loai_mon_an']}")
        
        print("\nNhập thông tin mới (để trống nếu không muốn thay đổi):")
        
        ten_moi = input("Tên món ăn mới: ")
        if ten_moi:
            danh_sach_mon_an[vi_tri]["ten_mon_an"] = ten_moi
        
        gia_moi = input("Giá mới (VNĐ): ")
        if gia_moi:
            danh_sach_mon_an[vi_tri]["gia"] = float(gia_moi)
        
        mo_ta_moi = input("Mô tả mới: ")
        if mo_ta_moi:
            danh_sach_mon_an[vi_tri]["mo_ta"] = mo_ta_moi
        
        calo_moi = input("Calo mới: ")
        if calo_moi:
            danh_sach_mon_an[vi_tri]["calo"] = int(calo_moi)
        
        loai_moi = input("Loại món ăn mới: ")
        if loai_moi:
            danh_sach_mon_an[vi_tri]["loai_mon_an"] = loai_moi
        
        luu_du_lieu_mon_an()
        print("\nĐã cập nhật thông tin món ăn thành công!")
    
    input("Nhấn Enter để tiếp tục...")

# 4. Xóa món ăn
def xoa_mon_an():
    hien_thi_tieu_de()
    print("XÓA MÓN ĂN")
    print("------------------------------------------------------")
    
    ma_mon_an = int(input("Nhập mã món ăn cần xóa: "))
    
    vi_tri = tim_mon_an_theo_ma(ma_mon_an)
    
    if vi_tri == -1:
        print(f"Không tìm thấy món ăn có mã {ma_mon_an}!")
    else:
        print("Thông tin món ăn cần xóa:")
        print(f"Mã: {danh_sach_mon_an[vi_tri]['ma_mon_an']}")
        print(f"Tên: {danh_sach_mon_an[vi_tri]['ten_mon_an']}")
        print(f"Giá: {danh_sach_mon_an[vi_tri]['gia']} VNĐ")
        
        xac_nhan = input("\nBạn có chắc chắn muốn xóa món ăn này? (y/n): ")
        
        if xac_nhan.lower() == 'y':
            danh_sach_mon_an.pop(vi_tri)
            luu_du_lieu_mon_an()
            print("\nĐã xóa món ăn thành công!")
        else:
            print("\nĐã hủy thao tác xóa!")
    
    input("Nhấn Enter để tiếp tục...")

# 5. Tìm kiếm món ăn theo tên
def tim_kiem_mon_an_theo_ten():
    hien_thi_tieu_de()
    print("TÌM KIẾM MÓN ĂN THEO TÊN")
    print("------------------------------------------------------")
    
    ten_can_tim = input("Nhập tên món ăn cần tìm: ").lower()
    
    ket_qua = []
    
    for mon_an in danh_sach_mon_an:
        if ten_can_tim in mon_an["ten_mon_an"].lower():
            ket_qua.append(mon_an)
    
    if not ket_qua:
        print(f"Không tìm thấy món ăn nào có tên chứa '{ten_can_tim}'!")
    else:
        print(f"Tìm thấy {len(ket_qua)} kết quả:")
        print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
        print("------------------------------------------------------")
        
        for mon_an in ket_qua:
            print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    input("\nNhấn Enter để tiếp tục...")

# 6. Thêm chế độ ăn mới
def them_che_do_an():
    hien_thi_tieu_de()
    print("THÊM CHẾ ĐỘ ĂN MỚI")
    print("------------------------------------------------------")
    
    che_do_an_moi = {}
    
    # Tự động tạo mã chế độ ăn mới
    if not danh_sach_che_do_an:
        che_do_an_moi["ma_che_do_an"] = 2001
    else:
        che_do_an_moi["ma_che_do_an"] = danh_sach_che_do_an[-1]["ma_che_do_an"] + 1
    
    print(f"Mã chế độ ăn: {che_do_an_moi['ma_che_do_an']}")
    
    che_do_an_moi["ten_che_do_an"] = input("Tên chế độ ăn: ")
    che_do_an_moi["mo_ta"] = input("Mô tả: ")
    che_do_an_moi["danh_sach_mon_an"] = []
    
    print("\nThêm món ăn vào chế độ ăn:")
    hien_thi_danh_sach_mon_an()
    
    while True:
        ma_mon_an = input("\nNhập mã món ăn cần thêm (nhập 0 để kết thúc): ")
        
        if ma_mon_an == "0":
            break
        
        ma_mon_an = int(ma_mon_an)
        vi_tri = tim_mon_an_theo_ma(ma_mon_an)
        
        if vi_tri == -1:
            print(f"Không tìm thấy món ăn có mã {ma_mon_an}!")
        else:
            if ma_mon_an in che_do_an_moi["danh_sach_mon_an"]:
                print("Món ăn này đã có trong chế độ ăn!")
            else:
                che_do_an_moi["danh_sach_mon_an"].append(ma_mon_an)
                print(f"Đã thêm món ăn '{danh_sach_mon_an[vi_tri]['ten_mon_an']}' vào chế độ ăn!")
    
    danh_sach_che_do_an.append(che_do_an_moi)
    luu_du_lieu_che_do_an()
    
    print("\nĐã thêm chế độ ăn thành công!")
    input("Nhấn Enter để tiếp tục...")

# 7. Hiển thị danh sách chế độ ăn
def hien_thi_danh_sach_che_do_an():
    hien_thi_tieu_de()
    print("DANH SÁCH CHẾ ĐỘ ĂN")
    print("------------------------------------------------------")
    
    if not danh_sach_che_do_an:
        print("Danh sách chế độ ăn trống!")
    else:
        for che_do_an in danh_sach_che_do_an:
            print(f"Mã: {che_do_an['ma_che_do_an']}")
            print(f"Tên: {che_do_an['ten_che_do_an']}")
            print(f"Mô tả: {che_do_an['mo_ta']}")
            
            print("Danh sách món ăn:")
            if not che_do_an['danh_sach_mon_an']:
                print("  Không có món ăn nào!")
            else:
                tong_calo = 0
                tong_gia = 0
                
                for ma_mon_an in che_do_an['danh_sach_mon_an']:
                    vi_tri = tim_mon_an_theo_ma(ma_mon_an)
                    if vi_tri != -1:
                        mon_an = danh_sach_mon_an[vi_tri]
                        print(f"  - {mon_an['ten_mon_an']} ({mon_an['calo']} calo, {mon_an['gia']:.0f} VNĐ)")
                        tong_calo += mon_an['calo']
                        tong_gia += mon_an['gia']
                
                print(f"Tổng calo: {tong_calo}")
                print(f"Tổng giá: {tong_gia:.0f} VNĐ")
            
            print("------------------------------------------------------")
    
    input("\nNhấn Enter để tiếp tục...")

# 8. Cập nhật thông tin chế độ ăn
def cap_nhat_che_do_an():
    hien_thi_tieu_de()
    print("CẬP NHẬT THÔNG TIN CHẾ ĐỘ ĂN")
    print("------------------------------------------------------")
    
    ma_che_do_an = int(input("Nhập mã chế độ ăn cần cập nhật: "))
    
    vi_tri = tim_che_do_an_theo_ma(ma_che_do_an)
    
    if vi_tri == -1:
        print(f"Không tìm thấy chế độ ăn có mã {ma_che_do_an}!")
    else:
        print("Thông tin chế độ ăn hiện tại:")
        print(f"Mã: {danh_sach_che_do_an[vi_tri]['ma_che_do_an']}")
        print(f"Tên: {danh_sach_che_do_an[vi_tri]['ten_che_do_an']}")
        print(f"Mô tả: {danh_sach_che_do_an[vi_tri]['mo_ta']}")
        
        print("Danh sách món ăn:")
        for ma_mon_an in danh_sach_che_do_an[vi_tri]['danh_sach_mon_an']:
            vi_tri_mon_an = tim_mon_an_theo_ma(ma_mon_an)
            if vi_tri_mon_an != -1:
                print(f"  - {danh_sach_mon_an[vi_tri_mon_an]['ten_mon_an']}")
        
        print("\nNhập thông tin mới (để trống nếu không muốn thay đổi):")
        
        ten_moi = input("Tên chế độ ăn mới: ")
        if ten_moi:
            danh_sach_che_do_an[vi_tri]["ten_che_do_an"] = ten_moi
        
        mo_ta_moi = input("Mô tả mới: ")
        if mo_ta_moi:
            danh_sach_che_do_an[vi_tri]["mo_ta"] = mo_ta_moi
        
        cap_nhat_mon_an = input("\nBạn có muốn cập nhật danh sách món ăn? (y/n): ")
        
        if cap_nhat_mon_an.lower() == 'y':
            print("\nDanh sách món ăn hiện có:")
            hien_thi_danh_sach_mon_an()
            
            danh_sach_che_do_an[vi_tri]["danh_sach_mon_an"] = []
            
            while True:
                ma_mon_an = input("\nNhập mã món ăn cần thêm (nhập 0 để kết thúc): ")
                
                if ma_mon_an == "0":
                    break
                
                ma_mon_an = int(ma_mon_an)
                vi_tri_mon_an = tim_mon_an_theo_ma(ma_mon_an)
                
                if vi_tri_mon_an == -1:
                    print(f"Không tìm thấy món ăn có mã {ma_mon_an}!")
                else:
                    if ma_mon_an in danh_sach_che_do_an[vi_tri]["danh_sach_mon_an"]:
                        print("Món ăn này đã có trong chế độ ăn!")
                    else:
                        danh_sach_che_do_an[vi_tri]["danh_sach_mon_an"].append(ma_mon_an)
                        print(f"Đã thêm món ăn '{danh_sach_mon_an[vi_tri_mon_an]['ten_mon_an']}' vào chế độ ăn!")
        
        luu_du_lieu_che_do_an()
        print("\nĐã cập nhật thông tin chế độ ăn thành công!")
    
    input("Nhấn Enter để tiếp tục...")

# 9. Xóa chế độ ăn
def xoa_che_do_an():
    hien_thi_tieu_de()
    print("XÓA CHẾ ĐỘ ĂN")
    print("------------------------------------------------------")
    
    ma_che_do_an = int(input("Nhập mã chế độ ăn cần xóa: "))
    
    vi_tri = tim_che_do_an_theo_ma(ma_che_do_an)
    
    if vi_tri == -1:
        print(f"Không tìm thấy chế độ ăn có mã {ma_che_do_an}!")
    else:
        print("Thông tin chế độ ăn cần xóa:")
        print(f"Mã: {danh_sach_che_do_an[vi_tri]['ma_che_do_an']}")
        print(f"Tên: {danh_sach_che_do_an[vi_tri]['ten_che_do_an']}")
        
        xac_nhan = input("\nBạn có chắc chắn muốn xóa chế độ ăn này? (y/n): ")
        
        if xac_nhan.lower() == 'y':
            danh_sach_che_do_an.pop(vi_tri)
            luu_du_lieu_che_do_an()
            print("\nĐã xóa chế độ ăn thành công!")
        else:
            print("\nĐã hủy thao tác xóa!")
    
    input("Nhấn Enter để tiếp tục...")

# 10. Thêm thực đơn mới
def them_thuc_don():
    hien_thi_tieu_de()
    print("THÊM THỰC ĐƠN MỚI")
    print("------------------------------------------------------")
    
    thuc_don_moi = {}
    
    # Tự động tạo mã thực đơn mới
    if not danh_sach_thuc_don:
        thuc_don_moi["ma_thuc_don"] = 3001
    else:
        thuc_don_moi["ma_thuc_don"] = danh_sach_thuc_don[-1]["ma_thuc_don"] + 1
    
    print(f"Mã thực đơn: {thuc_don_moi['ma_thuc_don']}")
    
    thuc_don_moi["ten_thuc_don"] = input("Tên thực đơn: ")
    thuc_don_moi["mo_ta"] = input("Mô tả: ")
    thuc_don_moi["danh_sach_mon_an"] = []
    thuc_don_moi["ngay_tao"] = time.time()
    
    print("\nThêm món ăn vào thực đơn:")
    hien_thi_danh_sach_mon_an()
    
    while True:
        ma_mon_an = input("\nNhập mã món ăn cần thêm (nhập 0 để kết thúc): ")
        
        if ma_mon_an == "0":
            break
        
        ma_mon_an = int(ma_mon_an)
        vi_tri = tim_mon_an_theo_ma(ma_mon_an)
        
        if vi_tri == -1:
            print(f"Không tìm thấy món ăn có mã {ma_mon_an}!")
        else:
            if ma_mon_an in thuc_don_moi["danh_sach_mon_an"]:
                print("Món ăn này đã có trong thực đơn!")
            else:
                thuc_don_moi["danh_sach_mon_an"].append(ma_mon_an)
                print(f"Đã thêm món ăn '{danh_sach_mon_an[vi_tri]['ten_mon_an']}' vào thực đơn!")
    
    danh_sach_thuc_don.append(thuc_don_moi)
    luu_du_lieu_thuc_don()
    
    print("\nĐã thêm thực đơn thành công!")
    input("Nhấn Enter để tiếp tục...")

# 11. Hiển thị danh sách thực đơn
def hien_thi_danh_sach_thuc_don():
    hien_thi_tieu_de()
    print("DANH SÁCH THỰC ĐƠN")
    print("------------------------------------------------------")
    
    if not danh_sach_thuc_don:
        print("Danh sách thực đơn trống!")
    else:
        for thuc_don in danh_sach_thuc_don:
            print(f"Mã: {thuc_don['ma_thuc_don']}")
            print(f"Tên: {thuc_don['ten_thuc_don']}")
            print(f"Mô tả: {thuc_don['mo_ta']}")
            print(f"Ngày tạo: {thoi_gian_sang_chuoi(thuc_don['ngay_tao'])}")
            
            print("Danh sách món ăn:")
            if not thuc_don['danh_sach_mon_an']:
                print("  Không có món ăn nào!")
            else:
                tong_calo = 0
                tong_gia = 0
                
                for ma_mon_an in thuc_don['danh_sach_mon_an']:
                    vi_tri = tim_mon_an_theo_ma(ma_mon_an)
                    if vi_tri != -1:
                        mon_an = danh_sach_mon_an[vi_tri]
                        print(f"  - {mon_an['ten_mon_an']} ({mon_an['calo']} calo, {mon_an['gia']:.0f} VNĐ)")
                        tong_calo += mon_an['calo']
                        tong_gia += mon_an['gia']
                
                print(f"Tổng calo: {tong_calo}")
                print(f"Tổng giá: {tong_gia:.0f} VNĐ")
            
            print("------------------------------------------------------")
    
    input("\nNhấn Enter để tiếp tục...")

# 12. Cập nhật thông tin thực đơn
def cap_nhat_thuc_don():
    hien_thi_tieu_de()
    print("CẬP NHẬT THÔNG TIN THỰC ĐƠN")
    print("------------------------------------------------------")
    
    ma_thuc_don = int(input("Nhập mã thực đơn cần cập nhật: "))
    
    vi_tri = tim_thuc_don_theo_ma(ma_thuc_don)
    
    if vi_tri == -1:
        print(f"Không tìm thấy thực đơn có mã {ma_thuc_don}!")
    else:
        print("Thông tin thực đơn hiện tại:")
        print(f"Mã: {danh_sach_thuc_don[vi_tri]['ma_thuc_don']}")
        print(f"Tên: {danh_sach_thuc_don[vi_tri]['ten_thuc_don']}")
        print(f"Mô tả: {danh_sach_thuc_don[vi_tri]['mo_ta']}")
        print(f"Ngày tạo: {thoi_gian_sang_chuoi(danh_sach_thuc_don[vi_tri]['ngay_tao'])}")
        
        print("Danh sách món ăn:")
        for ma_mon_an in danh_sach_thuc_don[vi_tri]['danh_sach_mon_an']:
            vi_tri_mon_an = tim_mon_an_theo_ma(ma_mon_an)
            if vi_tri_mon_an != -1:
                print(f"  - {danh_sach_mon_an[vi_tri_mon_an]['ten_mon_an']}")
        
        print("\nNhập thông tin mới (để trống nếu không muốn thay đổi):")
        
        ten_moi = input("Tên thực đơn mới: ")
        if ten_moi:
            danh_sach_thuc_don[vi_tri]["ten_thuc_don"] = ten_moi
        
        mo_ta_moi = input("Mô tả mới: ")
        if mo_ta_moi:
            danh_sach_thuc_don[vi_tri]["mo_ta"] = mo_ta_moi
        
        cap_nhat_mon_an = input("\nBạn có muốn cập nhật danh sách món ăn? (y/n): ")
        
        if cap_nhat_mon_an.lower() == 'y':
            print("\nDanh sách món ăn hiện có:")
            hien_thi_danh_sach_mon_an()
            
            danh_sach_thuc_don[vi_tri]["danh_sach_mon_an"] = []
            
            while True:
                ma_mon_an = input("\nNhập mã món ăn cần thêm (nhập 0 để kết thúc): ")
                
                if ma_mon_an == "0":
                    break
                
                ma_mon_an = int(ma_mon_an)
                vi_tri_mon_an = tim_mon_an_theo_ma(ma_mon_an)
                
                if vi_tri_mon_an == -1:
                    print(f"Không tìm thấy món ăn có mã {ma_mon_an}!")
                else:
                    if ma_mon_an in danh_sach_thuc_don[vi_tri]["danh_sach_mon_an"]:
                        print("Món ăn này đã có trong thực đơn!")
                    else:
                        danh_sach_thuc_don[vi_tri]["danh_sach_mon_an"].append(ma_mon_an)
                        print(f"Đã thêm món ăn '{danh_sach_mon_an[vi_tri_mon_an]['ten_mon_an']}' vào thực đơn!")
        
        luu_du_lieu_thuc_don()
        print("\nĐã cập nhật thông tin thực đơn thành công!")
    
    input("Nhấn Enter để tiếp tục...")

# 13. Xóa thực đơn
def xoa_thuc_don():
    hien_thi_tieu_de()
    print("XÓA THỰC ĐƠN")
    print("------------------------------------------------------")
    
    ma_thuc_don = int(input("Nhập mã thực đơn cần xóa: "))
    
    vi_tri = tim_thuc_don_theo_ma(ma_thuc_don)
    
    if vi_tri == -1:
        print(f"Không tìm thấy thực đơn có mã {ma_thuc_don}!")
    else:
        print("Thông tin thực đơn cần xóa:")
        print(f"Mã: {danh_sach_thuc_don[vi_tri]['ma_thuc_don']}")
        print(f"Tên: {danh_sach_thuc_don[vi_tri]['ten_thuc_don']}")
        
        xac_nhan = input("\nBạn có chắc chắn muốn xóa thực đơn này? (y/n): ")
        
        if xac_nhan.lower() == 'y':
            danh_sach_thuc_don.pop(vi_tri)
            luu_du_lieu_thuc_don()
            print("\nĐã xóa thực đơn thành công!")
        else:
            print("\nĐã hủy thao tác xóa!")
    
    input("Nhấn Enter để tiếp tục...")

# 14. Tìm kiếm món ăn theo loại
def tim_kiem_mon_an_theo_loai():
    hien_thi_tieu_de()
    print("TÌM KIẾM MÓN ĂN THEO LOẠI")
    print("------------------------------------------------------")
    
    loai_can_tim = input("Nhập loại món ăn cần tìm: ").lower()
    
    ket_qua = []
    
    for mon_an in danh_sach_mon_an:
        if loai_can_tim in mon_an["loai_mon_an"].lower():
            ket_qua.append(mon_an)
    
    if not ket_qua:
        print(f"Không tìm thấy món ăn nào thuộc loại '{loai_can_tim}'!")
    else:
        print(f"Tìm thấy {len(ket_qua)} kết quả:")
        print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
        print("------------------------------------------------------")
        
        for mon_an in ket_qua:
            print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    input("\nNhấn Enter để tiếp tục...")

# 15. Tìm kiếm món ăn theo khoảng giá
def tim_kiem_mon_an_theo_gia():
    hien_thi_tieu_de()
    print("TÌM KIẾM MÓN ĂN THEO KHOẢNG GIÁ")
    print("------------------------------------------------------")
    
    gia_min = float(input("Nhập giá tối thiểu (VNĐ): "))
    gia_max = float(input("Nhập giá tối đa (VNĐ): "))
    
    ket_qua = []
    
    for mon_an in danh_sach_mon_an:
        if gia_min <= mon_an["gia"] <= gia_max:
            ket_qua.append(mon_an)
    
    if not ket_qua:
        print(f"Không tìm thấy món ăn nào trong khoảng giá từ {gia_min:.0f} đến {gia_max:.0f} VNĐ!")
    else:
        print(f"Tìm thấy {len(ket_qua)} kết quả:")
        print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
        print("------------------------------------------------------")
        
        for mon_an in ket_qua:
            print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    input("\nNhấn Enter để tiếp tục...")

# 16. Tìm kiếm món ăn theo khoảng calo
def tim_kiem_mon_an_theo_calo():
    hien_thi_tieu_de()
    print("TÌM KIẾM MÓN ĂN THEO KHOẢNG CALO")
    print("------------------------------------------------------")
    
    calo_min = int(input("Nhập calo tối thiểu: "))
    calo_max = int(input("Nhập calo tối đa: "))
    
    ket_qua = []
    
    for mon_an in danh_sach_mon_an:
        if calo_min <= mon_an["calo"] <= calo_max:
            ket_qua.append(mon_an)
    
    if not ket_qua:
        print(f"Không tìm thấy món ăn nào trong khoảng calo từ {calo_min} đến {calo_max}!")
    else:
        print(f"Tìm thấy {len(ket_qua)} kết quả:")
        print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
        print("------------------------------------------------------")
        
        for mon_an in ket_qua:
            print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    input("\nNhấn Enter để tiếp tục...")

# 17. Sắp xếp món ăn theo giá
def sap_xep_mon_an_theo_gia():
    hien_thi_tieu_de()
    print("SẮP XẾP MÓN ĂN THEO GIÁ")
    print("------------------------------------------------------")
    
    thu_tu = input("Chọn thứ tự sắp xếp (1: Tăng dần, 2: Giảm dần): ")
    
    if thu_tu == "1":
        danh_sach_mon_an.sort(key=lambda x: x["gia"])
        print("Đã sắp xếp món ăn theo giá tăng dần!")
    else:
        danh_sach_mon_an.sort(key=lambda x: x["gia"], reverse=True)
        print("Đã sắp xếp món ăn theo giá giảm dần!")
    
    print("\nDanh sách món ăn sau khi sắp xếp:")
    print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
    print("------------------------------------------------------")
    
    for mon_an in danh_sach_mon_an:
        print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    luu_du_lieu_mon_an()
    input("\nNhấn Enter để tiếp tục...")

# 18. Sắp xếp món ăn theo calo
def sap_xep_mon_an_theo_calo():
    hien_thi_tieu_de()
    print("SẮP XẾP MÓN ĂN THEO CALO")
    print("------------------------------------------------------")
    
    thu_tu = input("Chọn thứ tự sắp xếp (1: Tăng dần, 2: Giảm dần): ")
    
    if thu_tu == "1":
        danh_sach_mon_an.sort(key=lambda x: x["calo"])
        print("Đã sắp xếp món ăn theo calo tăng dần!")
    else:
        danh_sach_mon_an.sort(key=lambda x: x["calo"], reverse=True)
        print("Đã sắp xếp món ăn theo calo giảm dần!")
    
    print("\nDanh sách món ăn sau khi sắp xếp:")
    print(f"{'Mã':<10}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}")
    print("------------------------------------------------------")
    
    for mon_an in danh_sach_mon_an:
        print(f"{mon_an['ma_mon_an']:<10}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}")
    
    luu_du_lieu_mon_an()
    input("\nNhấn Enter để tiếp tục...")

# 19. Thống kê món ăn theo loại
def thong_ke_mon_an_theo_loai():
    hien_thi_tieu_de()
    print("THỐNG KÊ MÓN ĂN THEO LOẠI")
    print("------------------------------------------------------")
    
    thong_ke = {}
    
    for mon_an in danh_sach_mon_an:
        loai = mon_an["loai_mon_an"]
        if loai in thong_ke:
            thong_ke[loai] += 1
        else:
            thong_ke[loai] = 1
    
    if not thong_ke:
        print("Không có dữ liệu để thống kê!")
    else:
        print(f"{'Loại món ăn':<30}{'Số lượng':<10}")
        print("------------------------------------------------------")
        
        for loai, so_luong in thong_ke.items():
            print(f"{loai:<30}{so_luong:<10}")
    
    input("\nNhấn Enter để tiếp tục...")

# 20. Xuất thực đơn ra file
def xuat_thuc_don_ra_file():
    hien_thi_tieu_de()
    print("XUẤT THỰC ĐƠN RA FILE")
    print("------------------------------------------------------")
    
    if not danh_sach_thuc_don:
        print("Danh sách thực đơn trống!")
        input("\nNhấn Enter để tiếp tục...")
        return
    
    print("Danh sách thực đơn:")
    for i, thuc_don in enumerate(danh_sach_thuc_don):
        print(f"{i+1}. {thuc_don['ten_thuc_don']} (Mã: {thuc_don['ma_thuc_don']})")
    
    chon = int(input("\nChọn thực đơn cần xuất (nhập số thứ tự): ")) - 1
    
    if chon < 0 or chon >= len(danh_sach_thuc_don):
        print("Lựa chọn không hợp lệ!")
    else:
        thuc_don = danh_sach_thuc_don[chon]
        ten_file = f"thuc_don_{thuc_don['ma_thuc_don']}.txt"
        
        with open(ten_file, "w", encoding="utf-8") as f:
            f.write(f"THỰC ĐƠN: {thuc_don['ten_thuc_don']}\n")
            f.write(f"Mã thực đơn: {thuc_don['ma_thuc_don']}\n")
            f.write(f"Mô tả: {thuc_don['mo_ta']}\n")
            f.write(f"Ngày tạo: {thoi_gian_sang_chuoi(thuc_don['ngay_tao'])}\n\n")
            
            f.write("DANH SÁCH MÓN ĂN:\n")
            f.write(f"{'STT':<5}{'Tên món ăn':<30}{'Giá (VNĐ)':<15}{'Calo':<10}{'Loại món ăn':<15}\n")
            f.write("-" * 75 + "\n")
            
            tong_calo = 0
            tong_gia = 0
            
            for i, ma_mon_an in enumerate(thuc_don['danh_sach_mon_an']):
                vi_tri = tim_mon_an_theo_ma(ma_mon_an)
                if vi_tri != -1:
                    mon_an = danh_sach_mon_an[vi_tri]
                    f.write(f"{i+1:<5}{mon_an['ten_mon_an']:<30}{mon_an['gia']:<15.0f}{mon_an['calo']:<10}{mon_an['loai_mon_an']:<15}\n")
                    tong_calo += mon_an['calo']
                    tong_gia += mon_an['gia']
            
            f.write("-" * 75 + "\n")
            f.write(f"Tổng calo: {tong_calo}\n")
            f.write(f"Tổng giá: {tong_gia:.0f} VNĐ\n")
        
        print(f"\nĐã xuất thực đơn ra file '{ten_file}' thành công!")
    
    input("\nNhấn Enter để tiếp tục...")

# Hàm lưu dữ liệu món ăn
def luu_du_lieu_mon_an():
    with open(file_mon_an, "w", encoding="utf-8") as f:
        json.dump(danh_sach_mon_an, f, ensure_ascii=False, indent=4)

# Hàm lưu dữ liệu chế độ ăn
def luu_du_lieu_che_do_an():
    with open(file_che_do_an, "w", encoding="utf-8") as f:
        json.dump(danh_sach_che_do_an, f, ensure_ascii=False, indent=4)

# Hàm lưu dữ liệu thực đơn
def luu_du_lieu_thuc_don():
    with open(file_thuc_don, "w", encoding="utf-8") as f:
        json.dump(danh_sach_thuc_don, f, ensure_ascii=False, indent=4)

# Hàm tải dữ liệu món ăn
def tai_du_lieu_mon_an():
    global danh_sach_mon_an
    try:
        with open(file_mon_an, "r", encoding="utf-8") as f:
            danh_sach_mon_an = json.load(f)
    except FileNotFoundError:
        danh_sach_mon_an = []

# Hàm tải dữ liệu chế độ ăn
def tai_du_lieu_che_do_an():
    global danh_sach_che_do_an
    try:
        with open(file_che_do_an, "r", encoding="utf-8") as f:
            danh_sach_che_do_an = json.load(f)
    except FileNotFoundError:
        danh_sach_che_do_an = []

# Hàm tải dữ liệu thực đơn
def tai_du_lieu_thuc_don():
    global danh_sach_thuc_don
    try:
        with open(file_thuc_don, "r", encoding="utf-8") as f:
            danh_sach_thuc_don = json.load(f)
    except FileNotFoundError:
        danh_sach_thuc_don = []

# Hàm hiển thị menu chính
def hien_thi_menu_chinh():
    hien_thi_tieu_de()
    print("MENU CHÍNH")
    print("------------------------------------------------------")
    print("1. Quản lý món ăn")
    print("2. Quản lý chế độ ăn")
    print("3. Quản lý thực đơn")
    print("4. Tìm kiếm và thống kê")
    print("0. Thoát chương trình")
    print("------------------------------------------------------")
    
    lua_chon = input("Nhập lựa chọn của bạn: ")
    return lua_chon

# Hàm hiển thị menu quản lý món ăn
def hien_thi_menu_quan_ly_mon_an():
    hien_thi_tieu_de()
    print("QUẢN LÝ MÓN ĂN")
    print("------------------------------------------------------")
    print("1. Thêm món ăn mới")
    print("2. Hiển thị danh sách món ăn")
    print("3. Cập nhật thông tin món ăn")
    print("4. Xóa món ăn")
    print("5. Sắp xếp món ăn theo giá")
    print("6. Sắp xếp món ăn theo calo")
    print("0. Quay lại menu chính")
    print("------------------------------------------------------")
    
    lua_chon = input("Nhập lựa chọn của bạn: ")
    return lua_chon

# Hàm hiển thị menu quản lý chế độ ăn
def hien_thi_menu_quan_ly_che_do_an():
    hien_thi_tieu_de()
    print("QUẢN LÝ CHẾ ĐỘ ĂN")
    print("------------------------------------------------------")
    print("1. Thêm chế độ ăn mới")
    print("2. Hiển thị danh sách chế độ ăn")
    print("3. Cập nhật thông tin chế độ ăn")
    print("4. Xóa chế độ ăn")
    print("0. Quay lại menu chính")
    print("------------------------------------------------------")
    
    lua_chon = input("Nhập lựa chọn của bạn: ")
    return lua_chon

# Hàm hiển thị menu quản lý thực đơn
def hien_thi_menu_quan_ly_thuc_don():
    hien_thi_tieu_de()
    print("QUẢN LÝ THỰC ĐƠN")
    print("------------------------------------------------------")
    print("1. Thêm thực đơn mới")
    print("2. Hiển thị danh sách thực đơn")
    print("3. Cập nhật thông tin thực đơn")
    print("4. Xóa thực đơn")
    print("5. Xuất thực đơn ra file")
    print("0. Quay lại menu chính")
    print("------------------------------------------------------")
    
    lua_chon = input("Nhập lựa chọn của bạn: ")
    return lua_chon

# Hàm hiển thị menu tìm kiếm và thống kê
def hien_thi_menu_tim_kiem_thong_ke():
    hien_thi_tieu_de()
    print("TÌM KIẾM VÀ THỐNG KÊ")
    print("------------------------------------------------------")
    print("1. Tìm kiếm món ăn theo tên")
    print("2. Tìm kiếm món ăn theo loại")
    print("3. Tìm kiếm món ăn theo khoảng giá")
    print("4. Tìm kiếm món ăn theo khoảng calo")
    print("5. Thống kê món ăn theo loại")
    print("0. Quay lại menu chính")
    print("------------------------------------------------------")
    
    lua_chon = input("Nhập lựa chọn của bạn: ")
    return lua_chon

# Hàm chính
def main():
    # Tải dữ liệu từ file
    tai_du_lieu_mon_an()
    tai_du_lieu_che_do_an()
    tai_du_lieu_thuc_don()
    
    while True:
        lua_chon = hien_thi_menu_chinh()
        
        if lua_chon == "1":  # Quản lý món ăn
            while True:
                lua_chon_mon_an = hien_thi_menu_quan_ly_mon_an()
                
                if lua_chon_mon_an == "1":
                    them_mon_an()
                elif lua_chon_mon_an == "2":
                    hien_thi_danh_sach_mon_an()
                elif lua_chon_mon_an == "3":
                    cap_nhat_mon_an()
                elif lua_chon_mon_an == "4":
                    xoa_mon_an()
                elif lua_chon_mon_an == "5":
                    sap_xep_mon_an_theo_gia()
                elif lua_chon_mon_an == "6":
                    sap_xep_mon_an_theo_calo()
                elif lua_chon_mon_an == "0":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")
                    input("Nhấn Enter để tiếp tục...")
        
        elif lua_chon == "2":  # Quản lý chế độ ăn
            while True:
                lua_chon_che_do_an = hien_thi_menu_quan_ly_che_do_an()
                
                if lua_chon_che_do_an == "1":
                    them_che_do_an()
                elif lua_chon_che_do_an == "2":
                    hien_thi_danh_sach_che_do_an()
                elif lua_chon_che_do_an == "3":
                    cap_nhat_che_do_an()
                elif lua_chon_che_do_an == "4":
                    xoa_che_do_an()
                elif lua_chon_che_do_an == "0":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")
                    input("Nhấn Enter để tiếp tục...")
        
        elif lua_chon == "3":  # Quản lý thực đơn
            while True:
                lua_chon_thuc_don = hien_thi_menu_quan_ly_thuc_don()
                
                if lua_chon_thuc_don == "1":
                    them_thuc_don()
                elif lua_chon_thuc_don == "2":
                    hien_thi_danh_sach_thuc_don()
                elif lua_chon_thuc_don == "3":
                    cap_nhat_thuc_don()
                elif lua_chon_thuc_don == "4":
                    xoa_thuc_don()
                elif lua_chon_thuc_don == "5":
                    xuat_thuc_don_ra_file()
                elif lua_chon_thuc_don == "0":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")
                    input("Nhấn Enter để tiếp tục...")
        
        elif lua_chon == "4":  # Tìm kiếm và thống kê
            while True:
                lua_chon_tim_kiem = hien_thi_menu_tim_kiem_thong_ke()
                
                if lua_chon_tim_kiem == "1":
                    tim_kiem_mon_an_theo_ten()
                elif lua_chon_tim_kiem == "2":
                    tim_kiem_mon_an_theo_loai()
                elif lua_chon_tim_kiem == "3":
                    tim_kiem_mon_an_theo_gia()
                elif lua_chon_tim_kiem == "4":
                    tim_kiem_mon_an_theo_calo()
                elif lua_chon_tim_kiem == "5":
                    thong_ke_mon_an_theo_loai()
                elif lua_chon_tim_kiem == "0":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")
                    input("Nhấn Enter để tiếp tục...")
        
        elif lua_chon == "0":  # Thoát chương trình
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        
        else:
            print("Lựa chọn không hợp lệ!")
            input("Nhấn Enter để tiếp tục...")

# Chạy chương trình
if __name__ == "__main__":
    main()