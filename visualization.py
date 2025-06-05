import matplotlib.pyplot as plt

trails = [[], [], []]  # One list per body

def plot_positions(positions):
    # Update trails
    for i in range(3):
        trails[i].append((positions[i][0], positions[i][1]))
        # Keep last 100 points for trail
        if len(trails[i]) > 50:
            trails[i] = trails[i][-50:]

    # Compute center of positions
    center_x = sum(pos[0] for pos in positions) / 3
    center_y = sum(pos[1] for pos in positions) / 3
    
    plt.clf()  # Clear previous frame
    
    # Plot trails as thin, white lines
    for i in range(3):
        if len(trails[i]) > 1:
            trail_x = [pt[0] for pt in trails[i]]
            trail_y = [pt[1] for pt in trails[i]]
            plt.plot(
                trail_x, trail_y, 
                color='white', linewidth=0.7, alpha=0.7
            )
    
    # Plot bodies as white circles
    x_vals = [pos[0] for pos in positions]
    y_vals = [pos[1] for pos in positions]
    plt.scatter(
        x_vals, y_vals, 
        c='white', edgecolor='black', s=80, zorder=3
    )
    
    # Center the view
    range_x = 50
    range_y = 50
    plt.xlim(center_x - range_x, center_x + range_x)
    plt.ylim(center_y - range_y, center_y + range_y)

    # Grid Style
    plt.xlabel("X Position", color='black')
    plt.ylabel("Y Position", color='black')
    plt.title("3 Body Problem | Simulation", color='black')
    plt.grid(True, color='black', linewidth=0.5)
    plt.tick_params(colors='black')   # Black numbers/ticks

    # Axes Style
    ax = plt.gca()
    ax.set_facecolor('black')
    plt.gcf().patch.set_facecolor('black')
    
    # Framerate
    plt.pause(0.01)
