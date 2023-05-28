# Wikipedia Speedrun Solver

## Introduction

The Wikipedia speedrun game is a game in which a player is given two Wikipedia pages at random, one being the start page, and the other the end page, where the goal is to get from the start page to the end page in as few steps as possible, traveling between pages using hyperlinks. To try this game out, visit https://wikispeedruns.com/.

In this project, the goal is to find as optimized (both in number of steps and in "distance"... more on this later) of a solution to the Wikipedia speedrun game as possible. To do this, the following elements will be implemented:
- A "web scraping module" that will recursively scrape hyperlink data from Wikipedia. While all other parts of this project are implemented in C++, only this module will use Python (libraries used: requests, BeautifulSoup, and random).
- A weighted, directed graph data structure in which each node is a Wikipedia page hyperlink, and each weighted edge corresponds to the "distance" between the two hyperlinks (The "distance" between two hyperlinks is defined as the index of the second hyperlink out of all links scraped from the first link, divided by the total number of links scraped by that link. For instance, if we scrape a total of 100 hyperlinks from link A, and link B is the 34th link we scraped, the distance between A and B will be 34/100). 
- A "validation module" that, given the above graph data structure, will use Kosaraju's algorithm to determine if playing the game is possible. Since Kosaraju's algorithm finds strongly connected subgraphs, we will know if the game is playable (i.e. the two graph nodes are connected) based on the algorithm's success. This module is necessary because it will not be efficient to scrape all links in English Wikipedia, which means some links will not be present in our structure. 
- A series of graph optimization algorithms (A*, Kruskals) that will use the above validated graph structure to find the shortest path between the two given hyperlinks. The "distance" between hyperlinks will be used as the heuristic for A*.
