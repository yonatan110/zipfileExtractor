import os
import zipfile


# extracting zipfiles class
class extractor:

    # getting the path of the extracted file and defining the path where to extract
    def __init__(self, extraction_zipfile_path):
        self.extraction_zipfile_path = extraction_zipfile_path
        self.this_path = os.path.dirname(__file__) + '\\ExtractedFiles'

    # extract all the files of the zipfile
    def extractAll(self):
        try:
            with open('rockyou.txt', 'rb') as file:
                for line in file:
                    for word in line.split():
                        try:
                            with zipfile.ZipFile(self.extraction_zipfile_path, 'r') as extracted_zipfile:
                                extracted_zipfile.extractall(self.this_path, pwd='' or word)
                                file.close()
                        except:
                            pass
        except:
            pass

    # extracting specific file of the zipfile
    def extract_Specific_file(self, file_name):
        try:
            with open('rockyou.txt', 'rb') as file:
                for line in file:
                    for word in line.split():
                        try:
                            with zipfile.ZipFile(self.extraction_zipfile_path, 'r') as extracted_zipfile:
                                extracted_zipfile.extract(file_name, self.this_path, pwd='' or word)
                                file.close()
                        except:
                            pass
        except:
            pass


# printing welcome message
def welcome_message():
    print('=' * 30)
    print("  Welcome to file extractor")
    print('=' * 30)


# extracting the whole zipfile
def extract_all(requested_file_extraction):
    requested_file_extraction.extractAll()
    print("File extracted successfully to ExtractedFile directory")


# extracting specific file from zipfile
def extractSpecific_file(requested_file_extraction):
    selected_file = input("File name to extract from the zipfile:")
    requested_file_extraction.extract_Specific_file(selected_file)


# checking if the path of the zipfile is really exist
def check_validate_path(path_to_check):
    try:
        with open(path_to_check, 'r'):
            return True
    except:
        return False


# taking the path from the user
def path_of_file():
    extract_this_file = input("Enter the path of the file you want to extract:")
    result = check_validate_path(extract_this_file)
    if result:
        return extractor(extract_this_file)
    else:
        print("Not existed path, Try again...")
        path_of_file()


# giving extracting options
def extraction_options(requested_file_extraction):
    print('=' * 30)
    print("Options of extraction:\n-Extract all\n-Extract specific file")
    print('=' * 30)
    choice = input("Choose an option:")

    if choice.lower() == 'extract all':
        extract_all(requested_file_extraction)

    elif choice.lower() == 'extract specific file':
        extractSpecific_file(requested_file_extraction)

    else:
        print("Incorrect input, try again...")
        extraction_options(requested_file_extraction)


def main():
    welcome_message()
    requested_file_extraction = path_of_file()
    extraction_options(requested_file_extraction)


if __name__ == '__main__':
    main()
