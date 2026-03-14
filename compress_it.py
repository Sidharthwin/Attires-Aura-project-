import os
from PIL import Image

assets_dir = 'assets'
images = [f for f in os.listdir(assets_dir) if f.startswith('IMG_') and f.lower().endswith(('.jpg', '.jpeg'))]

for img in images:
    img_path = os.path.join(assets_dir, img)
    print(f"Compressing {img}...")
    try:
        picture = Image.open(img_path)
        
        # Calculate new dimensions (max 1600px width/height while keeping aspect ratio)
        max_size = 1600
        ratio = min(max_size / picture.width, max_size / picture.height)
        new_size = (int(picture.width * ratio), int(picture.height * ratio))
        
        if ratio < 1:
            picture = picture.resize(new_size, Image.Resampling.LANCZOS)
            
        # Overwrite with high compression (Q=75 is standard web practice)
        picture.save(img_path, "JPEG", optimize=True, quality=75)
        print(f"Success: {img}")
    except Exception as e:
        print(f"Error on {img}: {e}")

print("All heavy assets compressed successfully!")
