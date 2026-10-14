
# Social Network using Adjacency Matrix

users = ["Amit", "Rahul", "Sneha", "Priya"]

# 0 means no friendship, 1 means friendship
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

print("Users:", users)
print("\nFriendship Adjacency Matrix:")

print("     ", end="")
for user in users:
    print(user, end="  ")
print()

for i in range(len(users)):
    print(users[i], end="  ")
    for j in range(len(users)):
        print(" ", matrix[i][j], end=" ")
    print()

print("\nFriendship Connections:")
for i in range(len(users)):
    for j in range(i + 1, len(users)):
        if matrix[i][j] == 1:
            print(users[i], "-", users[j])
