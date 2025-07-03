class FileExport:
    @staticmethod
    def save_to_file(filename: str, content: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return f"Arquivo salvo como {filename}"
