from PIL import Image
import os

# Get the current directory
current_dir = os.getcwd()

# Define input and output folders (same directory)
input_folder = current_dir
output_folder = os.path.join(current_dir, "resized_images")  # Saves resized images in a new folder

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the current directory
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Filter images
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)  # Open image

        # Resize image to 32x32
        resized_img = img.resize((32, 32), Image.Resampling.LANCZOS)

        # Save resized image in the output folder
        resized_img.save(os.path.join(output_folder, filename))

print("All images have been resized to 32x32 and saved in the 'resized_images' folder!")