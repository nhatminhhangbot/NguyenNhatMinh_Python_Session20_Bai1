# Chương trình in ra dòng chữ ZeroDivisionError: division by zero vì số mạng bị hạ gục được truyền vào là chuỗi 0 => công thức kda = (int(k) + int(a)) / int(d) thực hiện chia cho 0 => không hợp lệ
# Nếu xóa ShowMaker, đến lượt Chovy chương trình sẽ báo lỗi ValueError vì số mạng chết của Chovy là chuỗi "ba" => ép kiểu int("ba") => không hợp lệ
# Cách đặt tên biến ds, x, n, k, d, a vi phạm chuẩn Clean Code vì người đọc không hiểu các biến này có ý nghĩa gì => tăng nguy cơ bug khi bảo trì
# Nên đặt tên các biến bằng các từ/cụm từ đầy đủ, có ý nghĩa
# Việc tách công thức tính KDA thành một hàm riêng biệt giúp tái sử dụng, dễ bảo trì và kiểm thử, đơn giản hóa logic
# Code đúng:

tournament_stats = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills_str, deaths_str, assists_str):
    kills = int(kills_str)
    deaths = int(deaths_str)
    assists = int(assists_str)

    return (kills + assists) / deaths


def display_kda_leaderboard(player_data_list):
    print("\n--- BẢNG XẾP HẠNG KDA ---")
    for player_record in player_data_list:
        player_name, kills, deaths, assists = player_record

        try:
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {player_name} có chỉ số KDA là: {kda:.1f}")
        except ZeroDivisionError:
            print(f"Tuyển thủ {player_name}: KDA Hoàn hảo (Perfect Game)!")
        except ValueError:
            print(f"Tuyển thủ {player_name}: Lỗi dữ liệu không hợp lệ!")
    print("--- HOÀN TẤT ---")


display_kda_leaderboard(tournament_stats)
