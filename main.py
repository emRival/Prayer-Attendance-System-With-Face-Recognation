import os

file_choices = {
    '1': 'get_faces_from_camera_tkinter.py',
    '2': 'features_extraction_to_csv.py',
    '3': 'attendance_taker.py'
}

choice = input("Masukkan nomor pilihan Anda (1, 2, atau 3): ")
selected_file = file_choices.get(choice)

if selected_file and os.path.exists(selected_file):
    # Jalankan file yang dipilih
    os.system(f'python {selected_file}')
else:
    print(f"File {selected_file} tidak ditemukan.")
