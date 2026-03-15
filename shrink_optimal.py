import re
import base64
import io
from PIL import Image

def compress_base64_image(b64_string, max_width=400, max_height=400, quality=60):
    try:
        # Pad base64 if needed
        b64_string += "=" * ((4 - len(b64_string) % 4) % 4)
        image_data = base64.b64decode(b64_string)
        img = Image.open(io.BytesIO(image_data))
        
        # Convert to RGB (required for aggressive WebP or JPEG compression without alpha)
        if img.mode in ("RGBA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "RGBA":
                bg.paste(img, mask=img.split()[3])
            else:
                bg.paste(img)
            img = bg
            
        # Optimal resize for thumbnails
        if img.width > max_width or img.height > max_height:
            img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        # High quality WebP compression
        output = io.BytesIO()
        img.save(output, format='WEBP', quality=quality, method=6)
        
        compressed_b64 = base64.b64encode(output.getvalue()).decode('ascii')
        return compressed_b64, len(b64_string), len(compressed_b64)
    except Exception as e:
        print(f"Error compressing: {e}")
        return b64_string, len(b64_string), len(b64_string)

with open("/tmp/generate_html.py", "r", encoding="utf-8") as f:
    content = f.read()

def replace_func(match):
    prefix = match.group(1)
    original_b64 = match.group(2)
    
    compressed_b64, old_size, new_size = compress_base64_image(original_b64)
    # Always replace with the newly compressed webp, even if slightly larger than ultra extreme, because we want better quality now
    prefix = re.sub(r'data:image/[a-zA-Z]+;base64,', 'data:image/webp;base64,', prefix)
    print(f"Optimal Compressed from {old_size} to {new_size} chars ({(new_size/old_size*100):.1f}%)")
    return prefix + compressed_b64

# Pattern matches any base64 image data
pattern = re.compile(r'(data:image/[a-zA-Z]+;base64,)([A-Za-z0-9+/=]+)')
new_content = pattern.sub(replace_func, content)

with open("/tmp/generate_html.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Finished optimal python shrinking logic")
