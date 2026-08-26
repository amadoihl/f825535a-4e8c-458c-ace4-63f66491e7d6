# Build and work with a dictionary that maps item IDs to item descriptions. 
# You’ll practice creating a dict, indexing, adding and removing keys, 
# checking for key existence, iterating with keys(), values(), items(), and 
# finishing with a small dictionary comprehension.

# 1)  Build the dictionary
#     Create a dict named lost_and_found where the key is the ID (e.g., "A101") and the value is the description (e.g., "Water bottle").
#     If the same ID appears twice, the last one wins. That’s normal dict behavior.

# 2)  Look up a value safely
#     Print the description for ID "B202".
#     If it doesn’t exist, print "Not found" without raising an error.

# 3)  Add and remove keys
#     Add a new item: ID "E505" -> "Gloves".
#     Remove ID "C303" if it exists. Do it safely (no KeyError).

# 4)  Check existence
#     If "Z999" is not in the dictionary, print "Z999 not present".

# 5)  Iterate through the dictionary
#     Using keys(): print all IDs on one line, space-separated.
#     Using values(): print all descriptions on one line, space-separated.
#     Using items(): print each pair as ID: description on its own line.

# 6)  Dictionary comprehension
#     Build a new dict called counts that maps each description to how many times it appears in lost_and_found.
#     Print counts.
#     Hint: iterate over lost_and_found.values(). A simple approach is to 
#     iterate over the unique descriptions and count how often each appears.

# ---------------------------------
# ---- Start you program here -----

# Use this list to initialize your dictionary:
initial_items = [
    ("A101", "Water bottle"),
    ("B202", "Wallet"),
    ("C303", "Scarf"),
    ("D404", "Water bottle"),
]


# 1) Build the dict from initial_items
lost_and_found = {}  # TODO: fill from initial_items

# 2) Lookup "B202"
# TODO: print description or "Not found" without raising an error

# 3) Add & remove
# TODO: add E505 -> "Gloves"
# TODO: remove C303 if present (no KeyError)

# 4) Existence check
# TODO: if "Z999" not in dict, print "Z999 not present"

# 5) Iterate with keys(), values(), items()
# TODO: print IDs (keys) space-separated
# TODO: print descriptions (values) space-separated
# TODO: print each "ID: description" using items()

# 6) Dictionary comprehension for counts
# Build counts: {description: frequency}
# Hint: iterate over lost_and_found.values()
counts = {}  # TODO: use a dict comprehension here
print(counts)
