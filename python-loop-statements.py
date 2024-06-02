import random
#1.  The Range Riddle
# The Range Riddle
#2. Double Scoop with Nested Loops
#Task 1: Your Mood Tracker

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_day = ["morning", "afternoon", "evening"]

for day in days_of_week:
    
    for time in times_day:
        mood = random.choice(moods)
        print("On", day,time,"you were",mood,".")
    print()

#3. Loop Condition Logic
#Task 1: Loop Condition Exploration
#Task 2: Conditional Exit

count = 0
loop = True
max_number = 5
while (count < max_number):
    print("This is iteration number:", count + 1)
    count += 1
    
    #if count >= 5:
        #loop = False
        #break
    #break

#4. Python's Random Game Night
#Task 1: Random Choice Game

# List of items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

# Randomly select an item from the list
selected_item = random.choice(items)

# Prompt the player to guess the item
print("Guess the selected item from the following list:")
print(", ".join(items))

# Get the player's guess
guess = input("Enter your guess: ")

# Provide feedback on whether the guess was correct
if guess == selected_item:
    print("Congratulations! You guessed correctly.")
else:
    print(f"Sorry, that's incorrect. The correct answer was {selected_item}.")

#5. Looping Lists - The Rythem of Repetition
#Task 1: The for Loop DJ Set
# List of genres
genres = ["Rock", "Jazz", "Hip Hop", "Classical", "Electronic", "Reggae", "Country"]

# Loop through the genres with a counter
for i, genre in enumerate(genres, start=1):
    # Print the track number and genre with a custom message
    print(f"Track {i}: Get ready for some {genre} music!")

#Task 2: The Remix Artist with while
i = 0
while i < len(genres):
    
    print("Get ready for some ", genres[i]," music!")
    i += 1
    if genres[i] == "Country":
        print("Country music present. Stop the party. Wheres my cowboy hat at?")
        break

#Task 3: Light Show Technician Loop
for index in range(len(genres)):
    genre = genres[index]
    
    # Skip the genre if it's not suitable for the light show
    if genre == 'Classical':
        continue
    
    # Print the track number and a message that the light show is ready
    track_number = index + 1
    print(f"Track {track_number}: Light show ready for {genre}!")

#6. Advanced Looping Techniques
#Task 1: The Selective DJ
sublist = genres[1:4]
for genre in sublist:
    print(genre)

#Task 2: The One-Liner Band with List Comprehensions
genres_with_music = [genre + ' Music' for genre in genres]

# Print the new list
print(genres_with_music)

#Task 3:
for i in range(10, 0, -1):
    print(i)

# Print the final message
print("The beat drops now!")


