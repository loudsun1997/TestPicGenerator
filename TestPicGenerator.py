from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
import random


class TestPicGenerator:

    def red_pic_generator(self):  # Generate pic with single color
        return Image.new('RGB', (60, 30), color='red')

    #red = []  # Color array

    #for x in range(1000):
     #   red.append(red_pic_generator())

    def show_img(self, image_for_show):  # Show single image
        plt.imshow(image_for_show)
        plt.show()

    def array_img_print(self, array):  # Show image in an array
        for everyone in array:
            TestPicGenerator.show_img(self, everyone)

    def grid_generator10x10(self):
        im = Image.new('RGB', (500, 500), color='white')

        draw = ImageDraw.Draw(im)

        temp_x = 0
        temp_y = 50
        for x in range(20):
            draw.line([(0, temp_y), (500, temp_y)], fill=(0, 0, 0), width=2)
            temp_y = temp_y + 50

        for x in range(20):
            draw.line([(temp_x, 0), (temp_x, 500)], fill=(0, 0, 0), width=2)
            temp_x = temp_x + 50

        del temp_x
        del temp_y
        del draw
        #TestPicGenerator.show_img(self, im)
        return im

    def add_eclipse_to_image(self, center_x, center_y, radius, image_to_draw_on):
        draw = ImageDraw.Draw(image_to_draw_on)
        draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], 'black', 'black')
        del draw
        TestPicGenerator.show_img(self, image_to_draw_on)


def main():
    tester = TestPicGenerator

    for c in range(10):
        test_image = TestPicGenerator.grid_generator10x10(tester)
        radius = random.randint(1, 200)
        print(radius)
        TestPicGenerator.add_eclipse_to_image(tester, 250, 250, radius, test_image)
        filename = 'testimage/' + str(radius) + '.jpeg'
        test_image.save(filename)
        del radius


if __name__ == "__main__":
    main()

