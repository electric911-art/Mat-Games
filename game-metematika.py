import random
import time
import os
from colorama import init, Fore, Back, Style

# Inisialisasi colorama
init(autoreset=True)

class MultiplicationGame:
    def __init__(self):
        self.username = ""
        self.score = 0
        self.streak = 0
        self.best_streak = 0
        self.attempts = 0
        self.correct_answers = 0
        self.multiplication_table = {}
        self.generate_multiplication_table()
    
    def clear_screen(self):
        """Membersihkan layar konsol"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generate_multiplication_table(self):
        """Membuat tabel perkalian 1-10"""
        for i in range(1, 11):
            for j in range(1, 11):
                self.multiplication_table[(i, j)] = i * j
    
    def print_welcome(self):
        """Menampilkan pesan selamat datang"""
        self.clear_screen()
        print(Fore.CYAN + r"""
  __  __       _ _   _ _       _           _   _             
 |  \/  |_   _| | |_(_) | __ _| |      ___| |_(_)_ __   __ _ 
 | |\/| | | | | | __| | |/ _` | |     / __| __| | '_ \ / _` |
 | |  | | |_| | | |_| | | (_| | |     \__ \ |_| | | | | (_| |
 |_|  |_|\__,_|_|\__|_|_|\__,_|_|     |___/\__|_|_| |_|\__, |
                                                       |___/ 
        """)
        print(Fore.YELLOW + "Selamat datang di Game Hafal Perkalian!")
        print(Fore.YELLOW + "Program ini akan membantumu menghafal perkalian dengan cara yang menyenangkan!\n")
    
    def get_username(self):
        """Meminta nama pengguna"""
        print(Fore.GREEN + "Halo! Siapa namamu?")
        self.username = input(Fore.WHITE + "> ").strip()
        if not self.username:
            self.username = "Teman"
        print(Fore.GREEN + f"\nHalo, {self.username}! Mari kita belajar perkalian bersama!\n")
        time.sleep(1)
        self.clear_screen()
    
    def show_main_menu(self):
        """Menampilkan menu utama"""
        while True:
            self.clear_screen()
            print(Fore.MAGENTA + "\n" + "="*50)
            print(Fore.MAGENTA + " MENU UTAMA ".center(50, "="))
            print(Fore.MAGENTA + "="*50)
            print(Fore.CYAN + "1. Lihat Tabel Perkalian")
            print(Fore.CYAN + "2. Latihan Soal Perkalian Acak")
            print(Fore.CYAN + "3. Latihan Perkalian Terurut (1-10)")
            print(Fore.CYAN + "4. Mini Game Tantangan")
            print(Fore.CYAN + "5. Statistik Belajar")
            print(Fore.CYAN + "6. Tips Menghafal Perkalian")
            print(Fore.RED + "7. Keluar")
            
            choice = input(Fore.WHITE + "\nPilih menu (1-7): ").strip()
            
            if choice == "1":
                self.show_multiplication_table()
            elif choice == "2":
                self.practice_random_questions()
            elif choice == "3":
                self.practice_sequential_questions()
            elif choice == "4":
                self.play_mini_game()
            elif choice == "5":
                self.show_stats()
            elif choice == "6":
                self.show_tips()
            elif choice == "7":
                print(Fore.YELLOW + f"\nTerima kasih sudah belajar, {self.username}! Sampai jumpa lagi!")
                print(Fore.YELLOW + f"Skor akhirmu: {self.score}")
                print(Fore.YELLOW + f"Rekor streak terbaik: {self.best_streak}\n")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan pilih 1-7.")
                time.sleep(1)
    
    def show_multiplication_table(self):
        """Menampilkan tabel perkalian dengan warna"""
        self.clear_screen()
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " TABEL PERKALIAN 1-10 ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        
        # Header kolom
        print(Fore.YELLOW + "   |" + "".join([f"{i:4}" for i in range(1, 11)]))
        print(Fore.YELLOW + "----+" + "-"*40)
        
        # Baris isi tabel
        for i in range(1, 11):
            # Header baris
            row = f"{i:2} |"
            for j in range(1, 11):
                # Warna berbeda untuk hasil perkalian genap/ganjil
                if (i * j) % 2 == 0:
                    row += Fore.GREEN + f"{i*j:4}"
                else:
                    row += Fore.BLUE + f"{i*j:4}"
            print(row)
        
        input(Fore.WHITE + "\nTekan Enter untuk kembali ke menu utama...")
    
    def practice_random_questions(self):
        """Mode latihan soal perkalian acak"""
        self.clear_screen()
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " LATIHAN SOAL PERKALIAN ACAK ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        print(Fore.CYAN + f"{self.username}, mari berlatih perkalian secara acak!")
        print(Fore.CYAN + "Jawab soal-soal berikut. Ketik 'stop' untuk kembali ke menu.\n")
        
        while True:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            correct_answer = a * b
            
            question = f"{Fore.YELLOW}Berapa hasil dari {Fore.WHITE}{a} × {b}{Fore.YELLOW}? "
            user_answer = input(question + Fore.WHITE).strip().lower()
            
            if user_answer == "stop":
                break
            
            self.attempts += 1
            
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    self.correct_answers += 1
                    self.score += 10
                    self.streak += 1
                    if self.streak > self.best_streak:
                        self.best_streak = self.streak
                    
                    feedback = [
                        f"{Fore.GREEN}Benar! {a} × {b} = {correct_answer}. Kerja bagus, {self.username}!",
                        f"{Fore.GREEN}Hebat! Jawabanmu benar. Lanjutkan!",
                        f"{Fore.GREEN}Tepat sekali! Kamu sedang dalam streak {self.streak}!",
                        f"{Fore.GREEN}Kamu benar! Skormu sekarang {self.score}."
                    ]
                    print(random.choice(feedback))
                else:
                    self.streak = 0
                    feedback = [
                        f"{Fore.RED}Maaf, jawabanmu salah. {a} × {b} = {correct_answer}.",
                        f"{Fore.RED}Oops! Jawaban yang benar adalah {correct_answer}. Jangan menyerah!",
                        f"{Fore.RED}Belum tepat. Ingat bahwa {a} × {b} = {correct_answer}."
                    ]
                    print(random.choice(feedback))
                
                # Tampilkan persentase benar
                accuracy = (self.correct_answers / self.attempts) * 100 if self.attempts > 0 else 0
                print(Fore.CYAN + f"Akurasi: {accuracy:.1f}% | Streak: {self.streak} | Skor: {self.score}\n")
            
            except ValueError:
                print(Fore.RED + "Masukkan angka yang valid atau ketik 'stop' untuk berhenti.")
    
    def practice_sequential_questions(self):
        """Mode latihan soal perkalian terurut 1-10"""
        self.clear_screen()
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " LATIHAN PERKALIAN TERURUT 1-10 ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        print(Fore.CYAN + f"{self.username}, mari berlatih perkalian secara terurut dari 1 sampai 10!")
        print(Fore.CYAN + "Ketik 'stop' kapan saja untuk kembali ke menu.\n")
        
        correct_in_session = 0
        total_in_session = 0
        
        for multiplier in range(1, 11):
            self.clear_screen()
            print(Fore.MAGENTA + "\n" + "="*50)
            print(Fore.MAGENTA + f" PERKALIAN {multiplier} ".center(50, "="))
            print(Fore.MAGENTA + "="*50)
            
            for i in range(1, 11):
                correct_answer = multiplier * i
                
                question = f"{Fore.YELLOW}{multiplier} × {i} = "
                user_answer = input(question + Fore.WHITE).strip().lower()
                
                if user_answer == "stop":
                    self.show_session_result(correct_in_session, total_in_session)
                    return
                
                total_in_session += 1
                self.attempts += 1
                
                try:
                    user_answer = int(user_answer)
                    if user_answer == correct_answer:
                        correct_in_session += 1
                        self.correct_answers += 1
                        self.score += 5  # Nilai lebih kecil karena lebih mudah
                        print(Fore.GREEN + "Benar! 👍")
                    else:
                        print(Fore.RED + f"Kurang tepat. Jawabannya adalah {correct_answer}.")
                    
                    time.sleep(0.5)  # Jeda singkat antara soal
                
                except ValueError:
                    print(Fore.RED + "Masukkan angka yang valid!")
                    total_in_session -= 1
                    self.attempts -= 1
        
        self.show_session_result(correct_in_session, total_in_session)
    
    def show_session_result(self, correct, total):
        """Menampilkan hasil sesi latihan"""
        self.clear_screen()
        accuracy = (correct / total) * 100 if total > 0 else 0
        
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " HASIL LATIHAN ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        print(Fore.CYAN + f"Total soal: {total}")
        print(Fore.CYAN + f"Jawaban benar: {correct}")
        print(Fore.CYAN + f"Akurasi: {accuracy:.1f}%")
        
        # Beri penghargaan berdasarkan akurasi
        if accuracy >= 90:
            print(Fore.GREEN + "\n⭐️⭐️⭐️ LUAR BIASA! Kamu hampir sempurna! ⭐️⭐️⭐️")
            self.score += 30  # Bonus untuk performa bagus
        elif accuracy >= 70:
            print(Fore.GREEN + "\n⭐️⭐️ Bagus! Terus tingkatkan! ⭐️⭐️")
            self.score += 15
        elif accuracy >= 50:
            print(Fore.YELLOW + "\n⭐️ Cukup baik. Ayo lebih giat lagi! ⭐️")
        else:
            print(Fore.RED + "\nTetap semangat! Lihat tabel perkalian untuk membantu.")
        
        print(Fore.CYAN + f"\nSkor tambahan: {correct * 5}")
        print(Fore.CYAN + f"Skor total sekarang: {self.score}")
        input(Fore.WHITE + "\nTekan Enter untuk kembali ke menu utama...")
    
    def play_mini_game(self):
        """Mode mini game tantangan"""
        self.clear_screen()
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " MINI GAME TANTANGAN ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        print(Fore.CYAN + f"{self.username}, siap untuk tantangan?")
        print(Fore.CYAN + "Kamu punya 30 detik untuk menjawab sebanyak mungkin soal perkalian!")
        print(Fore.CYAN + "Setiap jawaban benar memberi 20 poin. Jawaban salah mengurangi 5 poin.")
        print(Fore.CYAN + "\nTekan Enter ketika siap...")
        input(Fore.WHITE + "> ")
        
        start_time = time.time()
        end_time = start_time + 30  # 30 detik
        questions_answered = 0
        correct_in_game = 0
        
        print(Fore.YELLOW + "\nMulai! Waktu dimulai sekarang!\n")
        
        while time.time() < end_time:
            a = random.randint(1, 12)  # Lebih menantang sampai 12
            b = random.randint(1, 12)
            correct_answer = a * b
            
            # Hitung waktu tersisa
            time_left = int(end_time - time.time())
            if time_left <= 0:
                break
            
            question = f"{Fore.YELLOW}[Waktu: {time_left} detik] {a} × {b} = "
            try:
                user_answer = int(input(question + Fore.WHITE))
            except ValueError:
                print(Fore.RED + "Masukkan angka saja! Coba soal berikutnya.")
                continue
            
            questions_answered += 1
            
            if user_answer == correct_answer:
                correct_in_game += 1
                self.score += 20
                self.correct_answers += 1
                print(Fore.GREEN + f"Benar! (+20 poin)")
            else:
                self.score = max(0, self.score - 5)  # Pastikan skor tidak negatif
                print(Fore.RED + f"Salah! Jawabannya {correct_answer}. (-5 poin)")
            
            self.attempts += 1
        
        # Hitung akurasi untuk game ini
        game_accuracy = (correct_in_game / questions_answered) * 100 if questions_answered > 0 else 0
        
        self.clear_screen()
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " HASIL MINI GAME ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        print(Fore.CYAN + f"Waktu habis, {self.username}!")
        print(Fore.CYAN + f"Total soal dijawab: {questions_answered}")
        print(Fore.CYAN + f"Jawaban benar: {correct_in_game}")
        print(Fore.CYAN + f"Akurasi: {game_accuracy:.1f}%")
        print(Fore.CYAN + f"Poin diperoleh: {correct_in_game * 20 - (questions_answered - correct_in_game) * 5}")
        print(Fore.CYAN + f"Skor total sekarang: {self.score}")
        input(Fore.WHITE + "\nTekan Enter untuk kembali ke menu utama...")
    
    def show_stats(self):
        """Menampilkan statistik belajar"""
        self.clear_screen()
        accuracy = (self.correct_answers / self.attempts) * 100 if self.attempts > 0 else 0
        
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " STATISTIK BELAJAR ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        print(Fore.CYAN + f"Nama: {self.username}")
        print(Fore.CYAN + f"Total soal dijawab: {self.attempts}")
        print(Fore.CYAN + f"Jawaban benar: {self.correct_answers}")
        print(Fore.CYAN + f"Akurasi: {accuracy:.1f}%")
        print(Fore.CYAN + f"Streak terbaik: {self.best_streak}")
        print(Fore.CYAN + f"Skor total: {self.score}")
        
        # Beri motivasi berdasarkan performa
        if self.attempts == 0:
            print(Fore.YELLOW + "\nKamu belum menjawab soal apa pun. Ayo mulai latihan!")
        elif accuracy >= 80:
            print(Fore.GREEN + "\nLuar biasa! Kamu sangat menguasai perkalian!")
        elif accuracy >= 60:
            print(Fore.GREEN + "\nBagus! Terus berlatih untuk meningkatkan akurasimu!")
        else:
            print(Fore.YELLOW + "\nTerus berusaha! Lihat tabel perkalian dan tips untuk membantumu.")
        
        input(Fore.WHITE + "\nTekan Enter untuk kembali ke menu utama...")
    
    def show_tips(self):
        """Menampilkan tips menghafal perkalian"""
        self.clear_screen()
        tips = [
            "1. Mulailah dengan perkalian mudah (1, 2, 5, 10) sebelum beralih ke yang lebih sulit.",
            "2. Gunakan tabel perkalian sebagai referensi saat mulai belajar.",
            "3. Hafalkan perkalian dengan pola, misalnya perkalian 9: hasilnya selalu angka puluhan +1 dan satuan -1 (9×2=18, 9×3=27, dst).",
            "4. Latihan setiap hari, bahkan hanya 5-10 menit, lebih efektif daripada sesi panjang tapi jarang.",
            "5. Gunakan jari untuk perkalian 6-9 untuk membantu menghafal.",
            "6. Buatlah lagu atau ritme untuk mengingat perkalian yang sulit.",
            "7. Cari pasangan angka yang hasil kalinya sama (2×6=12, 3×4=12) untuk memahami hubungan antar angka.",
            "8. Gunakan benda nyata seperti kelereng atau buah untuk memvisualisasikan perkalian.",
            "9. Tantang dirimu dengan timer untuk meningkatkan kecepatan.",
            "10. Jangan takut membuat kesalahan - itu bagian dari proses belajar!"
        ]
        
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.MAGENTA + " TIPS MENGHAPAL PERKALIAN ".center(50, "="))
        print(Fore.MAGENTA + "="*50)
        
        for tip in tips:
            print(Fore.CYAN + tip)
        
        input(Fore.WHITE + "\nTekan Enter untuk kembali ke menu utama...")

# Jalankan program
if __name__ == "__main__":
    game = MultiplicationGame()
    game.print_welcome()
    game.get_username()
    game.show_main_menu()