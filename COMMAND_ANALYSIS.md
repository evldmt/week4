# Week 4 ROS 2 Command Analysis

## Turtlesim

| Command | Analysis |
| --- | --- |
| `sudo apt update` | Refreshes the local APT package index, so the VM can see current package metadata before installation. `sudo` is required because this changes system package information. |
| `sudo apt install ros-rolling-turtlesim` | Installs the ROS 2 Rolling turtlesim package. Turtlesim is a lightweight graphical simulator used to learn how ROS 2 nodes and executables run. |
| `ros2 pkg executables turtlesim` | Queries the ROS 2 package index and lists executable programs exported by the `turtlesim` package. This verifies that ROS 2 can find the installed package and shows runnable executables such as the simulator and teleoperation tool. |
| `ros2 run turtlesim turtlesim_node` | Starts the `turtlesim_node` executable from the `turtlesim` package. This node creates the simulator window and participates in the ROS graph. |
| `ros2 run turtlesim turtle_teleop_key` | Starts the keyboard teleoperation executable. It reads keyboard arrows and sends movement commands to the simulator, demonstrating communication between ROS 2 nodes. |

## RQT

| Command | Analysis |
| --- | --- |
| `sudo apt install ~nros-rolling-rqt*` | Installs the Rolling RQT packages/plugins using the package expression shown in the slides. RQT provides graphical access to ROS 2 tools. |
| `rqt` | Opens the main RQT GUI. From this window, I can select **Plugins > Services > Service Caller** to inspect/call ROS 2 services through a graphical interface. |
| `ros2 run rqt_console rqt_console` | Runs RQT Console directly. It displays ROS 2 log messages and supports filtering by severity level and highlighting messages containing specified text. |

## Workspace and colcon

| Command | Analysis |
| --- | --- |
| `source /opt/ros/rolling/setup.bash` | Configures the current terminal to use the installed ROS 2 Rolling environment. It updates shell environment variables so ROS 2 commands and packages can be found. This must be repeated for each new terminal unless configured automatically. |
| `mkdir -p ~/ros2_ws/src` | Creates a ROS 2 workspace folder and its `src` directory. The `-p` option also creates missing parent directories and does not fail if they already exist. |
| `cd ~/ros2_ws` | Changes into the workspace root, where colcon will create the `build`, `install`, and `log` directories. |
| `git clone https://github.com/ros2/examples src/examples -b rolling` | Downloads the ROS 2 examples source branch for Rolling into the workspace source directory. This supplies packages for colcon to build. |
| `colcon build --symlink-install` | Builds packages in the workspace. Colcon performs out-of-source builds. `--symlink-install` uses symbolic links for installed files where appropriate, making edits to some source files easier to test during development. |
| `. install/setup.bash` | Sources the workspace setup file after building. It overlays the workspace on the base ROS installation, making executables and libraries built in the workspace available in this terminal. |
| `git clone https://github.com/ros/ros_tutorials.git -b rolling-devel` | Downloads the ROS tutorial source branch used by the alternative overlay exercise on the slides. |
| `rosdep install -i --from-path src --rosdistro rolling -y` | Resolves and installs missing system dependencies required by packages below the `src` directory for the specified Rolling distribution. `-i` ignores dependencies that are already satisfied, and `-y` accepts installation prompts. |
| `. install/local_setup.bash` | Sources this workspace's local overlay setup file. It adds the locally built packages while preserving access to the underlay ROS 2 installation. |

## Creating and using a package

| Command | Analysis |
| --- | --- |
| `cd ~/ros2_ws/src` | Moves to the workspace source directory. A ROS 2 package must be created here rather than inside another package, because nested packages are not supported. |
| `ros2 pkg create --build-type ament_python week4_activity` | Generates a Python-based ROS 2 package template named `week4_activity`. The `ament_python` build type creates package metadata and Python packaging files needed for colcon and ROS 2 tools. |
| `colcon build --packages-select week4_activity` | Builds only the named package, which is faster and isolates package-level build problems during testing. |
| `ros2 run week4_activity my_node` | Runs the `my_node` console entry point exported by the package after the workspace overlay has been sourced. |

## ROS 2 concepts observed in the activity

- A **node** is an executable with one focused responsibility. `turtlesim_node` and `turtle_teleop_key` are separate nodes.
- A **topic** supports continuous publisher-subscriber data exchange. Turtle teleoperation uses ongoing movement commands rather than one-time responses.
- A **service** uses a request-response pattern. RQT Service Caller provides a GUI to interact with available services.
- A **parameter** is a node-specific configuration value.
- An **action** is suitable for a longer task: it has a goal, feedback, and a result, and can be cancelled.
- The ROS 2 **graph** is the set of active nodes and their communication connections.

## Integrity note

This document explains the purpose of the commands from Week 4. Actual command output, screenshots, and any successful modification of turtlesim must be produced in my own VM and added to the repository before submission.
