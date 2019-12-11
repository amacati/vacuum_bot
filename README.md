# vacuum\_bot

## Functionality

The package contains the vacuum\_bot model and launch files to start a Gazebo simulation with the vacuum\_bot\_gazebo and vacuum\_bot\_moveit\_config package.

To test the model with MoveIt!, simply launch
'roslaunch vacuum\_bot vacuum\_bot.launch'

## Known Issues

In case Gazebo dies with a 'minimum corner of the box' exception, use the my\_flat\_safe.world file in the vacuum\_bot\_gazebo package launchfile to start the simulation. The kitchen model causes problems on some computers or Gazebo versions.

If Gazebo can't start because of a bad X drawable, quit and relaunch. This is a bug with Gazebo, I don't know of any fix on the package side.

Gazebo might also crash when restarting it after a forced shutdown. In that case, wait 10 seconds until you relaunch Gazebo.

In case any of the nodes dies, just restart the whole vacuum\_bot.launch process.

If MoveIt! shows all robot arm links in the center of the RVIZ scene, the robot (naturally) always detects a collision when planning movements. This bug is caused by the computers language settings and can be resolved by executing the following command in the terminal.

`export LC_NUMERIC="en_US.UTF-8"`

This has to be done everytime a new terminal is opened, or you have to add it to your .bashrc.

MoveIt! collision aware planning may also fail if your robot is configured with continuous joints instead of revolute joints with limited range. This is an issue with MoveIt! and can only be adressed by limiting the joints to lower and upper limits.

## Website

Additional information for TUM members can be found on the [RoVi Wiki](https://wiki.lmt.ei.tum.de/intern:lmt:all:rovi:students:2019_schuck).
