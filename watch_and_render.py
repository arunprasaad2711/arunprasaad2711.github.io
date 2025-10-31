import time
import hashlib
from pathlib import Path
from convert_markdown import convert_markdown_to_html, get_blog_metadata
from config_loader import load_site_config
from jinja2 import Environment, FileSystemLoader

class MarkdownWatcher:
    """Watch and render markdown files on changes"""
    
    def __init__(self):
        self.config = load_site_config()
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.blog_template = self.env.get_template('blog_post.html')
        
        # Track folders to watch
        self.watch_folders = self.config["blogfolders"]
        
        # Track file hashes to detect changes
        self.file_hashes = {}
    
    def get_file_hash(self, filepath: Path) -> str:
        """Get hash of file contents"""
        try:
            return hashlib.md5(filepath.read_bytes()).hexdigest()
        except:
            return ""
    
    def scan_for_changes(self):
        """Scan all markdown files and detect changes"""
        changes = []
        
        for folder in self.watch_folders:
            folder_path = Path(folder)
            if not folder_path.exists():
                continue
            
            # Find all markdown files recursively
            for md_file in folder_path.rglob('*.md'):
                current_hash = self.get_file_hash(md_file)
                previous_hash = self.file_hashes.get(str(md_file))
                
                # Detect changes
                if current_hash != previous_hash:
                    changes.append(md_file)
                    self.file_hashes[str(md_file)] = current_hash
        
        return changes
    
    def render_file(self, md_file: Path):
        """Render a single markdown file to HTML"""
        try:
            print(f"\n🔄 Change detected: {md_file}")
            
            # Determine base folder
            base_folder = md_file.parts[0]
            
            # Get blog metadata
            blog_meta = get_blog_metadata(md_file, base_folder)
            
            # Convert markdown to HTML
            print(f"  📝 Converting markdown...")
            html_content = convert_markdown_to_html(md_file)
            
            # Render with template
            print(f"  🎨 Applying template...")
            full_html = self.blog_template.render(
                site=self.config['site'],
                navigation=self.config['navigation'],
                socials=self.config['socials'],
                themes=self.config['themes'],
                content=html_content,
                page=blog_meta
            )
            
            # Write HTML file
            html_file = md_file.with_suffix('.html')
            html_file.write_text(full_html, encoding='utf-8')
            
            print(f"  ✅ Rendered: {html_file}")
            print(f"  ⏱️  Watching for next change...")
            
        except Exception as e:
            print(f"  ❌ Error rendering {md_file}: {e}")
    
    def watch(self):
        """Start watching for changes"""
        print("👀 Watching for markdown file changes...")
        print("📁 Monitoring folders: Writing, Notes, Coding, Devblogs, Resources")
        print("💡 Edit any .md file and it will auto-render!")
        print("🛑 Press Ctrl+C to stop\n")
        
        # Initial scan to populate hashes
        print("🔍 Initial scan...")
        for folder in self.watch_folders:
            folder_path = Path(folder)
            if folder_path.exists():
                for md_file in folder_path.rglob('*.md'):
                    self.file_hashes[str(md_file)] = self.get_file_hash(md_file)
                print(f"✅ Watching: {folder}/ (including all subfolders)")
        
        print("\n⏳ Ready! Watching for changes...\n")
        
        try:
            while True:
                # Check for changes every second
                changes = self.scan_for_changes()
                
                for md_file in changes:
                    self.render_file(md_file)
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\n👋 Stopped watching. Goodbye!")


if __name__ == '__main__':
    watcher = MarkdownWatcher()
    watcher.watch()