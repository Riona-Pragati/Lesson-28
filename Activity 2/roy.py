class StudentFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_student_info(self, info):
        with open(self.filename, "w") as file:
            file.write(info)
        print("File overwritten successfully!")

    def append_student_info(self, info):
        with open(self.filename, "a") as file:
            file.write(info)
        print("New student info added!")

    def read_file(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                print("\n--- File Content ---")
                print(content)
        except FileNotFoundError:
            print("File not found! Please create it first.")

    def read_write_mode(self, info):
        try:
            with open(self.filename, "r+") as file:
                print("\n--- Existing Content ---")
                print(file.read())
                file.write("\n" + info)
            print("Updated file using r+ mode!")
        except FileNotFoundError:
            print("File not found! Cannot use r+ mode.")


def main():
    print("Roy's Student Record Manager\n")

    handler = StudentFileHandler("students.txt")

    handler.write_student_info("Name: Aditi\nIntro: Loves painting\nFavorite Subject: Art\n\n")

    handler.append_student_info("Name: Rohan\nIntro: Enjoys football\nFavorite Subject: Math\n\n")

    handler.read_file()

    handler.read_write_mode("Name: Sara\nIntro: Book lover\nFavorite Subject: English\n")

    handler.read_file()


if __name__ == "__main__":
    main()
