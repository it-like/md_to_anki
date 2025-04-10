import os

def merge_markdown_files_to_txt(folder_path, output_file):
    """
    Merges the contents of all .md files in `folder_path`
    into a single .txt file specified by `output_file`.
    """
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as out_f:
        
        for filename in os.listdir(folder_path):
            # We only care about Markdown files
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                
                # Read the contents of the Markdown file
                with open(file_path, 'r', encoding='utf-8') as in_f:
                    contents = in_f.read()
                
                # Write the contents to the output file
                print(f'Reading File: {filename}')
                out_f.write(f'# Begin File {filename}\n\n')  # Optional header
                out_f.write(contents)
                out_f.write('\n\n')  # Fill
                out_f.write(f'# End File {filename}\n\n')  # Optional header
                out_f.write('\n\n')  

if __name__ == '__main__':
    # CHANGE THESE PATHS to your desired folder and output file name
    
    path = '/Users/YOURNAME/Obsidian/VAULTNAME/PRECISE/PATH/TO/THE/MONEEEYY'
    output_file = 'merged_markdown.txt'

    merge_markdown_files_to_txt(path, output_file)
    print(f"All Markdown files from {path} have been merged into {output_file}.")
