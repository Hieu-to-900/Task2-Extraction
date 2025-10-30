"""
Utility to breakdown large MD file into smaller files by sections
"""
import os
import re

def breakdown_markdown_file(input_file: str, output_dir: str = "documents"):
    """Break down markdown file by # Public### sections"""
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by # Public pattern
    sections = re.split(r'\n(?=# Public\d+)', content)
    
    # Process each section
    files_created = 0
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Extract Public### name from first line
        lines = section.split('\n')
        if lines and lines[0].startswith('# Public'):
            public_name = lines[0].replace('# ', '').strip()
            
            # Create output file
            output_file = os.path.join(output_dir, f"{public_name}.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(section)
            
            print(f"Created: {output_file}")
            files_created += 1
    
    print(f"\nTotal files created: {files_created}")

if __name__ == "__main__":
    # Usage
    breakdown_markdown_file("answer_template_0to89.md", "documents")
