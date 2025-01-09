#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include "math.h"
#include "unistd.h"
#include "iostream"

#include <sstream>

ros::Publisher move_pub;

//void posCallback(const std_msgs::String::ConstPtr& msg)
//{
//  ROS_INFO("I heard: [%s]", msg->data.c_str());
//}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "turtle_controller");

	ros::NodeHandle n;
  
	// ros::Subscriber sub = n.subscribe("chatter", 1000, posCallback);

	move_pub = n.advertise<geometry_msgs::Twist>("/turtlesim1/turtle1/cmd_vel", 1);

	ros::Rate loop_rate(0.5);

	geometry_msgs::Twist movement;
	
	float theta = M_PI/2;
	float d_theta = 4*M_PI/3;
	//float d_theta = 0;
	int distance = 4;

  	int i = 0;
  	int j = 0;
  	int k = 2;
  	
  	float offset = M_PI/6;

	sleep(2);

  	while (ros::ok())
  	{
  		// Leg 1 (Start)
		movement.linear.x = distance*cos(theta);
		movement.linear.y = distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta + d_theta;
		sleep(2);

		// Leg 2 (Connection 1)
		movement.linear.x = distance*cos(theta);
		movement.linear.y = distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta + d_theta;
		sleep(2);

		// Leg 3 (Long 1)
		movement.linear.x = 2*distance*cos(theta);
		movement.linear.y = 2*distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta + d_theta;
		sleep(2);

		// Leg 4 (Connection 2)
		movement.linear.x = distance*cos(theta);
		movement.linear.y = distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta + d_theta;
		sleep(2);

		// Leg 5 (Long 2)
		movement.linear.x = 2*distance*cos(theta);
		movement.linear.y = 2*distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta + d_theta;
		sleep(2);

		// Leg 6 (Connection 3)
		movement.linear.x = distance*cos(theta);
		movement.linear.y = distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta + d_theta;
		sleep(2);

		// Leg 7 (End)
		movement.linear.x = distance*cos(theta);
		movement.linear.y = distance*sin(theta);
	
		move_pub.publish(movement);

		theta = theta - offset;
		sleep(2);

    	ros::spinOnce();

    	loop_rate.sleep();
  	}


  	return 0;
}
