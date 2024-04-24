# Frequent Itemset Mining and Product Search on Kafka Stream

## Introduction

This project implements frequent itemset mining and product search functionalities on a Kafka stream. It leverages Apache Kafka for real-time data streaming and MongoDB for storing frequent itemsets. The system consists of several components including data sampling, data cleaning, Kafka producer, frequent itemset mining using the Apriori algorithm (Consumer 1), frequent itemset mining using the PCY algorithm (Consumer 2), and product search (Consumer 3).

## Features

- Sampling and cleaning of large-scale data.
- Real-time streaming of cleaned data to Kafka topics.
- Frequent itemset mining using both the Apriori and PCY algorithms.
- Product search functionality based on user-specified category.
- Automated execution of all components using a bash script.

## Dependencies

- Apache Kafka
- Python 3.x
- pymongo
- nltk
- tqdm

## Installation and Setup

1. **Kafka Installation**: Install Apache Kafka by following the instructions [here](link_to_kafka_installation_instructions).
2. **Python Dependencies**: Install Python dependencies using pip:

    ```bash
    pip install kafka-python pymongo nltk tqdm
    ```

3. **Clone Repository**: Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

4. **Download NLTK Resources**: Download NLTK resources for text preprocessing:

    ```bash
    python -m nltk.downloader stopwords
    ```

5. **Configure Kafka**: Update Kafka configuration (`config/server.properties`) to match your environment settings.

## Usage

### Data Preparation

- Run `data_sampler.py` to sample the input data to the desired size.
- Run `data_cleaner.py` to clean the sampled data and select specific columns.

### Start Kafka

Start Zookeeper and Kafka server using the provided bash script:

```bash
./run.sh

Produce Data
Run producer.py to stream the cleaned data onto Kafka topics.

Consume Data
Run each consumer script (Approri.py, PCY.py, SearchProduct.py) in separate terminals to perform frequent itemset mining and product search functionalities.

Configuration
Adjust batch sizes, window sizes, and minimum support thresholds in consumer scripts for optimal performance.
Customize MongoDB connection settings in consumer scripts (Approri.py and PCY.py) to match your MongoDB configuration.
Troubleshooting
Ensure Kafka and Zookeeper are running and properly configured.
Check for any errors in the consumer logs (Approri.py, PCY.py, SearchProduct.py) for debugging purposes.
Verify that MongoDB is accessible and configured correctly for storing frequent itemsets.
Potential Improvements
Implement dynamic adjustment of batch sizes and minimum support thresholds based on data characteristics.
Enhance search functionality to support more complex queries and incorporate fuzzy matching for better results.
Optimize data preprocessing and cleaning steps for improved efficiency.
Implement real-time visualization of frequent itemsets and search results using visualization libraries like Plotly or Matplotlib.
Contributing
Contributions are welcome! Feel free to open issues for any bugs or feature requests, or submit pull requests to contribute enhancements or fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to the Apache Kafka and MongoDB communities for their excellent documentation and support.

Contact
For any inquiries or assistance, please contact sahil.r.kumar11@gmail.com.
