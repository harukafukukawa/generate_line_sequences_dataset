img_height = 256
img_width = 256
size(256, 256)
background(0)
stroke(255)
strokeWeight(3)

dir_path = "/tmp/simple_line" 
seq_length = 10 # number of images in a sequence
num_seqs = 500 # number of total sequences

for j in range(0, num_seqs):  # Start line at random place and grow longer from both ends
    start_x = random(img_width)
    start_y = random(img_height)
    traj_x = int(random(-10, 10))
    traj_y = int(random(-10, 10))
    background(0)

    magnitude = int(random(1, 10)) # Determines length of initial line
    endpt_x = [start_x, start_x + traj_x * magnitude]
    endpt_y = [start_y, start_y + traj_y * magnitude]
    line(endpt_x[0], endpt_y[0] , endpt_x[1], endpt_y[1])
    magnitude = int(random(1, 5)) # Determines magnitude of line growth

    for i in range(0, seq_length):
        endpt_x = [endpt_x[0] - traj_x * magnitude, endpt_x[1] + traj_x * magnitude]
        endpt_y = [endpt_y[0] - traj_y * magnitude,  endpt_y[1] + traj_y * magnitude]
        line(endpt_x[0], endpt_y[0], endpt_x[1], endpt_y[1])
        save("{}/{}_{}.png".format(dir_path,j,i))
