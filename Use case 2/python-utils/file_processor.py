class FileProcessor:
    def __init__(self, path):
        self.path = path

    def read(self):
        """Safely read all lines from file"""
        try:
            with open(self.path, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.path}' not found.")
            return []
        except PermissionError:
            print(f"Error: No permission to read '{self.path}'.")
            return []

    def process(self, lines):
        """Clean and transform lines using comprehension"""
        return [line.strip().upper() for line in lines if line.strip()]

    def write(self, output_path, lines):
        """Safely write processed lines"""
        try:
            with open(output_path, "w") as f:
                for line in lines:
                    f.write(line + "\n")
            print(f"Written {len(lines)} lines to {output_path}")
        except IOError as e:
            print(f"Error writing file: {e}")


if __name__ == "__main__":
    fp = FileProcessor("data.txt")
    raw_lines = fp.read()
    processed = fp.process(raw_lines)
    fp.write("processed_data.txt", processed)