# Dice Duel Showdown: FIFTY or BUST 🎲

## Project Overview
Dice Duel Showdown is a strategic, turn-based dice game where a player competes against a probability-based AI. The goal is to reach a score as close to **50** as possible without going over ("busting"). 

This repository contains three implementations of the game logic, demonstrating proficiency in **Web Development**, **Python scripting**, and **Object-Oriented Java programming**.

## 🎮 Play the Web Version
**[Click Here to Play the Game Online](https://draggle.github.io/dice-duel-showdown/)**

## Features & Rules
* **Objective:** Reach 50 points. Exact 50 wins instantly. Over 50 loses instantly.
* **Rounds:** Max 10 rounds. Closest to 50 wins if no one hits it exactly.
* **Doubles Penalty:** Rolling doubles causes the *opponent* to lose 10 points.
* **Resource Management:** Players unlock "Skips" after reaching 40 points to strategically avoid busting.
* **AI Opponent:** The computer utilizes a probabilistic approach, with a 30% chance to skip turns when near the target score.

## 📂 Repository Structure

### 1. Web Application (`/web-app`)
* **Tech Stack:** HTML5, CSS3 (Tailwind), JavaScript (ES6).
* **Highlights:**
    * Responsive UI with CSS Grid/Flexbox.
    * Custom Sound Engine using the Web Audio API (Real-time synthesized sound).
    * Visual dice animations and dynamic DOM manipulation.

### 2. Python Prototype (`/python-version`)
* **Tech Stack:** Python 3.x.
* **Highlights:**
    * Command Line Interface (CLI).
    * Implements `try-except` blocks for robust input validation.
    * Statistical analysis of dice rolls (Min/Max/Avg).

### 3. Java Implementation (`/java-version`)
* **Tech Stack:** Java.
* **Highlights:**
    * **OOP Principles:** Utilizes Inheritance and Polymorphism (`PlayerRoll` extends `Rolling`).
    * **Recursion:** Uses recursive algorithms to calculate game statistics.
    * **Encapsulation:** Separates game logic, entities, and runner classes.

## 🚀 How to Run

**Python Version:**
```bash
cd python-version
python dice_duel.py
```

**Java Version:**
```bash
javac GameRunner.java
java GameRunner
```
Author: Ayan Bin Saif
