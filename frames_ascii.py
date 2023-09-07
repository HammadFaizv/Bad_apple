from PIL import Image

def image_to_ascii_art(img_path, output_file):

    img = Image.open(img_path).convert("L")  # convert pic to black and white

    width, height = img.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.65
    img = img.resize((new_width, int(new_height)))

    pixels = img.getdata()
    print("PIXELS OF IMAGE: \n",pixels)
    for i in pixels:
        print(i, end=" ")
    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [
        new_pixels[index : index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]
    ascii_image = "\n".join(ascii_image)

    with open(f"{output_file}.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image


for i in range(1,6573):
    img_path = "./Frames/frame_" + str(i) + ".png"
    output = "./Ascii_Frames/Aframe_" + str(i)
    image_to_ascii_art(img_path, output)
print("Images converted successfully")

