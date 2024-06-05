#!/bin/bash

# Function to print "You lost" and exit
you_lost() {
    echo "You lost"
    exit 1
}

# Entrance hall
entrance_hall() {
    echo "You are in the entrance hall. It's dark and musty. There are doors to the left, right, and straight ahead."
    echo "Do you want to go 'left', 'right', or 'straight'?"
    read choice
    case $choice in
        left) library ;;
        right) kitchen ;;
        straight) staircase ;;
        *) you_lost ;;
    esac
}

# Library
library() {
    echo "You enter a dusty library filled with old books. There's a flickering candle on the table."
    echo "Do you want to 'examine books', 'take candle', or 'go back'?"
    read choice
    case $choice in
        "examine books")
            echo "You find an old book about the history of the house. It's very interesting."
            library ;;
        "take candle")
            echo "You take the candle. It might be useful later."
            entrance_hall ;;
        "go back") entrance_hall ;;
        *) you_lost ;;
    esac
}

# Kitchen
kitchen() {
    echo "The kitchen is dirty and smells terrible. There are broken plates everywhere and a strange noise coming from the cupboard."
    echo "Do you want to 'open cupboard', 'search drawers', or 'go back'?"
    read choice
    case $choice in
        "open cupboard")
            echo "A ghost jumps out of the cupboard! You run back to the entrance hall."
            entrance_hall ;;
        "search drawers")
            echo "You find an old, rusty key. It might be useful later."
            entrance_hall ;;
        "go back") entrance_hall ;;
        *) you_lost ;;
    esac
}

# Staircase
staircase() {
    echo "You see a grand staircase leading upstairs. The air feels colder here."
    echo "Do you want to 'go upstairs' or 'go back'?"
    read choice
    case $choice in
        "go upstairs") hallway ;;
        "go back") entrance_hall ;;
        *) you_lost ;;
    esac
}

# Hallway
hallway() {
    echo "The hallway is long and has several doors. At the end, there is a window."
    echo "Do you want to 'enter first door', 'enter second door', 'look out window', or 'go downstairs'?"
    read choice
    case $choice in
        "enter first door") bedroom ;;
        "enter second door") study ;;
        "look out window")
            echo "You see nothing but darkness outside. It's very eerie."
            hallway ;;
        "go downstairs") entrance_hall ;;
        *) you_lost ;;
    esac
}

# Bedroom
bedroom() {
    echo "A dusty old bedroom with a large bed. There's something shiny under the bed."
    echo "Do you want to 'look under bed', 'check closet', or 'go back'?"
    read choice
    case $choice in
        "look under bed")
            echo "You find a hidden treasure chest! Congratulations, you found the treasure and escaped the haunted house!"
            exit 0 ;;
        "check closet")
            echo "A ghost jumps out of the closet! You run back to the hallway."
            hallway ;;
        "go back") hallway ;;
        *) you_lost ;;
    esac
}

# Study
study() {
    echo "A small study room with a desk and a chair. Papers are scattered everywhere."
    echo "Do you want to 'read papers', 'check desk drawer', or 'go back'?"
    read choice
    case $choice in
        "read papers")
            echo "You find notes about the haunted house. They are very spooky."
            study ;;
        "check desk drawer")
            echo "You find a secret map of the house. It might be useful later."
            hallway ;;
        "go back") hallway ;;
        *) you_lost ;;
    esac
}

# Start the game
echo "Welcome to the Haunted House Adventure!"
entrance_hall
