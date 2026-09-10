import os
import random
import shutil

def rotate_banner():
    # Define paths relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, '..', 'assets')
    target_banner = os.path.join(assets_dir, 'header_banner.svg')
    
    # The specific banners the user selected
    banners = [
        "banner_aryan_ashish_terminal.svg",
        "banner_retro_phosphor.svg",
        "banner_crimson_eclipse.svg",
        "banner_abyssal_trench.svg",
        "banner_minimal_monolith.svg",
        "banner_titanium_monolith.svg",
        "banner_quantum_violet.svg",
        "banner_stellar_amber.svg",
        "banner_neo_synthwave.svg"
    ]
    
    # Verify they exist
    available_banners = [b for b in banners if os.path.exists(os.path.join(assets_dir, b))]
    
    if not available_banners:
        print("Error: No banners found in the assets directory.")
        return
        
    print(f"Found {len(available_banners)} banners available for rotation.")
    
    # Pick a random banner
    selected_banner = random.choice(available_banners)
    source_path = os.path.join(assets_dir, selected_banner)
    
    # Copy the selected banner to header_banner.svg
    shutil.copy2(source_path, target_banner)
    
    print(f"Successfully rotated banner to: {selected_banner}")

if __name__ == "__main__":
    rotate_banner()
