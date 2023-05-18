# Wikipedia Speedrun Solver: Intro

The Wikipedia speedrun game is a game in which a player is given two Wikipedia pages at random, one being the start page, and the other the end page, where the goal is to get from the start page to the end page in as few steps as possible, traveling between pages using hyperlinks. To try this game out, see https://wikispeedruns.com/.

In this project, the goal is to use various algorithms to find as optimized (both in number of steps and in "distance"... more on this later) of a solution to the Wikipedia speedrun game as possible. To do this, the following elements will be implemented:
- A "web scraping module" that will recursively scrape hyperlink data from Wikipedia. While all other parts of this project are implemented in C++, only this module will use the Selenium Python library.
- A weighted graph data structure in which each node is a Wikipedia page hyperlink, and each weighted edge corresponds to the "distance" between the two hyperlinks.     -> The "distance" between two hyperlinks is defined as the number of lines of text between the top of the page of the first hyperlink and the location on that          same page where the second hyperlink is linked.
- A "validation module" that, given the above graph data structure, will use Kosaraju's algorithm to determine if playing the game is possible
    -> Since Kosaraju's algorithm finds strongly connected subgraphs, we will know if the game is playable (i.e. the two graph nodes are connected) based on the            algorithm's success.
- A series of graph optimization algorithms (A*? Kruskals? decide later lol) that will use the above validated graph structure to find the shortest path between two   given hyperlinks
