import pygame

col = 64
row = 32
def construct(self, scale):

    self.scale = scale
    
    pygame.init()
    self.canvas = pygame.display.set_mode((col*scale, row*scale))
    self.display = [0] * (col * row)

def detectPixel(self, x, y):
    if x >= col:
        x -= col
    elif x < 0:
        x += col

    if y >= row:
        y -= row
    elif y < 0:
        y += row

    pixel_location = x + (y * col)
    self.display[pixel_location] ^= 1

    return not self.display[pixel_location]

def clearAll(self):
    self.display = [0] * (col * row)

def render(self):
        
        self.canvas.fill((255, 255, 255))

        for i in range(self.cols * self.rows):
            if self.display[i]:

                x = (i % self.cols) * self.scale
                y = (i // self.cols) * self.scale 

                pygame.draw.rect(

                    self.canvas,
                    (0, 0, 0), 
                    (x, y, self.scale, self.scale)
                )