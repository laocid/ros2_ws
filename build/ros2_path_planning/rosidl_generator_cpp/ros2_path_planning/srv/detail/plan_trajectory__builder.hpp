// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros2_path_planning:srv/PlanTrajectory.idl
// generated code does not contain a copyright notice

#ifndef ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__BUILDER_HPP_
#define ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros2_path_planning/srv/detail/plan_trajectory__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros2_path_planning
{

namespace srv
{

namespace builder
{

class Init_PlanTrajectory_Request_grid_map
{
public:
  explicit Init_PlanTrajectory_Request_grid_map(::ros2_path_planning::srv::PlanTrajectory_Request & msg)
  : msg_(msg)
  {}
  ::ros2_path_planning::srv::PlanTrajectory_Request grid_map(::ros2_path_planning::srv::PlanTrajectory_Request::_grid_map_type arg)
  {
    msg_.grid_map = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_path_planning::srv::PlanTrajectory_Request msg_;
};

class Init_PlanTrajectory_Request_target_position
{
public:
  explicit Init_PlanTrajectory_Request_target_position(::ros2_path_planning::srv::PlanTrajectory_Request & msg)
  : msg_(msg)
  {}
  Init_PlanTrajectory_Request_grid_map target_position(::ros2_path_planning::srv::PlanTrajectory_Request::_target_position_type arg)
  {
    msg_.target_position = std::move(arg);
    return Init_PlanTrajectory_Request_grid_map(msg_);
  }

private:
  ::ros2_path_planning::srv::PlanTrajectory_Request msg_;
};

class Init_PlanTrajectory_Request_robot_position
{
public:
  Init_PlanTrajectory_Request_robot_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PlanTrajectory_Request_target_position robot_position(::ros2_path_planning::srv::PlanTrajectory_Request::_robot_position_type arg)
  {
    msg_.robot_position = std::move(arg);
    return Init_PlanTrajectory_Request_target_position(msg_);
  }

private:
  ::ros2_path_planning::srv::PlanTrajectory_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_path_planning::srv::PlanTrajectory_Request>()
{
  return ros2_path_planning::srv::builder::Init_PlanTrajectory_Request_robot_position();
}

}  // namespace ros2_path_planning


namespace ros2_path_planning
{

namespace srv
{

namespace builder
{

class Init_PlanTrajectory_Response_trajectory
{
public:
  Init_PlanTrajectory_Response_trajectory()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ros2_path_planning::srv::PlanTrajectory_Response trajectory(::ros2_path_planning::srv::PlanTrajectory_Response::_trajectory_type arg)
  {
    msg_.trajectory = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros2_path_planning::srv::PlanTrajectory_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros2_path_planning::srv::PlanTrajectory_Response>()
{
  return ros2_path_planning::srv::builder::Init_PlanTrajectory_Response_trajectory();
}

}  // namespace ros2_path_planning

#endif  // ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__BUILDER_HPP_
