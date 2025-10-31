from pathlib import Path
from typing import Dict, List

# def generate_blog_listing_html(blog_structure: Dict[str, List[Path]], base_folder: str) -> str:
#     """Generate HTML for blog listing
    
#     Args:
#         blog_structure: Dict from scan_blog_folders()
#         base_folder: Base folder name (e.g., 'Writing')
    
#     Returns:
#         HTML string for the content section
#     """
#     if not blog_structure:
#         return '<div class="container mx-auto max-w-7xl p-8"><p>No content available yet.</p></div>'
    
#     html_parts = ['<div class="container mx-auto max-w-7xl p-8">']
    
#     # Generate section for each category
#     for category, files in blog_structure.items():
#         html_parts.append(f'    <!-- {category} Section -->')
#         html_parts.append(f'    <section class="mb-12">')
#         html_parts.append(f'        <h2 class="text-3xl font-bold mb-6">{category}</h2>')
#         html_parts.append(f'        <ul class="space-y-3">')
        
#         # Generate list item for each blog
#         for md_file in files:
#             title = get_blog_title(md_file)
            
#             # Generate relative path for the link
#             # Example: Writing/Articles/blog1.md -> /Writing/Articles/blog1.html
#             relative_path = md_file.relative_to(Path('.'))
#             html_path = f"/{relative_path.with_suffix('.html')}"
            
#             html_parts.append(f'            <li>')
#             html_parts.append(f'                <a href="{html_path}" class="link link-hover text-lg">{title}</a>')
#             html_parts.append(f'            </li>')
        
#         html_parts.append(f'        </ul>')
#         html_parts.append(f'    </section>')
#         html_parts.append('')  # Empty line for readability
    
#     html_parts.append('</div>')
    
#     return '\n'.join(html_parts)

def generate_blog_listing_html(blog_structure: Dict[str, List[Path]], base_folder: str) -> str:
    """Generate HTML for blog listing with DaisyUI list components
    
    Args:
        blog_structure: Dict from scan_blog_folders()
        base_folder: Base folder name (e.g., 'Writing')
    
    Returns:
        HTML string for the content section
    """
    if not blog_structure:
        return '<div class="container mx-auto max-w-7xl p-8"><p>No content available yet.</p></div>'
    
    html_parts = ['<div class="container mx-auto max-w-7xl p-8">']
    
    # Generate section for each category
    for category, files in blog_structure.items():
        html_parts.append(f'    <!-- {category} Section -->')
        html_parts.append(f'    <section class="mb-16">')
        html_parts.append(f'        <h2 class="text-3xl font-bold mb-6">{category}</h2>')
        
        # Create responsive grid for lists
        html_parts.append(f'        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">')
        
        # Split posts into chunks of 5 for each list
        chunk_size = 5
        for i in range(0, len(files), chunk_size):
            chunk = files[i:i + chunk_size]
            
            # Start a new list component
            html_parts.append(f'            <ul class="list bg-base-200 rounded-box shadow-md">')
            
            # Generate list items for this chunk
            for md_file in chunk:
                title = get_blog_title(md_file)
                
                # Generate relative path for the link
                relative_path = md_file.relative_to(Path('.'))
                html_path = f"/{relative_path.with_suffix('.html')}"
                
                html_parts.append(f'                <li class="list-row hover:bg-base-300 transition-colors">')
                html_parts.append(f'                    <div class="list-col-grow">')
                html_parts.append(f'                        <a href="{html_path}" class="link link-hover font-medium">{title}</a>')
                html_parts.append(f'                    </div>')
                html_parts.append(f'                    <button class="btn btn-square btn-ghost btn-sm" onclick="window.location.href=\'{html_path}\'">')
                html_parts.append(f'                        <svg class="size-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>')
                html_parts.append(f'                    </button>')
                html_parts.append(f'                </li>')
            
            html_parts.append(f'            </ul>')
        
        html_parts.append(f'        </div>')
        html_parts.append(f'    </section>')
        html_parts.append('')
    
    html_parts.append('</div>')
    
    return '\n'.join(html_parts)

def humanize_folder_name(folder_name: str) -> str:
    """Convert folder name to human-readable format"""
    # Replace underscores and hyphens with spaces
    name = folder_name.replace('_', ' ').replace('-', ' ')
    
    return name


def scan_blog_folders(base_folder: str) -> Dict[str, List[Path]]:
    """Scan a base folder and return organized blog structure"""
    base_path = Path(base_folder)
    
    if not base_path.exists():
        return {}
    
    blog_structure = {}
    
    # Iterate through subfolders
    for subfolder in sorted(base_path.iterdir()):
        if subfolder.is_dir():
            # Get all markdown files in this subfolder
            md_files = sorted(subfolder.glob('*.md'))
            
            if md_files:
                folder_name = humanize_folder_name(subfolder.name)
                blog_structure[folder_name] = md_files
    
    return blog_structure


def get_blog_title(md_file: Path) -> str:
    """Extract title from markdown file"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Try to find first # heading
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# '):
                    return line.replace('# ', '').strip()
            
            # Fallback to filename
            return md_file.stem.replace('_', ' ').replace('-', ' ')
    
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return md_file.stem


if __name__ == '__main__':
    # Test the scanner
    folders = ['Writing', 'Notes', 'Coding', 'Devblogs', 'Resources']
    
    for folder in folders:
        print(f"\n{folder}:")
        structure = scan_blog_folders(folder)
        
        for category, files in structure.items():
            print(f"  {category}:")
            for file in files:
                title = get_blog_title(file)
                print(f"    - {title}")