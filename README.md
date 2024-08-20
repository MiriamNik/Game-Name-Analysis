# Game Name Generator
## Project Overview

This project is a game name generator developed using a Markov chain model. It analyzes mobile games from the Google Play Store, focusing on genre distributions, ratings, game sizes, and more. The goal is to explore trends in game naming and generate potential names based on existing ones.

## Table of Contents
1. Project Structure
2. Usage
3. How to View

## Project Structure

The project is organized into the following directories:

* data/: Contains the dataset (googleplaystore.csv).
* images/: Contains generated plots and images.
* src/: Contains source code for data preprocessing, Markov chain generation, and analysis scripts.
* notebooks/: Contains the Jupyter notebook (game_name_generator.ipynb).

## Usage
### Jupyter Notebook

The main analysis and visualizations are contained in the Jupyter notebook:

Open the notebooks/game_name_generator.ipynb file in Jupyter Notebook.
The notebook is fully executed, so you can directly explore the outputs and visualizations without needing to rerun the cells.

### Source Code
The src/ directory contains scripts for:

* Data Preprocessing: Cleaning and preparing the dataset for analysis.
* Text Preprocessing: Cleaning and preapering the words from the dataset.
* Markov Chain Generation: Building a model to generate new game names based on existing data.
* Markov Chain Visualization: Create a plot to showcase the process of the name generator. 

These scripts are modular and can be adapted for similar projects or datasets.

## How to View
Simply open the notebook (game_name_generator.ipynb) on GitHub or download it and open it using Jupyter Notebook or any compatible viewer. No additional installation or dependencies are required.
