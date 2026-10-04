# Week 4 ROS 2 Activity

This repository is my individual Week 4 ROS 2 activity. It follows the lab material: turtlesim, RQT, ROS 2 concepts, colcon workspaces, and an `ament_python` package.

## Submission status

The source files and command plan are ready. Commands marked **Run in my VM** must be executed in my own ROS 2 Rolling VM before submission. I will add my own terminal output and screenshots under `evidence/`; this repository does not claim that those commands were run elsewhere.

## Environment assumed by the slides

- Ubuntu VM with ROS 2 Rolling installed
- Internet access for package installation and cloning sources
- A terminal whose ROS 2 environment can be sourced with `/opt/ros/rolling/setup.bash`

## 1. Turtlesim

Open separate terminals as needed.

```bash
# Run in my VM: update and install the package shown in the slides
sudo apt update
sudo apt install ros-rolling-turtlesim

# Run in my VM: inspect turtlesim executables
ros2 pkg executables turtlesim

# Terminal 1 - run in my VM: start the simulator node
ros2 run turtlesim turtlesim_node

# Terminal 2 - run in my VM: keyboard teleoperation
ros2 run turtlesim turtle_teleop_key
```

With the teleoperation terminal focused, I will use the arrow keys and capture evidence of the turtle path.

## 2. RQT

```bash
# Run in my VM: install RQT and its plugins (exact package pattern shown on slide 16)
sudo apt update
sudo apt install ~nros-rolling-rqt*

# Run in my VM: open the RQT application
rqt

# Run in my VM: open the console directly
ros2 run rqt_console rqt_console
```

In `rqt`, I will select **Plugins > Services > Service Caller**. In `rqt_console`, I will inspect messages, try a severity filter, and try a text highlight/filter.

## 3. Workspace and colcon

```bash
# Run in my VM: source the ROS installation for this terminal
source /opt/ros/rolling/setup.bash

# Run in my VM: create and enter the workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Run in my VM: clone the example source used in the slides
git clone https://github.com/ros2/examples src/examples -b rolling

# Run in my VM: build the workspace
colcon build --symlink-install

# Run in my VM: use the built workspace overlay
. install/setup.bash
```

After a successful build, `build/`, `install/`, and `log/` should appear beside `src/`. These directories are build artifacts and are intentionally not committed here.

### Alternative overlay workflow shown in the slides

```bash
# Run in my VM, from ~/ros2_ws/src
git clone https://github.com/ros/ros_tutorials.git -b rolling-devel
rosdep install -i --from-path src --rosdistro rolling -y

# Run in my VM, from ~/ros2_ws
colcon build
source /opt/ros/rolling/setup.bash
. install/local_setup.bash
```

The slide also asks the student to change `setWindowTitle("TurtleSim")` to `setWindowTitle("MyTurtleSim")` in `~/ros2_ws/src/ros_tutorials/turtlesim/src/turtle_frame.cpp`, rebuild, and run `ros2 run turtlesim turtlesim_node`. I will only report this as completed after doing it in my VM.

## 4. Python package

The `src/week4_activity` directory is a small `ament_python` package matching the package structure discussed in the slides.

```bash
# Run in my VM: copy this repository's src/week4_activity folder into ~/ros2_ws/src,
# then run:
source /opt/ros/rolling/setup.bash
cd ~/ros2_ws
colcon build --packages-select week4_activity
. install/local_setup.bash
ros2 run week4_activity my_node
```

Expected behavior after the final command: the node starts and logs a message. Capture the actual terminal output in `evidence/package-run.txt`.

## Evidence to add before submission

See [evidence/README.md](evidence/README.md). Add only your own VM output/screenshots; do not fabricate outputs.

## Files for I-Class

- [Command analysis](COMMAND_ANALYSIS.md)
- [Ready-to-paste I-Class post](I_CLASS_SUBMISSION.md)
- [Evidence checklist](evidence/README.md)

## Suggested GitHub submission steps

```bash
# Run in my VM or on the machine where this repository is stored
git add README.md COMMAND_ANALYSIS.md I_CLASS_SUBMISSION.md evidence src .gitignore
git commit -m "Add Week 4 ROS 2 activity"
git branch -M main
git remote add origin <MY_GITHUB_REPOSITORY_URL>
git push -u origin main
```

Replace `<MY_GITHUB_REPOSITORY_URL>` with the repository URL you create in your own GitHub account. Then paste that link into the I-Class discussion post.
