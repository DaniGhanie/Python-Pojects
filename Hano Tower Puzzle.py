# Group 12
# Dani Ghanie U83713490
# Aaron Acevedo U89664173

# - n: The number of disks to be moved.
# - A: The source peg.
# - B: The auxiliary peg.
# - C: The destination peg.
def TowerOfHanoi(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
        return 1
    else:
# 1. Move n-1 disks from peg A to peg B using peg C as the auxiliary peg.
        count1 = TowerOfHanoi(n - 1, A, C, B)
# 2. Print the move for the nth disk from peg A to peg C.
        print(f"Move disk {n} from {A} to {C}")
# 3. Move the n-1 disks from peg B to peg C using peg A as the auxiliary peg.
        count2 = TowerOfHanoi(n - 1, B, A, C)
        return count1 + 1 + count2

def main():
    print("Input length of the tower")
    n = int(input())
    total = TowerOfHanoi(n, 'A', 'B', 'C')
    print(f"count = {total}")

main()
