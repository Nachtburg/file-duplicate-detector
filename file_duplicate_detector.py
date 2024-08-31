import os
import hashlib
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def hash_file(file_path):
    """指定されたファイルのSHA-256ハッシュを計算する"""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
    except Exception as e:
        return None, f"Error reading file {file_path}: {e}"
    return hasher.hexdigest(), None

def find_duplicates(directory, num_threads=4):
    """指定されたディレクトリ内の重複ファイルを検出する"""
    hashes = {}
    duplicates = {}
    errors = []

    def process_file(file_path):
        file_hash, error = hash_file(file_path)
        if error:
            errors.append((file_path, error))
            return
        if file_hash:
            if file_hash in hashes:
                if file_hash not in duplicates:
                    duplicates[file_hash] = [hashes[file_hash]]
                duplicates[file_hash].append(file_path)
            else:
                hashes[file_hash] = file_path

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                futures.append(executor.submit(process_file, file_path))

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing files"):
            pass

    return duplicates, errors

def remove_duplicates(duplicates, keep_original=True):
    """重複ファイルを削除し、リストを保存する"""
    removed_files = []
    kept_files = []

    for file_hash, files in duplicates.items():
        if keep_original:
            kept_files.append(files[0])
            for file in files[1:]:
                os.remove(file)
                removed_files.append(file)
        else:
            for file in files:
                os.remove(file)
                removed_files.append(file)

    with open('kept_files.txt', 'w') as kept_file:
        for file in kept_files:
            kept_file.write(f"{file}\n")
    
    with open('removed_files.txt', 'w') as removed_file:
        for file in removed_files:
            removed_file.write(f"{file}\n")

def main():
    directory = input("Enter the directory to scan for duplicates: ")
    num_threads = int(input("Enter the number of threads to use (e.g., 4): "))
    keep_original = input("Keep the original files? (yes/no): ").strip().lower() == 'yes'
    
    print("Scanning for duplicates...")
    duplicates, errors = find_duplicates(directory, num_threads)
    
    if duplicates:
        print("Duplicate files detected. Removing duplicates...")
        remove_duplicates(duplicates, keep_original)
        print("Duplicate removal complete. Check kept_files.txt and removed_files.txt for details.")
    else:
        print("No duplicates found.")
    
    if errors:
        with open('errors.log', 'w') as log_file:
            for file_path, error in errors:
                log_file.write(f"Error processing {file_path}: {error}\n")
        print("Errors have been logged to errors.log")

if __name__ == "__main__":
    main()
