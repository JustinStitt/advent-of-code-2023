from solve2 import export_to_render
from solve3 import export_contained

import pygame
pygame.init()

background_colour = (24, 24, 42)
width, height = (1000, 1000)
screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)

pt_color = (255, 0, 0)
ln_color = (66, 66, 66)
# grid lines
n = 200
sz = 5
r = sz//4
left_shift = 5
# vertical
for c in range(n):
    pygame.draw.line(screen, ln_color, (c*sz, 0), (c*sz, width))

# horizotnal
for c in range(n):
    pygame.draw.line(screen, ln_color, (0, c*sz), (height, c*sz))


# DRAW ALL POINTS AND EDGES
adj = export_to_render("big.in")
contained = export_contained()
print(adj)
# pygame.draw.circle(screen, pt_color, (100, 100), 100)

for pt, neighbors in adj.items():
    one, two = neighbors
    one = list(one)
    two = list(two)
    pt = list(pt)
    pt[0] -= left_shift
    pt[1] -= left_shift
    one[0] -= left_shift
    one[1] -= left_shift
    two[0] -= left_shift
    two[1] -= left_shift


    here = [pt[0]*sz, pt[1]*sz][::-1]
    one = [one[0]*sz, one[1]*sz][::-1]
    two = [two[0]*sz, two[1]*sz][::-1]
    pygame.draw.circle(screen, pt_color, here, r)
    # connect neighbors
    pygame.draw.line(screen, pt_color, here, one)
    pygame.draw.line(screen, pt_color, here, two)

    # if contained
    if pt in contained:
        pygame.draw.rect(screen, (0, 255, 0), (pt[1]*sz, pt[0]*sz, sz, sz))


pygame.display.flip()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print('done w/ render')
# print("export to render: ", export_to_render())
