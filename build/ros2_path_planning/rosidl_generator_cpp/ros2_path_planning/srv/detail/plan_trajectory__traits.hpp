// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ros2_path_planning:srv/PlanTrajectory.idl
// generated code does not contain a copyright notice

#ifndef ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__TRAITS_HPP_
#define ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ros2_path_planning/srv/detail/plan_trajectory__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'robot_position'
// Member 'target_position'
#include "geometry_msgs/msg/detail/pose__traits.hpp"
// Member 'grid_map'
#include "nav_msgs/msg/detail/occupancy_grid__traits.hpp"

namespace ros2_path_planning
{

namespace srv
{

inline void to_flow_style_yaml(
  const PlanTrajectory_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_position
  {
    out << "robot_position: ";
    to_flow_style_yaml(msg.robot_position, out);
    out << ", ";
  }

  // member: target_position
  {
    out << "target_position: ";
    to_flow_style_yaml(msg.target_position, out);
    out << ", ";
  }

  // member: grid_map
  {
    out << "grid_map: ";
    to_flow_style_yaml(msg.grid_map, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PlanTrajectory_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_position:\n";
    to_block_style_yaml(msg.robot_position, out, indentation + 2);
  }

  // member: target_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_position:\n";
    to_block_style_yaml(msg.target_position, out, indentation + 2);
  }

  // member: grid_map
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "grid_map:\n";
    to_block_style_yaml(msg.grid_map, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PlanTrajectory_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ros2_path_planning

namespace rosidl_generator_traits
{

[[deprecated("use ros2_path_planning::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros2_path_planning::srv::PlanTrajectory_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_path_planning::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_path_planning::srv::to_yaml() instead")]]
inline std::string to_yaml(const ros2_path_planning::srv::PlanTrajectory_Request & msg)
{
  return ros2_path_planning::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_path_planning::srv::PlanTrajectory_Request>()
{
  return "ros2_path_planning::srv::PlanTrajectory_Request";
}

template<>
inline const char * name<ros2_path_planning::srv::PlanTrajectory_Request>()
{
  return "ros2_path_planning/srv/PlanTrajectory_Request";
}

template<>
struct has_fixed_size<ros2_path_planning::srv::PlanTrajectory_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Pose>::value && has_fixed_size<nav_msgs::msg::OccupancyGrid>::value> {};

template<>
struct has_bounded_size<ros2_path_planning::srv::PlanTrajectory_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Pose>::value && has_bounded_size<nav_msgs::msg::OccupancyGrid>::value> {};

template<>
struct is_message<ros2_path_planning::srv::PlanTrajectory_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'trajectory'
// already included above
// #include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace ros2_path_planning
{

namespace srv
{

inline void to_flow_style_yaml(
  const PlanTrajectory_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: trajectory
  {
    if (msg.trajectory.size() == 0) {
      out << "trajectory: []";
    } else {
      out << "trajectory: [";
      size_t pending_items = msg.trajectory.size();
      for (auto item : msg.trajectory) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PlanTrajectory_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: trajectory
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.trajectory.size() == 0) {
      out << "trajectory: []\n";
    } else {
      out << "trajectory:\n";
      for (auto item : msg.trajectory) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PlanTrajectory_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ros2_path_planning

namespace rosidl_generator_traits
{

[[deprecated("use ros2_path_planning::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ros2_path_planning::srv::PlanTrajectory_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ros2_path_planning::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ros2_path_planning::srv::to_yaml() instead")]]
inline std::string to_yaml(const ros2_path_planning::srv::PlanTrajectory_Response & msg)
{
  return ros2_path_planning::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ros2_path_planning::srv::PlanTrajectory_Response>()
{
  return "ros2_path_planning::srv::PlanTrajectory_Response";
}

template<>
inline const char * name<ros2_path_planning::srv::PlanTrajectory_Response>()
{
  return "ros2_path_planning/srv/PlanTrajectory_Response";
}

template<>
struct has_fixed_size<ros2_path_planning::srv::PlanTrajectory_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ros2_path_planning::srv::PlanTrajectory_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ros2_path_planning::srv::PlanTrajectory_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ros2_path_planning::srv::PlanTrajectory>()
{
  return "ros2_path_planning::srv::PlanTrajectory";
}

template<>
inline const char * name<ros2_path_planning::srv::PlanTrajectory>()
{
  return "ros2_path_planning/srv/PlanTrajectory";
}

template<>
struct has_fixed_size<ros2_path_planning::srv::PlanTrajectory>
  : std::integral_constant<
    bool,
    has_fixed_size<ros2_path_planning::srv::PlanTrajectory_Request>::value &&
    has_fixed_size<ros2_path_planning::srv::PlanTrajectory_Response>::value
  >
{
};

template<>
struct has_bounded_size<ros2_path_planning::srv::PlanTrajectory>
  : std::integral_constant<
    bool,
    has_bounded_size<ros2_path_planning::srv::PlanTrajectory_Request>::value &&
    has_bounded_size<ros2_path_planning::srv::PlanTrajectory_Response>::value
  >
{
};

template<>
struct is_service<ros2_path_planning::srv::PlanTrajectory>
  : std::true_type
{
};

template<>
struct is_service_request<ros2_path_planning::srv::PlanTrajectory_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ros2_path_planning::srv::PlanTrajectory_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__TRAITS_HPP_
