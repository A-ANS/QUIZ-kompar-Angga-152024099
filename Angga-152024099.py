import threading
import time

# TUGAS 1: Inisialisasi Sumber Daya (Resources)
# Kita menggunakan threading.Lock() untuk menyimulasikan dua sumber daya terpisah (misal: printer dan scanner).
sumber_daya_A = threading.Lock()
sumber_daya_B = threading.Lock()

def proses_1():
    # TUGAS 2: Eksekusi Proses 1
    print("Proses 1: Mencoba mendapatkan Sumber Daya A...")
    sumber_daya_A.acquire()
    print("Proses 1: -> Menahan (Hold) Sumber Daya A.")
    
    # Menyimulasikan waktu pemrosesan untuk memastikan Proses 2 punya waktu untuk mengambil Sumber Daya B
    time.sleep(1) 
    
    print("Proses 1: -> Menunggu Sumber Daya B (Kondisi Hold and Wait)...")
    sumber_daya_B.acquire() # Proses 1 akan terjebak (stuck) di sini
    
    # Baris di bawah ini tidak akan pernah dieksekusi karena terjadi deadlock
    print("Proses 1: Berhasil mendapatkan kedua sumber daya! Menyelesaikan tugas...")
    sumber_daya_B.release()
    sumber_daya_A.release()

def proses_2():
    # TUGAS 3: Eksekusi Proses 2
    print("Proses 2: Mencoba mendapatkan Sumber Daya B...")
    sumber_daya_B.acquire()
    print("Proses 2: -> Menahan (Hold) Sumber Daya B.")
    
    # Menyimulasikan waktu pemrosesan untuk memastikan Proses 1 punya waktu untuk mengambil Sumber Daya A
    time.sleep(1) 
    
    print("Proses 2: -> Menunggu Sumber Daya A (Kondisi Hold and Wait)...")
    sumber_daya_A.acquire() # Proses 2 akan terjebak (stuck) di sini
    
    # Baris di bawah ini tidak akan pernah dieksekusi karena terjadi deadlock
    print("Proses 2: Berhasil mendapatkan kedua sumber daya! Menyelesaikan tugas...")
    sumber_daya_A.release()
    sumber_daya_B.release()

# TUGAS 4: Eksekusi Thread
if __name__ == "__main__":
    print("--- Memulai Eksekusi Sistem ---")
    
    # Membuat thread untuk proses kita
    t1 = threading.Thread(target=proses_1)
    t2 = threading.Thread(target=proses_2)
    
    # Memulai thread secara bersamaan
    t1.start()
    t2.start()
    
    # Menunggu thread selesai
    t1.join()
    t2.join()
    
    print("--- Eksekusi Sistem Selesai ---") # Ini tidak akan pernah dicetak karena terjadi deadlock.