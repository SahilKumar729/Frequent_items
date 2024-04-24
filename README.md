# Frequent Itemset Mining and Product Search on Kafka Stream

## Contribution
This project exists thanks to the extraordinary people who contributed to it.
-  Muhammad Daniyal Haider (i222042@nu.edu.pk)
-  Muhammad Anas Khan (i221987@nu.edu.pk)


## Introduction

In today's data-driven world, businesses across various domains rely on analyzing large volumes of data to derive meaningful insights and make informed decisions. This project addresses the need for real-time data processing and analysis by implementing frequent itemset mining and product search functionalities on a Kafka stream.

**Frequent Itemset Mining**: Frequent itemset mining is a fundamental task in data mining, where the goal is to discover sets of items that frequently occur together in transactional datasets. These frequent itemsets provide valuable insights into the relationships and patterns present in the data.

**Product Search**: Product search functionality allows users to query a dataset based on specific criteria, such as product category or keywords. This enables users to quickly find relevant products that match their search criteria, enhancing the overall user experience.

The system architecture comprises several components, each playing a crucial role in the overall data processing pipeline:

1. **Data Sampling**: The input data, typically large-scale and unstructured, is sampled to a manageable size to facilitate efficient processing.

2. **Data Cleaning**: The sampled data is cleaned and preprocessed to remove noise and irrelevant information, ensuring high data quality for subsequent analysis.

3. **Kafka Producer**: The cleaned data is streamed onto Kafka topics in real-time, enabling seamless integration with downstream consumers for further processing.

4. **Frequent Itemset Mining**: Two algorithms, namely Apriori and PCY (Park-Chen-Yu), are implemented to perform frequent itemset mining on the Kafka stream. These algorithms identify sets of items that frequently occur together, providing valuable insights into customer purchasing patterns.

5. **Product Search**: A consumer script allows users to search for products based on specific criteria, such as product category or keywords. This functionality enhances user experience by enabling quick and efficient product discovery.

The project offers a scalable and efficient solution for real-time data processing and analysis, making it suitable for a wide range of applications across industries such as e-commerce, retail, and finance. By leveraging Apache Kafka for real-time data streaming and MongoDB for storing frequent itemsets, the system provides a robust and reliable platform for deriving actionable insights from streaming data.

## Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation and Setup](#installation-and-setup)
- [mangodb usgae](#MongoDB-Usage)
- [Advantages](#Advantages)
- [Usage](#usage)
    - [Data Preparation](#data-preparation)
    - [Start Kafka](#start-kafka)
    - [Produce Data](#produce-data)
    - [Consume Data](#consume-data)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Potential Improvements](#potential-improvements)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)


## Features

- Scalable and efficient processing of large-scale data streams.
- Real-time data streaming and processing using Apache Kafka.
- Implementation of Apriori and PCY algorithms for frequent itemset mining.
- Product search functionality based on user-specified criteria.
- Automated execution of data processing pipeline using a bash script.

## Dependencies

- Apache Kafka
- Python 3.x
- pymongo
- nltk
- tqdm

## Installation and Setup

1. **Kafka Installation**: Install Apache Kafka by following the instructions [here](link_to_kafka_installation_instructions).
2. **Python Dependencies**: Install Python dependencies using pip:

    ```
    pip install kafka-python pymongo nltk tqdm
    ```

3. **Clone Repository**: Clone this repository to your local machine:

    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

4. **Download NLTK Resources**: Download NLTK resources for text preprocessing:

    ```
    python -m nltk.downloader stopwords
    ```

5. **Configure Kafka**: Update Kafka configuration (`config/server.properties`) to match your environment settings.

   
### MongoDB Usage

This project utilizes MongoDB as a database for storing frequent itemsets. MongoDB is a popular NoSQL database known for its flexibility, scalability, and ease of use. By leveraging MongoDB in this assignment, we benefit from:

- **Schemaless Design**: MongoDB's flexible schema allows us to store and retrieve complex data structures without predefined schemas, making it well-suited for handling diverse and evolving data types.
- **Scalability**: MongoDB's horizontal scaling capabilities enable seamless scaling of database clusters to accommodate growing data volumes and user loads.
- **High Performance**: MongoDB's architecture is optimized for high throughput and low latency, ensuring fast read and write operations even with large datasets.
- **Rich Querying Capabilities**: MongoDB supports powerful query languages and indexing mechanisms, enabling efficient retrieval of relevant data based on various criteria.
- **Real-time Analytics**: MongoDB's integration with Kafka and other real-time data processing frameworks facilitates real-time analytics and insights generation from streaming data sources.

### Advantages

- **Real-time Data Processing**: The use of Apache Kafka for real-time data streaming and MongoDB for storing frequent itemsets enables efficient real-time data processing and analysis.
- **Scalability and Performance**: Leveraging distributed computing technologies like Kafka and MongoDB ensures scalability and high performance, making the system suitable for processing large-scale datasets.
- **Flexibility and Modularity**: The modular architecture of the system allows for easy customization and extension, enabling developers to adapt the system to specific use cases and requirements.
- **Actionable Insights**: By performing frequent itemset mining and product search on streaming data, the system provides valuable insights into customer behavior and preferences, enabling businesses to make data-driven decisions and enhance user experience.


## Usage

### Data Preparation

- Run `data_sampler.py` to sample the input data to the desired size.
- Run `data_cleaner.py` to clean the sampled data and select specific columns.

### Start Kafka

Start Zookeeper and Kafka server using the provided bash script:`./run.sh`


### Produce Data

Run `producer.py` to stream the cleaned data onto Kafka topics.

### Consume Data

Run each consumer script (`Approri.py`, `PCY.py`, `SearchProduct.py`) in separate terminals to perform frequent itemset mining and product search functionalities.

## Configuration

- Adjust batch sizes, window sizes, and minimum support thresholds in consumer scripts for optimal performance.
- Customize MongoDB connection settings in consumer scripts (`Approri.py` and `PCY.py`) to match your MongoDB configuration.

## Troubleshooting

- Ensure Kafka and Zookeeper are running and properly configured.
- Check for any errors in the consumer logs (`Approri.py`, `PCY.py`, `SearchProduct.py`) for debugging purposes.
- Verify that MongoDB is accessible and configured correctly for storing frequent itemsets.

## Potential Improvements

- Implement dynamic adjustment of batch sizes and minimum support thresholds based on data characteristics.
- Enhance search functionality to support more complex queries and incorporate fuzzy matching for better results.
- Optimize data preprocessing and cleaning steps for improved efficiency.
- Implement real-time visualization of frequent itemsets and search results using visualization libraries like Plotly or Matplotlib.

## Contributing

Contributions are welcome! Feel free to open issues for any bugs or feature requests, or submit pull requests to contribute enhancements or fixes.


## Acknowledgements

Special thanks to the Apache Kafka and MongoDB communities for their excellent documentation and support.

## Contact

For any inquiries or assistance, please contact sahil.r.kumar11@gmail.com.
