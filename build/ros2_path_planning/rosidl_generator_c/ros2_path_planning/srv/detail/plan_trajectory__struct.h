// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros2_path_planning:srv/PlanTrajectory.idl
// generated code does not contain a copyright notice

#ifndef ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__STRUCT_H_
#define ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'robot_position'
// Member 'target_position'
#include "geometry_msgs/msg/detail/pose__struct.h"
// Member 'grid_map'
#include "nav_msgs/msg/detail/occupancy_grid__struct.h"

/// Struct defined in srv/PlanTrajectory in the package ros2_path_planning.
typedef struct ros2_path_planning__srv__PlanTrajectory_Request
{
  geometry_msgs__msg__Pose robot_position;
  geometry_msgs__msg__Pose target_position;
  nav_msgs__msg__OccupancyGrid grid_map;
} ros2_path_planning__srv__PlanTrajectory_Request;

// Struct for a sequence of ros2_path_planning__srv__PlanTrajectory_Request.
typedef struct ros2_path_planning__srv__PlanTrajectory_Request__Sequence
{
  ros2_path_planning__srv__PlanTrajectory_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_path_planning__srv__PlanTrajectory_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'trajectory'
// already included above
// #include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in srv/PlanTrajectory in the package ros2_path_planning.
typedef struct ros2_path_planning__srv__PlanTrajectory_Response
{
  geometry_msgs__msg__Pose__Sequence trajectory;
} ros2_path_planning__srv__PlanTrajectory_Response;

// Struct for a sequence of ros2_path_planning__srv__PlanTrajectory_Response.
typedef struct ros2_path_planning__srv__PlanTrajectory_Response__Sequence
{
  ros2_path_planning__srv__PlanTrajectory_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros2_path_planning__srv__PlanTrajectory_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__STRUCT_H_
