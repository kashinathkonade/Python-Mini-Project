# Simple Voting System

# Input candidate names
candidate1 = input("Enter the first candidate's name: ")
candidate2 = input("Enter the second candidate's name: ")

# Initialize vote counters for both candidates
cand1_votes = 0
cand2_votes = 0

# List of eligible voter IDs
voters_id = [1, 2, 3, 4, 5, 6]
no_of_voters = len(voters_id)
print("Number of voters: ", no_of_voters)

# List to keep track of voters who have already voted
voted = []

# Voting loop
while True:
    # Check if all voters have voted
    if voters_id == []:
        print("Voting is over.")
        
        # Determine the winner or if there is a tie
        if cand1_votes > cand2_votes:
            print(f"{candidate1} won the election with {cand1_votes} votes!")
        elif cand2_votes > cand1_votes:
            print(f"{candidate2} won the election with {cand2_votes} votes!")
        else:
            print("The election is tied!")
        break  # End the voting process

    else:
        # Ask for the voter's ID
        voter = int(input("Enter your voter ID: "))
        
        # Check if the voter has already voted
        if voter in voted:
            print("You have already voted!")
        else:
            # Check if the voter ID is valid
            if voter in voters_id:
                # Show the candidates and prompt for choice
                print(f"1. {candidate1}\n2. {candidate2}")
                choice = int(input("Enter your choice (1 or 2): "))
                
                # Record the vote based on the user's choice
                if choice == 1:
                    cand1_votes += 1
                    print(f"You voted for {candidate1}!")
                elif choice == 2:
                    cand2_votes += 1
                    print(f"You voted for {candidate2}!")
                else:
                    print("Invalid choice! Vote not counted.")
                    continue  
                
                # Mark the voter as having voted and remove them from eligible voters
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("Invalid voter ID. You are not allowed to vote!")
