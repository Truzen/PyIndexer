#!usr/bin/env Python3

import PyPDF2
import re
import tkinter as tk
from tkinter import filedialog
import sys
import pyautogui as pag

def extractor():

    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Use the file dialog to select the PDF file
    file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

    # Check if a file was selected
    if not file_path:
        print("No file selected. Exiting...")
    else:
        # Open the selected PDF file
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Create a regular expression pattern for a 3 letter 3 digit combination
        pattern = re.compile(r"\w{3}\d{3}")

        # Create or open the match.txt file for writing
        with open('match.txt', 'w') as match_file:
            # Iterate through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()

                # Find all matches of the pattern on the page
                check = pattern.search(page_text)
                matches = check.group()

                # Write the matches for the current page to the match.txt file
                if matches:
                    match_file.write(matches + "\n")

        # Close the PDF file
        pdf_file.close()

    print("Matches have been written to 'match.txt'")

def indexer():
    try:
        pag.PAUSE = 1
        pag.moveTo(64, 186)
        pag.moveTo(1645, 236)
        pag.moveTo(1654, 317)
        pag.moveTo(1649, 514)
        pag.moveTo(1841, 831)
    except Exception as oops:
        print(oops)

def prompting():
    # Displays the actual menu system to the user
    print("What would you like to do?\n"
          + "1. Extract IDs from letters (pdf)\n"
          + "2. Use match.txt to index letters in AppXtender \n"
          + "3. Exit")

    # takes the users input from the menu system
    choice = input()


    # depending on the users' choice, run the specific function
    # runs the ID extractor function and redisplays the menu
    if choice == "1":
        extractor()
        prompting()

    if choice =="2":
        indexer()
        prompting()

     # exits the program
    if choice == "3":
        sys.exit()

    # if the users inputs anything besides 1-5, show an error message and have them try again
    else:
        end = input("I'm sorry, that is an invalid entry. Try again? (y/N)")

        # if they choose to try again by typing either Y/y/yes/Yes, redisplay the menu
        if end and end[0].lower() == 'y':
            prompting()

        # if they either purposfully or accidently end something else, terminate the program
        else:
            print("Good-bye")
            sys.exit()

prompting()

