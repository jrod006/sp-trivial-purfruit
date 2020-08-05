# sp-trivial-purfruit
Slowpokes Trivial Purfruit Development

### 1. Requirements for User Interfaces

The libraries needed to run user interfaces include:
- PIL
- tkinter
- pandas

### 2. Running UI scripts

- Run "python tp_application.py"
  - This application will begin program and instantiate a Main Menu window.
- On the Main Menu window, users will have access to one of the three options below:
  - Start New Game
  - Access Database
  - Exit Trivial Purfruit (this button will shut down Main Menu and exit application)
- Start New Game Button
  - A new window titled TP Game Settings will pop up, this will allow users to enter settings for a new game.
  - Enter names of the players to join the game
  - Select a time limit for answering questions (for demo purposes only)
  - Select game difficulty for questions (for demo purposes only)
  - With the buttons at the bottom of the window, the user can either view rules of the game or begin new game
- Access Database Button
  - A new window titled Database Authentication will pop up, an authorized user must enter their username and password
  - For demo purposes, username = username, password = test123. Click Authenticate to confirm credentials
  - If the credentials are verified, a new window will pop up allowing Database acccess and modification
  - A button in the Database Authentication window also allows for exit and return to the Main Menu
- Trivial Purfruit Question Database
  1. Add Question
    - To add a question, the user should enter the question category, the new question, and answer associated with the question
    - Once all information is entered, clicking "Add Question" will add the question to the database
  2. Retrieve/Update Question
    - To retrieve a question to modify, the user can select any question with their cursor
    - Once a question is selected and highlighted, clicking the "Retrieve Question to Modify" button will retrieve question information in the below text fields for modification
  3. Delete Question
    - To delete a question in the database, a user can select and highlight the question to be deleted with the cursor
    - Once selected, clicking "Remove Question" will delete the question from the database
  4. Swap Color Category
    - To swap color categories in the database, in the first entry with the label, "Category of Color to be Replaced," the user should enter the color they wish to replace
    - In the entry with the label "New Color for Category" the user should enter the new desired color
    - Once the entries are filled with the desired selections, clicking "Swap Color Category" will swap the colors in the database
  5. Save and Close Database
    - This selection will save the current database and close the Database window
- Trivial Purfruit Game Window
  - When Begin New button is selected from the TP Game Settings window, with the selected settings a Trivial Purfruit Game window should open
  - This window is purely for demonstration purposes and does not currently have any functionality
  - Clicking the "Game Simulation" button at the bottom of the window will proceed to a text based game simulation in the terminal
  - After game simulation is complete (terminal will print SIMULATION COMPLETE), return to Trivial Purfruit Gameboard to re-run simulation or exit game board
