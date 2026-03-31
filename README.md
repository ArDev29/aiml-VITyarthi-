# Route Evaluator

A simple Python program that finds a travel route between two Indian cities using graph search.

You type in where you are and where you want to go — it figures out a path.

---

## What This Project Does

The program reads a dataset of Indian city connections, builds a graph out of those connections, and then uses **Depth First Search (DFS)** to find a route from your chosen start city to your destination.

It prints the full list of cities you would pass through, in order.

This is not a GPS or a maps app. Think of it as a transparent, educational demonstration of how graph traversal works — using real Indian cities as the data.

---

## How It Works (The Short Version)

1. The dataset is loaded — it contains city pairs and the road distances between them
2. A graph is built internally as an **adjacency list** (a dictionary of city → neighbours)
3. DFS explores the graph, going as deep as possible along each path until it finds the destination
4. The route is printed as a sequence of cities connected by arrows

---

## Project Structure

```
Route-Evaluator/
│
├── data/
│   └── indian-cities-dataset.csv   ← the city connections data
│
├── route_evaluator.py              ← the main program
└── README.md                       ← this file
```

---

## Requirements

- Python 3.x
- pandas library

If you do not have pandas installed, run this once:

```bash
pip install pandas
```

---

## How to Set It Up

**Step 1 — Clone or download this repository**

```bash
git clone https://github.com/Abhyuday-Pratap-Singh/VityarthiProjectAIML.git
cd Route-Evaluator
```

**Step 2 — Install the dependency**

```bash
pip install pandas
```

**Step 3 — Run the program**

```bash
python route_evaluator.py
```

That is it. No configuration needed.

---

## How to Use It

When you run the program, it will first show you all the cities available in the dataset:

```
Available Cities: Agra, Ahmedabad, Bengaluru, Bhopal, Chennai, Delhi ...
```

Then it will ask you two questions:

```
Enter start city: Agra
Enter end city: Delhi
```

And it will print the route:

```
--- Pathfinding from Agra to Delhi ---
DFS Path: Agra -> Delhi
```

If cities are connected through other cities, you will see the full chain:

```
DFS Path: Bengaluru -> Pune -> Mumbai
```

> **Tip:** City names are case-insensitive. Typing `agra`, `Agra`, or `AGRA` all work the same way.

---

## Important Note About the Route

DFS finds **a valid path**, not necessarily the shortest one. The path it returns is the first complete route it discovers while exploring the graph. Different search strategies (like Dijkstra's algorithm) would be needed to guarantee the shortest distance.

---

## Dataset

The dataset (`indian-cities-dataset.csv`) contains road connections between major Indian cities with three columns:

| Column | Description |
|---|---|
| Origin | The starting city |
| Destination | The connected city |
| Distance | Road distance in kilometres |

The graph is **directed** — a connection from City A to City B does not automatically mean there is one from B to A. This reflects how the data was originally recorded.

---

## Possible Future Improvements

- Add Dijkstra's algorithm to find the actual shortest path by distance
- Make the graph bidirectional so routes work in both directions
- Add a simple command-line interface with flags for start and end cities
- Show the total distance of the route, not just the city names

---

## Course Context

This project was built as part of a Fundamentals in AIML course. It demonstrates graph construction using adjacency lists and graph traversal using recursive DFS — both of which are core topics in the course.
