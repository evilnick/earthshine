import os

def insert_header_after_frontmatter(file_path):
    """Insert a header after the frontmatter in the file with the file name."""
    file_name = os.path.basename(file_path)
    header = f"# {file_name}\n\n"
    
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0, 0)
        
        # Determine if the file contains frontmatter
        if lines[0].strip() == '---':
            frontmatter_end_index = None
            for i in range(1, len(lines)):
                if lines[i].strip() == '---':
                    frontmatter_end_index = i
                    break
            
            if frontmatter_end_index is not None:
                # Insert header after the frontmatter
                updated_lines = lines[:frontmatter_end_index + 1] + [header] + lines[frontmatter_end_index + 1:]
                file.writelines(updated_lines)
                return

        # If no valid frontmatter found, just prepend the header
        file.writelines([header] + lines)

def process_markdown_files(directory):
    """Process all markdown files in the given directory."""
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                insert_header_after_frontmatter(file_path)
                print(f"Inserted header in {file_name}")

if __name__ == "__main__":
    directory = input("Enter the directory path to process Markdown files: ")
    process_markdown_files(directory)
