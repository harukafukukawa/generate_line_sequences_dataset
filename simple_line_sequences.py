img_height = 128
img_width = 128
size(128, 128)
background(0)
stroke(255)

"""
Dataset options:
    1. One line that gets longer by a constant length on both ends and stays the same random width throughout sequence
    2. One line that gets longer by a constant length on both ends and also gets wider by a constant amount
    3. Multiple lines that follow the rules of option 1
    4. Multiple lines that follow the rules of option 2
"""

dataset_num = 1 # See options above
dir_path = "/tmp/lines_{}".format(str(dataset_num))

futuregan_fmt = False

seq_length = 6 # number o f images in a sequence
num_seqs = 500 # number of total sequences

line_widens = False
if dataset_num % 2 == 0:
    line_widens = True

for j in range(0, num_seqs):  # Start line at random place and grow longer from both ends
    xys = []
    trajs = []
    stroke_weights = []
    line_coords = []
    line_widen_amts = []
    background(0)
    num_lines = int(random(1,5)) if dataset_num > 2 else 1
    for i in range(num_lines):
        xys.append([random(img_width), random(img_height)])
        trajs.append([int(random(-10, 10)), int(random(-10, 10))])
        init_len = int(random(1, 10))
        stroke_weights.append(random(1, 10))
        line_coords.append([xys[i][0], xys[i][1], xys[i][0] + trajs[i][0] * init_len, xys[i][1] + trajs[i][1] * init_len]) # coords are: x1, y1, x2, y2
        line_widen_amts.append(random(0, 1))
        strokeWeight(stroke_weights[i])
        line(*line_coords[i])

    for i in range(0, seq_length):
        background(0)
        for l in range(num_lines):
            coords = line_coords[l]
            traj = trajs[l]
            line_coords[l] = [coords[0] - traj[0], coords[1] - traj[1], coords[2] + traj[0], coords[3] + traj[1]]
            if line_widens:
                stroke_weights[l] += line_widen_amts[l]
            strokeWeight(stroke_weights[l])
            line(*line_coords[l])
        if futuregan_fmt == True:
            # Create test/train sets in the format expected for FutureGAN
            if j < num_seqs * .2:
                save("{}/test/{}/{}.png".format(dir_path,j,i)) # No need to shuffle train/test set because the lines are generated randomly
            else:
                save("{}/train/{}/{}.png".format(dir_path,j,i))
        else:
            save("{}/{}_{}.png".format(dir_path,j,i))
