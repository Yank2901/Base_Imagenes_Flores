from PIL import Image
import os

def convert_images_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{name}.jpg")
            try:
                with Image.open(input_path) as img:
                    rgb_img = img.convert('RGB')
                    rgb_img.save(output_path, format='JPEG')
                print(f"Imagen {filename} convertida y guardada en: {output_path}")
            except Exception as e:
                print(f"Error al convertir la imagen {filename}: {e}")

input_folder_path = "C:/Users/yanic/RosaBrighton"
output_folder_path = "C:/Users/yanic/RosaBrightonConvertidas"

convert_images_to_jpg(input_folder_path, output_folder_path)
