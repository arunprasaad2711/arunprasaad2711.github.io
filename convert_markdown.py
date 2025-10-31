from pathlib import Path
import subprocess
from jinja2 import Environment, FileSystemLoader
from config_loader import load_site_config

def convert_markdown_to_html(md_file: Path) -> str:
    """Convert markdown file to HTML using Pandoc
    
    Args:
        md_file: Path to markdown file
    
    Returns:
        HTML string of converted content
    """
    try:
        # Run Pandoc to convert markdown to HTML
        result = subprocess.run(
            ['pandoc', '--from=markdown', '--to=html5', '--mathjax', '--highlight-style=pygments', str(md_file)],
            capture_output=True,
            text=True,
            check=True
        )
        
        return result.stdout
    
    except subprocess.CalledProcessError as e:
        print(f"Error converting {md_file}: {e}")
        return f"<p>Error converting markdown file.</p>"
    
    except FileNotFoundError:
        print("Pandoc not found. Please install Pandoc.")
        return f"<p>Pandoc not installed.</p>"


def get_blog_metadata(md_file: Path, base_folder: str) -> dict:
    """Extract metadata from markdown file path
    
    Args:
        md_file: Path to markdown file
        base_folder: Base folder name (e.g., 'Writing')
    
    Returns:
        Dict with blog metadata
    """
    # Get blog title
    title = get_blog_title(md_file)
    
    # Get category (subfolder name)
    # Example: Writing/Articles/blog.md -> 'Articles'
    relative_path = md_file.relative_to(base_folder)
    category = relative_path.parts[0] if len(relative_path.parts) > 1 else base_folder
    
    return {
        'title': title,
        'category': category,
        'folder': base_folder,
        'is_blog_post': True  # Flag to indicate this is a blog post
    }


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


def convert_all_markdown_files(base_folders: list):
    """Convert all markdown files in specified folders to HTML"""
    
    # Load config
    config = load_site_config()
    
    # Setup Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    blog_template = env.get_template('blog_post.html')
    
    total_converted = 0
    
    for base_folder in base_folders:
        base_path = Path(base_folder)
        
        if not base_path.exists():
            print(f"⚠️  Folder not found: {base_folder}")
            continue
        
        print(f"\n📁 Processing: {base_folder}")
        
        # Find all markdown files recursively
        md_files = list(base_path.rglob('*.md'))
        
        if not md_files:
            print(f"  No markdown files found.")
            continue
        
        print(f"  Found {len(md_files)} markdown files")
        
        for md_file in md_files:
            print(f"  Converting: {md_file.relative_to(base_path)}")
            
            # Get blog metadata
            blog_meta = get_blog_metadata(md_file, base_folder)
            
            # Convert markdown to HTML
            html_content = convert_markdown_to_html(md_file)
            
            # Render with template
            full_html = blog_template.render(
                site=config['site'],
                navigation=config['navigation'],
                socials=config['socials'],
                themes=config['themes'],
                content=html_content,
                page=blog_meta  # Pass blog metadata as 'page'
            )
            
            # Write HTML file in same directory as markdown file
            html_file = md_file.with_suffix('.html')
            html_file.write_text(full_html, encoding='utf-8')
            
            total_converted += 1
            print(f"    ✅ Generated: {html_file.relative_to(base_path)}")
    
    print(f"\n🎉 Successfully converted {total_converted} markdown files!")


if __name__ == '__main__':
    # Folders to process
    folders = ['Writing', 'Notes', 'Coding', 'Devblogs', 'Resources']
    
    convert_all_markdown_files(folders)