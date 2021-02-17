import tkinter as tk
from domain.api import get_pokemon_img_data
from config.logging import config_logger
from PIL import Image, ImageTk
from io import BytesIO


def show_window(pokemon_info: dict):
    log = config_logger()

    main_window = tk.Tk()

    image_url = pokemon_info["sprites"]["other"]["official-artwork"]["front_default"]
    log.debug(f"image_url: {image_url}")
    img_data = get_pokemon_img_data(image_url)
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    sprite_url = pokemon_info["sprites"]["front_default"]
    log.debug(f"sprite_url: {sprite_url}")
    sprite_data = get_pokemon_img_data(sprite_url)
    sprite = ImageTk.PhotoImage(Image.open(BytesIO(sprite_data)))

    main_window.iconphoto(False, sprite)
    main_window.title(pokemon_info["name"].upper())
    b_image = tk.Button(main_window, image=img, command=main_window.destroy)
    b_image.pack(side="bottom", fill="both", expand="yes")

    log.info("Opening image-window...")
    main_window.mainloop()
