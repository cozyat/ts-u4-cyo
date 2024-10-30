
import random
import tsapp
import sys

def load_string(filename):
    with open(filename, "r") as file:
        return file.read()

def split_line(line):
    return line.split(": ")

collection = {}
string = load_string("data.txt")
score_list = load_string("number.txt").strip().split("\n")

def process_data(string):
    image_keys = []
    app_values = []
    lines = string.strip().split("\n")
    for line in lines:
        if ": " in line:
            img, app = split_line(line)
            image_keys.append(img)
            app_values.append(app)
    return image_keys, app_values

image_names, app_names = process_data(string)

for image_key, app_value in zip(image_names, app_names):
    collection[image_key] = app_value

window = tsapp.GraphicsWindow(500, 500, tsapp.BLACK)
current_sprite = None
counter_sprite = None
score = 0

while window.is_running:
    random_image = random.choice(list(collection.keys()))
    if current_sprite is not None and counter_sprite is not None:
        current_sprite.destroy()
        counter_sprite.destroy()
        
    current_sprite = tsapp.Sprite(random_image, 100, 100, 1)
    counter_sprite = tsapp.Sprite(score_list[score], 100, 100, 1)
    
    counter_sprite.center = (100, 60)
    
    window.add_object(current_sprite)
    window.add_object(counter_sprite)
    
    window_center_x = window.width // 2
    window_center_y = window.height // 2
    
    sprite_center_x = current_sprite.width // 2
    sprite_center_y = current_sprite.height // 2
    
    current_sprite.x = window_center_x - sprite_center_x
    current_sprite.y = window_center_y - sprite_center_y

    current_sprite.scale = 1
    window.finish_frame()

    guess = input('What is this app? (or type "exit" to quit) ')
    if guess.lower() == "exit" and score == 0:
        print("You have exited.")
        break
    elif guess.lower() == "exit" and score != 0:
        print("You have exited, thanks for playing!")
        break
    if guess == collection.get(random_image):
        print("Correct!")
        score += 1
    else:
        print("The correct answer was " + collection.get(random_image) + ".")
        score -= 1
    if score < 0:
        print("Your score went below 0. Game over.")
        counter_sprite.destroy()
        break
    elif score > 9:
        print("Congratulations! You've reached the maximum score of 10 points.")
        counter_sprite.destroy()
        break
    
    print("\n")
    
sys.exit()
