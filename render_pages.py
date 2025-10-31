from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from config_loader import load_site_config
from blog_scanner import scan_blog_folders, generate_blog_listing_html

def render_all_pages():
    """Render all pages from navigation config"""
    
    # Load config
    config = load_site_config()
    
    # Setup Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    base_template = env.get_template('base.html')
    blog_listing_template = env.get_template('blog_listing.html')
    
    # Create output directory
    output_dir = Path('.')
    
    # Pages that need blog listings
    blog_pages = config["blogfolders"]
    
    # Render each page
    for page in config['navigation']:
        print(f"Rendering: {page['label']}...")
        
        folder_name = page.get('folder')
        
        # Check if this page needs a blog listing
        if folder_name and folder_name in blog_pages:
            # Scan for blogs
            blog_structure = scan_blog_folders(folder_name)
            blog_listing_html = generate_blog_listing_html(blog_structure, folder_name)
            
            # Render with blog listing template
            html = blog_listing_template.render(
                site=config['site'],
                navigation=config['navigation'],
                socials=config['socials'],
                themes=config['themes'],
                page=page,
                blog_listing_html=blog_listing_html
            )
        else:
            # Regular page without blog listing
            html = base_template.render(
                site=config['site'],
                navigation=config['navigation'],
                socials=config['socials'],
                themes=config['themes'],
                page=page
            )
        
        # Write output
        output_path = output_dir / page['file']
        output_path.write_text(html, encoding='utf-8')
        
        print(f"  ✅ Generated: {output_path}")
    
    print(f"\n🎉 Successfully generated {len(config['navigation'])} pages!")

if __name__ == '__main__':
    render_all_pages()