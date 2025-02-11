# Map-Matching

## Overview

This file is a Jupyter notebook, developed as part of a project at Sharif University of Technology. The primary objective of this project is to implement a denoising algorithm for GPS data, particularly in urban environments where GPS signals can be unreliable due to noise. The script focuses on simulating GPS noise, applying a Hidden Markov Model (HMM) for denoising, and visualizing the results.

## Key Components

1. **Environment Setup**:
   - The script begins by importing necessary libraries such as `numpy`, `pandas`, `matplotlib`, and `keplergl` for data manipulation and visualization.

2. **Introduction**:
   - It introduces the problem of GPS noise and its implications for applications like ride-hailing services, emphasizing the need for accurate GPS data.

3. **Data Loading**:
   - The code loads two datasets:
     - `pasdaran_streets.csv`: Contains information about streets, including node pairs, lengths, and one-way restrictions.
     - `pasdaran_nodes.csv`: Contains GPS coordinates of various nodes.

4. **Trip Creation**:
   - Functions are defined to create trips by selecting random start and end points from the nodes and finding the shortest path using a custom implementation of Dijkstra's algorithm.

5. **Ride Simulation**:
   - A function simulates a ride based on parameters like speed and GPS reporting time, generating intermediate GPS coordinates along the path.

6. **GPS Noise Simulation**:
   - The code includes functions to add random noise to the GPS coordinates using different statistical distributions:
     - Uniform Noise
     - Normal Distribution Noise
     - Mixed Noise

7. **Visualization**:
   - It utilizes `keplergl` for interactive map visualizations and `matplotlib` for plotting the effects of noise on the rides.

8. **Denoising with HMM**:
   - The HMM is implemented to denoise GPS locations, treating streets as hidden states and noisy GPS points as observations. The Viterbi algorithm is used to derive the most probable sequence of hidden states.

9. **Testing and Evaluation**:
   - The code concludes with a section for testing the HMM model using provided noisy and original datasets, calculating the Mean Haversine Distance (MHD) to evaluate denoising performance.

## Functions Defined

- **find_shotest_path**: Finds the shortest path between two nodes.
- **dijkstra**: Implements Dijkstra's algorithm for pathfinding.
- **calculate_distance**: Computes the distance between two geographical points.
- **visualize_a_ride**: Generates GPS coordinates for a simulated ride.
- **add_uniform_gps_noise**: Adds uniform noise to GPS coordinates.
- **add_normal_gps_noise**: Adds normal distribution noise to GPS coordinates.
- **add_mixed_gps_noise**: Combines different noise types to GPS coordinates.
- **process_trip_data**: Applies the HMM to denoise GPS data and calculates the average distance error.

## Data Structure

### Datasets

1. **`pasdaran_streets.csv`**:
   - Columns: `u`, `v`, `length`, `one_way`
   - Represents edges in the graph with lengths and directionality.

2. **`pasdaran_nodes.csv`**:
   - Columns: `id`, `lat`, `lon`
   - Represents nodes with their respective GPS coordinates.

### Output File

- **`out.csv`**:
  - Contains the denoised GPS data with columns for `trip_id`, `lat`, `lon`, and other relevant metadata.

## Conclusion

The project serves as a foundational component for developing a robust GPS data denoising algorithm using Hidden Markov Models. It includes essential functionalities for data loading, processing, noise simulation, and visualization, making it a comprehensive resource for further development in the project.
