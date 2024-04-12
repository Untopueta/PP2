import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    
    drawing = False
    start_pos = None
    color = (255, 255, 255)  # Initial color (white)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                handle_key_events(event, color, mode)
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_down(event, points, color, mode, start_pos, drawing)
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                handle_mouse_motion(event, points, radius, mode, start_pos, drawing, screen, color)
        
        screen.fill((0, 0, 0))
        
        # Draw all points
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        pygame.display.flip()
        clock.tick(60)

def handle_key_events(event, color, mode):
    if event.key == pygame.K_r:
        mode = 'red'
    elif event.key == pygame.K_g:
        mode = 'green'
    elif event.key == pygame.K_b:
        mode = 'blue'
    elif event.key == pygame.K_c:
        color = pygame.Color('black')  # Change color to black
    elif event.key == pygame.K_e:
        color = pygame.Color('white')  # Change color to white
    # Add more color selection if needed
    
def handle_mouse_down(event, points, color, mode, start_pos, drawing):
    if event.button == 1:  # Left click
        drawing = True
        start_pos = event.pos
        points.append(start_pos)
    elif event.button == 3:  # Right click
        # Erase by drawing white over the points
        color = pygame.Color('white')
        drawing = True
        start_pos = event.pos
        points.append(start_pos)
    # Add handling for rectangle and circle drawing if needed

def handle_mouse_motion(event, points, radius, mode, start_pos, drawing, screen, color):
    if drawing:
        if mode == 'eraser':
            points.append(event.pos)
        elif mode == 'rectangle':
            pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], event.pos[0] - start_pos[0], event.pos[1] - start_pos[1]))
        elif mode == 'circle':
            radius = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
            pygame.draw.circle(screen, color, start_pos, radius)
        else:
            points.append(event.pos)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
