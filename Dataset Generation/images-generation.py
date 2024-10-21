import os
import csv
from PIL import ImageGrab
import pyautogui
import win32com.client
import win32gui
import time

def get_word_window_handle():
    def enum_windows_callback(hwnd, handles):
        if win32gui.IsWindowVisible(hwnd) and 'Word' in win32gui.GetWindowText(hwnd):
            handles.append(hwnd)
    handles = []
    win32gui.EnumWindows(enum_windows_callback, handles)
    return handles[0] if handles else None

def write_word_in_doc(word, doc):
    doc.Content.Text = ""
    p = doc.Content.Paragraphs.Add()
    p.Range.Text = word
    
    # Apply font settings
    p.Range.Font.SizeBi = 140  # Set the font size to 150
    p.Range.Font.NameBi = "AmarNastaleeq "  
    p.Range.Font.Name = "AmarNastaleeq"
    p.Range.ParagraphFormat.Alignment = 1  # Center align the paragraph (1 corresponds to center alignment)

    doc.ActiveWindow.View.Zoom.Percentage = 100
    # Set line spacing to 1.15
    # p.Range.ParagraphFormat.LineSpacingRule = 5  # wdLineSpaceExactly
    # p.Range.ParagraphFormat.LineSpacing = 15
    p.Range.ParagraphFormat.SpaceBefore = 45
    doc.SpellingChecked = False
    doc.GrammarChecked = False
    doc.ShowSpellingErrors = False
    # doc.ShowGrammarErrors = False
    p.Range.InsertParagraphAfter()

    # Add 4 empty paragraphs before moving the cursor out of view
    for _ in range(4):
        empty_paragraph = doc.Content.Paragraphs.Add()
        empty_paragraph.Range.InsertParagraphAfter()

    # Force refresh
    doc.Application.ScreenRefresh()
   
    # Wait for Word to apply changes
    pyautogui.sleep(2)  # Adjust the sleep time as needed
    # doc.Application.Selection.EndKey(Unit=6)  # wdStory
    # # This scrolls the document window so that the cursor (end of document) is visible
    # doc.ActiveWindow.ScrollIntoView(doc.Application.Selection.Range)
    
    # # Adjust the scroll position by moving it a bit up
    # doc.ActiveWindow.SmallScroll(Down=-90) 
    doc.ActiveWindow.VerticalPercentScrolled = 3

def move_cursor_out_of_view(doc):
    end_of_doc = doc.Content.End
    doc.Application.Selection.Start = end_of_doc
    doc.Application.Selection.End = end_of_doc
    doc.Application.ScreenRefresh()

def take_screenshot(output_folder, label):
    # Wait for the document to update
    pyautogui.sleep(2)
    # Nice one
    # x1, y1 = 600, 299
    # x2, y2 = 1299, 999
    #Nice one 2
    # x1, y1 = 490, 289
    # x2, y2 = 1410, 959
    # Define the region to capture (adjust as needed)
    x1, y1 = 347, 298
    x2, y2 = 1551, 993
    # x1, y1 = 599, 299
    # x2, y2 = 1299, 799
    bbox = (x1, y1, x2, y2)

    # Take a screenshot
    screenshot = ImageGrab.grab(bbox)

    # Save the screenshot
    screenshot.save(os.path.join(output_folder, f"{label}.png"))

# Main script
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

csv_file = 'Allwords_labels21FF.csv'

# Start Word application
word_app = win32com.client.Dispatch("Word.Application")
word_app.Visible = True

# Create a new Word document
doc = word_app.Documents.Add()

# Give Word some time to start up and display the window
time.sleep(2)

# Bring the Word window to the foreground
hwnd = get_word_window_handle()
if hwnd:
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)  # Give some time for the window to come to the foreground

with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)  # Read all rows into a list

    # Extract count from the first row
    count = int(rows[0][1])
    # Process each row starting from the count index
    end = int(rows[1][1])
    temp = 0
    for row in rows[count:end]:
        label = row[0]
        word = row[1]

        # Write the word into the Word document
        write_word_in_doc(word, doc)

        # Move the cursor out of the visible area
        move_cursor_out_of_view(doc)

        # Bring the Word window to the foreground before taking the screenshot
        hwnd = get_word_window_handle()
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(1)  # Give some time for the window to come to the foreground

        # Take a screenshot and save it
        take_screenshot(output_folder, label)

        # Increment the count
        count += 1

        # Update the count in the CSV file after each word is processed
        rows[0][1] = str(count)
        with open(csv_file, mode='w', newline='', encoding='utf-8') as write_file:
            csv_writer = csv.writer(write_file)
            csv_writer.writerows(rows)
        # if temp==20:
        #     count+=10000
        #     temp=0

# Close the Word application
word_app.Quit()

print("Dataset generation complete.")
