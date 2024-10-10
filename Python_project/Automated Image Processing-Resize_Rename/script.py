from PIL import Image, ImageOps
import os
import json

def get_best_match(image_name, names_list):
    max_matches = 0
    best_match = None

    for name in names_list:
        # Count matching characters in a simple way (you could implement LCS for better matching)
        matches = sum(1 for char in image_name if char in name)
        if matches > max_matches:
            max_matches = matches
            best_match = name

    return best_match

def resize_images(input_directory, output_directory, names_list, target_size=(150, 250), max_file_size_kb=100):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_directory, filename)
            with Image.open(image_path) as img:
                # Handle orientation
                img = ImageOps.exif_transpose(img)

                # Resize the image to fill the target dimensions
                img = img.resize(target_size, Image.LANCZOS)

                # Convert image to RGB mode if it's in RGBA mode
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                # Get the base name of the image (without extension and in lowercase)
                image_name = os.path.splitext(filename)[0].lower()

                # Find the best matching name from names_list
                best_match = get_best_match(image_name, names_list)

                if best_match:
                    output_filename = best_match
                else:
                    print(f"No matching name found for {filename}. Using default naming.")
                    output_filename = f"{image_name}.jpg"  # Default to original if no match

                output_path = os.path.join(output_directory, output_filename)

                # Save the image with a quality setting to keep file size under max_file_size_kb
                quality = 95  # Start with high quality
                while True:
                    img.save(output_path, format='JPEG', quality=quality)
                    # Check the file size
                    if os.path.getsize(output_path) <= max_file_size_kb * 1024:
                        break
                    quality -= 5  # Decrease quality if file size is too large

if __name__ == "__main__":
    input_dir = r'C:\Users\Asus\Desktop\profile_pictures'
    output_dir = r'C:\Users\Asus\Desktop\profile_pictures\Folder'

    # Read names from names.txt
    with open('names.txt', 'r') as file:
        names_list = json.load(file)

    resize_images(input_dir, output_dir, names_list)