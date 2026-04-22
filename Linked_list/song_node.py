class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
        
# song1 = SongNode("Uptown Funk")
# song2 = SongNode("Party Rock Anthem")
# song1.next = song2
# song3 = SongNode("Bad Romance")
# song2.next = song3

# top_hits_2010s = song1

top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

print_linked_list(top_hits_2010s)