import check_box
import pygame
import os
import sys


class CheckBoxCollection():
    def __init__(self, x, y, amount, height, texts, realtive_height_of_element=0.8, only_one_simultaneous_ckeck=False,
                 layout="vertical", horizontal_box_distance=None,
                 color=(255, 255, 255), font_name="comicsans",
                 relative_box_size=0.7, border_thickness=None, is_checked=False, draw_mouse_hover=False,
                 fps=60, tick_color=(30, 130, 255)):

        self.only_one_simultaneous_ckeck = only_one_simultaneous_ckeck

        distance = (1-realtive_height_of_element) * height
        element_height = int(
            round((realtive_height_of_element * height / amount), 0))

        self.check_boxes = []

        for i in range(amount):
            if layout == "horizontal":
                pos_x = x + horizontal_box_distance * i
                pos_y = y
            else:
                pos_x = x
                pos_y = y + distance * i

            self.check_boxes.append(check_box.CheckBox(pos_x, pos_y, texts[i], element_height, color=color, font_name=font_name,
                                                       relative_box_size=relative_box_size, border_thickness=border_thickness, is_checked=is_checked,
                                                       draw_mouse_hover=draw_mouse_hover, fps=FPS, tick_color=tick_color))

    def draw(self, win):
        for check_box in self.check_boxes:
            check_box.draw(win)

    def update(self, click_event):
        before = [i.is_checked for i in self.check_boxes]

        for check_box in self.check_boxes:
            check_box.update(click_event)

        after = [i.is_checked for i in self.check_boxes]

        diffrence = [a - b for a, b in zip(before, after)]

        if self.only_one_simultaneous_ckeck:
            if any(diffrence):
                if any(before) and sum(diffrence) < 0:
                    change_index = [i for i, x in enumerate(before) if x][0]
                    self.check_boxes[change_index].is_checked = not self.check_boxes[change_index].is_checked

    def get_checked_texts(self):
        checked_texts = [i.text for i in self.check_boxes if i.is_checked]
        return checked_texts


if __name__ == '__main__':

    FPS = 60

    c = CheckBoxCollection(
        100, 100, 4, 400, ["text1", "text2", "text3", "text4"], draw_mouse_hover=True, only_one_simultaneous_ckeck=False)

    SCRWIDTH = 600
    SCRHEIGHT = 600

    HW = SCRWIDTH // 2
    HH = SCRHEIGHT // 2

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (100, 100, 100)
    RED = (255, 30, 30)
    GREEN = (30, 255, 30)
    BLUE = (30, 30, 255)

    WIN = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))
    pygame.display.set_caption("Space Game")
    directory_of_file = os.path.normpath(sys.argv[0] + os.sep + os.pardir)

    CLOCK = pygame.time.Clock()

    def draw():
        WIN.fill((0, 0, 0))
        c.draw(WIN)

    def main():
        run = True

        while run:
            click_event = False

            CLOCK.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_event = True

            keys = pygame.key.get_pressed()
            c.update(click_event)

            draw()

            pygame.display.update()

    main()
    pygame.quit()
