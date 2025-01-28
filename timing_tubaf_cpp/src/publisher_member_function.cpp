// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

class NumberPublisher : public rclcpp::Node
{
public:
  NumberPublisher() : Node("number_publisher"), counter_(0)
  {
    // Publisher für "number" erstellen
    publisher_ = this->create_publisher<std_msgs::msg::Int32>("number", 10);

    // Timer, um alle 1 Sekunde eine Nachricht zu veröffentlichen
    timer_ = this->create_wall_timer(
      std::chrono::seconds(1), std::bind(&NumberPublisher::publish_number, this));
  }

private:
  // Methode zum Veröffentlichen der Nachricht
  void publish_number()
  {
    auto message = std_msgs::msg::Int32();
    message.data = counter_;  // Setze den Wert der Nachricht auf den aktuellen Zählerstand

    RCLCPP_INFO(this->get_logger(), "Publishing: '%d'", message.data);

    // Nachricht veröffentlichen
    publisher_->publish(message);

    // Zähler um 1 erhöhen
    counter_++;
  }

  // Publisher-Objekt und Timer
  rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;

  // Zähler für den Wert von 'number'
  int counter_;
};

int main(int argc, char **argv)
{
  // ROS 2 Initialisierung
  rclcpp::init(argc, argv);

  // Erstelle den Publisher-Node
  rclcpp::spin(std::make_shared<NumberPublisher>());

  // ROS 2 Shutdown
  rclcpp::shutdown();
  return 0;
}
