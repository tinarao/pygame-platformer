class Block():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size


def get_blocks():
    WIDTH = 1000
    HEIGHT = 800
    block_size = 96
    
    blocks = []
    for i in range(0, (WIDTH // block_size) * 100, block_size):
        blocks.append(
            Block(i, HEIGHT - block_size, block_size)
        )
        
    print(blocks)
    
    
get_blocks()