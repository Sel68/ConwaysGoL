import pygame as pg
import numpy as np

WIDTH, HEIGHT = 1440, 900
CELL_SIZE = 30
GRID_W = WIDTH // CELL_SIZE
GRID_H = HEIGHT // CELL_SIZE
COLOUR_A = "blue"
COLOUR_D = "white"
COLOUR_BORDER = "black"



def draw_grid(surface, grid):
    for x in range(GRID_W):
        for y in range(GRID_H):
            rect = pg.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(surface, pg.Color(COLOUR_A) if grid[x, y] else pg.Color(COLOUR_D), rect)
            pg.draw.rect(surface, pg.Color(COLOUR_BORDER), rect, 1)

def update(grid):
    new_grid = np.copy(grid)
    for x in range(GRID_W):
        for y in range(GRID_H):
            alive_n = np.sum(grid[max(0,x-1):min(GRID_W,x+2), max(0,y-1):min(GRID_H,y+2)]) - grid[x,y]
            
            if grid[x,y]:
                if alive_n not in [2,3]:
                    new_grid[x,y] = 0
            else:
                if alive_n==3:
                    new_grid[x,y] =1
            
    return new_grid

def f():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    grid = np.zeros((GRID_W, GRID_H), dtype=bool)
    paused = True

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                return
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE:
                    paused ^= 1
                elif e.key == pg.K_c:
                    grid.fill(False)
                elif e.key == pg.K_r:
                    grid = np.random.randint(2, size=(GRID_W, GRID_H), dtype=bool)
            elif e.type == pg.MOUSEBUTTONDOWN or e.type == pg.MOUSEMOTION:
                buttons = e.buttons if hasattr(e, 'buttons') else pg.mouse.get_pressed()
                if buttons[0]:
                    x,y = pg.mouse.get_pos()
                    grid[x//CELL_SIZE, y//CELL_SIZE] = True
                elif buttons[2]:
                    x,y = pg.mouse.get_pos()
                    grid[x//CELL_SIZE, y//CELL_SIZE] = False

        screen.fill(pg.Color(COLOUR_D))
        draw_grid(screen, grid)
        pg.display.flip()
        if not paused:
            grid = update(grid)
        clock.tick(30)


if __name__ == "__main__":
    f()
