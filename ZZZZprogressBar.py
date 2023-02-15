import math
from PIL import Image, ImageDraw, ImageFont

def generate_progress_bar(total, current, milestones, labels):
    width, height = 400, 80
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 14)

    fill_width = math.floor(current / total * width)
    draw.rectangle((0, 60, 400, height), fill=(100, 100, 100, 255))
    draw.rectangle((0, 60, fill_width, height), fill=(0, 128, 0, 255))

    for milestone, label in zip(milestones, labels):
        milestone_width = math.floor(milestone / total * width)
        draw.line((milestone_width, 60, milestone_width, height), fill=(0, 0, 0, 255), width=2)
        draw.text((milestone_width, 20), label, fill=(0, 255, 53, 255), font=font)
    drawAt = min(323,fill_width + 2)
    draw.text((drawAt, 60), labels[-1], fill=(255, 255, 255, 255), font=font)

    return image

total = 1000
current = 645.61
milestones = [150, 300, 500, 750, 1000]
labels = ['I match\n$150','Hot Pepper\n$300', 'Bleached hair\n$500', '24 hr\n$750', f'Current(${current})']
image = generate_progress_bar(total, current, milestones, labels)
image.save('progress_bar.png', format='PNG')
