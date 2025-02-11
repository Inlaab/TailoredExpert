# TailoredExpert Project

## Overview
The TailoredExpert project aims to build an AI agent capable of handling natural language interactions, emulating human customer service. The project utilizes a graph-based data structure to manage knowledge and facilitate effective responses.

## Project Structure
```
TailoredExpert
├── src
│   ├── main.py          # Main entry point of the project
│   └── agente_ia.py     # Definition of the AI agent class
├── kb
│   └── conocimiento.json # Knowledge data in JSON format
├── grafo.py             # Graph data structure implementation
├── README.md            # Project documentation
└── setup_ini.py         # Initial project setup script
```

## RAG Approach
The project implements the RAG (Retrieve-Augment-Generate) approach, which allows the AI agent to provide accurate and useful responses. This is achieved through the following steps:

1. **Retrieve**: The agent retrieves relevant information from the graph data structure defined in `grafo.py`.
2. **Augment**: The retrieved information is enriched with additional calculations and validations to ensure accuracy and relevance.
3. **Generate**: Finally, the agent generates a clear and understandable response for the user.

## Usage
To run the project, execute the `main.py` file located in the `src` directory. This will initialize the graph and the AI agent, allowing for user interaction.

## Setup
To set up the project environment, run the `setup_ini.py` script. This will create the necessary directories and files required for the project.

## Knowledge Base
The knowledge base is stored in `kb/conocimiento.json`, which contains structured data that the AI agent utilizes to enhance its responses.

## Contribution
Contributions to the project are welcome. Please follow the standard practices for contributing to open-source projects.

