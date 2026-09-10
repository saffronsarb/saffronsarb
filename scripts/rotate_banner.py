import os
import random
import shutil

def rotate_banner():
    # Define paths relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, '..', 'assets')
    target_banner = os.path.join(assets_dir, 'header_banner.svg')
    
    # Get all banner files
    banners = [f for f in os.listdir(assets_dir) if f.startswith('banner_') and f.endswith('.svg')]
    
    if not banners:
        print("Error: No banners found in the assets directory.")
        return
        
    print(f"Found {len(banners)} banners available for rotation.")
    
    # Pick a random banner
    selected_banner = random.choice(banners)
    source_path = os.path.join(assets_dir, selected_banner)
    
    # Copy the selected banner to header_banner.svg
    shutil.copy2(source_path, target_banner)
    
    print(f"Successfully rotated banner to: {selected_banner}")

if __name__ == "__main__":
    rotate_banner()
