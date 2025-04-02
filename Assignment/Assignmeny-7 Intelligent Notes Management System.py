import os

# Create a folder to store notes
myfile = "26-03-2025/all files"         #creating a file path
if not os.path.exists(myfile):
    os.makedirs(myfile)

# positive,negative,neutral words for sentiment analysis
positive_words = {"enjoy", "happy", "excellent", "amazing", "great", "positive", "success", "good"}
negative_words = {"bad", "sad", "terrible", "awful", "hate", "negative", "fail", "poor"}
neutral_words = {"okay", "fine", "average", "normal", "usual", "simple", "neutral", "fair"}
# Function to check sentiment of a given text
def check_sentiment(content):
    content = content.lower()
    pos_count = sum(content.count(word) for word in positive_words)
    neg_count = sum(content.count(word) for word in negative_words)
    neu_count = sum(content.count(word) for word in neutral_words)

    if pos_count > neg_count:
        return "Positive Sentiment"
    elif neg_count > pos_count:
        return "Negative Sentiment"
    elif neu_count > pos_count:
        return "Neutral Sentiment"
    else:
        return "No Sentiments"

# Function to list all saved file
def allfiles():
    files = os.listdir(myfile)
    if files:
        print("Available Notes:")
        for note in files:
            print(note)
    else:
        print("No notes found.")

# Function to read a file and check sentiment
def readingfile():
    allfiles()
    filename = input("Enter the note name (or type 'all' to read everything): ")
    
    if filename.lower() == 'all':
        for note in os.listdir(myfile):
            with open(os.path.join(myfile, note), 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"\n--- {note} ---")
                print(content)
                print("Sentiment:", check_sentiment(content))
    else:
        file_path = os.path.join(myfile, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print("\nContent:")
                print(content)
                print("Sentiment:", check_sentiment(content))
        else:
            print("Note not found.")

# Function to create a new file
def creatingfile():
    filename = input("Enter a name for your file (myfilename .txt): ")
    content = input("Enter your note content: ")
    with open(os.path.join(myfile, filename), 'w', encoding='utf-8') as file:
        file.write(content)
    print("####file saved successfully.####")

# Function to edit an saved txt file
def editingfile():
    allfiles()
    filename = input("Enter the filename to edit: ")
    file_path = os.path.join(myfile, filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'r+', encoding='utf-8') as file:
            print("Current content:")
            print(file.read())
            file.seek(0)
            new_content = input("Enter new content: ")
            file.write(new_content)
            file.truncate()
        print("file updated successfully.")
    else:
        print("file not found.")

# Main function to show all options
def main():
    while True:
        print("\n===== Intelligent Notes Management System =====")
        print("1. Read & Analyze Notes")
        print("2. Create a file")
        print("3. Edit a file")
        print("4. Exit")
        choice = input("Choose any one option(1/2/3/4): ")
        
        if choice == '1':
            readingfile()
        elif choice == '2':
            creatingfile()
        elif choice == '3':
            editingfile()
        elif choice == '4':
            print("Goodbye! Thanks for using the Notes Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1/2/3/4.")

# function calling or running the programe
main()
