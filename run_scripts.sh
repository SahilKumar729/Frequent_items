#!/bin/bash

# Start Zookeeper in a new terminal
gnome-terminal -- bash -c "cd kafka; ./bin/zookeeper-server-start.sh config/zookeeper.properties" &

# Start Kafka Server in a new terminal
gnome-terminal -- bash -c "cd kafka; ./bin/kafka-server-start.sh config/server.properties" &

# Run Approri.py in a new terminal
gnome-terminal -- bash -c "cd Documents/Asg03; python3 Approri.py"  &

# Run PCY.py in a new terminal
gnome-terminal -- bash -c "cd Documents/Asg03; python3 PCY.py" &

# Run producer.py in a new terminal
gnome-terminal -- bash -c "cd Documents/Asg03; python3 producer.py" &

# Run SearchProduct.py in a new terminal
gnome-terminal -- bash -c "cd Documents/Asg03; python3 SearchProduct.py"

