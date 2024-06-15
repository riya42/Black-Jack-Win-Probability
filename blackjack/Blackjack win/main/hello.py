# Input
n = int(input())
marbles = list(map(int, input().split()))

# Create a dictionary to store the count of each marble value
marble_count = {}
for marble in marbles:
    marble_count[marble] = marble_count.get(marble, 0) + 1

# Sort the unique marble values in non-decreasing order
unique_marbles = sorted(list(set(marbles)))

# Count the number of neighboring pairs where a[i+1] > a[i]
happy_count = 0
for i in range(len(unique_marbles) - 1):
    current_marble = unique_marbles[i]
    next_marble = unique_marbles[i + 1]

    # Check the count of current and next marble values
    happy_count += min(marble_count[current_marble], marble_count[next_marble])

# Output the result
print(happy_count)
