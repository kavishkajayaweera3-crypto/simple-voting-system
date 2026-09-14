num_candidates = int(input("Enter the number of candidates: "))
candidates = []
votes = [0] * num_candidates  # Initialize votes for each candidate to 0

for i in range(num_candidates):
    name = input('Enter the name of candidate: ')
    candidates.append(name)

for i in range(num_candidates): #len means number
    print(f"{i+1} - {candidates[i]}")

while True:
    user_input = input("Enter your vote (or type 'stop' to finish): ")
    if user_input.lower() == 'stop':
        break
    if user_input.isdigit():
        vote = int(user_input)
        if 1 <= vote <= num_candidates:
            votes[vote -1] += 1
            print( "vote recorded.")
        else:
            print("Invalid vote! Please try again.")
    else:
        print("Invalid input! Please enter a number or 'stop' to finish.")
print ("Election Results:")

index = 0
while index < num_candidates:
    print(f"{candidates[index]} received {votes[index]} votes.")
    index += 1

if votes[0] > votes[1] and votes[0] > votes[2]:
    print(f"1st place: {candidates[0]} with {votes[0]} votes.")
elif votes[0] < votes[1] and votes[0] < votes[2]:
    print(f"3rd place: {candidates[0]} with {votes[0]} votes.")
else:
    print(f"2nd place: {candidates[0]} with {votes[0]} votes.")

if votes[1] > votes[0] and votes[1] > votes[2]:
    print(f"1st place: {candidates[1]} with {votes[1]} votes.")
elif votes[1] < votes[0] and votes[1] < votes[2]:
    print(f"3rd place: {candidates[1]} with {votes[1]} votes.")
else:
    print(f"2nd place: {candidates[1]} with {votes[1]} votes.")

if votes[2] > votes[0] and votes[2] > votes[1]:
    print(f"1st place: {candidates[2]} with {votes[2]} votes.")
elif votes[2] < votes[0] and votes[2] < votes[1]:
    print(f"3rd place: {candidates[2]} with {votes[2]} votes.")
else:
    print(f"2nd place: {candidates[2]} with {votes[2]} votes.")



