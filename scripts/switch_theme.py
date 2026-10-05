import os
import shutil
import sys

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(script_dir, '..')
    
    readme_path = os.path.join(repo_dir, 'README.md')
    rich_path = os.path.join(repo_dir, 'README-rich.md')
    minimal_path = os.path.join(repo_dir, 'README-minimal.md')
    
    if not os.path.exists(rich_path) or not os.path.exists(minimal_path):
        print("Error: README-rich.md or README-minimal.md is missing.")
        sys.exit(1)
        
    with open(readme_path, 'r', encoding='utf-8') as f:
        current_content = f.read()
        
    with open(rich_path, 'r', encoding='utf-8') as f:
        rich_content = f.read()
        
    # Check if we are currently rich or minimal
    is_rich = current_content.strip() == rich_content.strip()
    
    target_path = minimal_path if is_rich else rich_path
    theme_name = "minimalist" if is_rich else "rich/visual"
    
    shutil.copy2(target_path, readme_path)
    print(f"Success: Switched to the {theme_name} theme!")
    print("Don't forget to commit the changes if you want them live on GitHub.")

if __name__ == "__main__":
    main()
