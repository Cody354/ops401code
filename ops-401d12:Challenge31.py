import os
import logging
import platform

# Set up logging
logging.basicConfig(filename='file_search.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def search_files(file_name, search_directory):
    hits = 0
    files_searched = 0

    # Walk through the directory
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            files_searched += 1
            if file == file_name:
                hits += 1
                file_path = os.path.join(root, file)
                print(f"Found: {file_path}")
                logging.info(f"Found: {file_path}")

    return files_searched, hits

def main():
    # Prompt user for file name and directory
    file_name = input("Enter the file name to search for: ").strip()
    search_directory = input("Enter the directory to search in: ").strip()

    # validate directory
    if not os.path.isdir(search_directory):
        print(f"Error: {search_directory} is not a valid directory.")
        logging.error(f"{search_directory} is not a valid directory.")
        return

    logging.info(f"Starting search for '{file_name}' in directory '{search_directory}'")
    
    # perform search
    files_searched, hits = search_files(file_name, search_directory)

    # Print summary
    print(f"\nSearch complete. {files_searched} files were searched.")
    print(f"{hits} hits were found.")
    logging.info(f"Search complete. {files_searched} files were searched. {hits} hits were found.")

if __name__ == "__main__":
    main()
