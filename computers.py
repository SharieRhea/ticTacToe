import random
from moves import Moves


def get_random_move(board):
    """Randomly generates moves until one is possible (no move already there)."""
    number = random.randint(0, 8)
    while board.get_tiles()[number].get_move() is not Moves.NONE:
        number = random.randint(0, 8)
    return number


class RandomComputer:
    """Models a computer players that picks random moves."""

    def get_computer_move(self, board):
        """Calls get_random_move to maintain interface."""
        return get_random_move(board)


class HumanComputer:
    """Models a 'human-like' computer player."""

    def get_computer_move(self, board):
        """Returns a move to win, block the other player, or randomly, in that order."""
        possibility_count = 0
        block_move = None
        for possibility in self.get_possibilities(board.get_tiles()):
            # create set of unique moves in line
            moves = set()
            for move in possibility:
                moves.add(move)

            # check for opportunity
            if len(moves) == 2 and possibility.count(Moves.NONE) == 1:
                move_index = possibility.index(Moves.NONE)
                # find exact tile number
                if Moves.COMPUTER in moves:
                    return self.get_tile_index(possibility_count, move_index)
                elif Moves.PLAYER in moves:
                    block_move = self.get_tile_index(possibility_count, move_index)

            possibility_count += 1

        if block_move is not None:
            return block_move
        return get_random_move(board)

    def get_possibilities(self, tiles):
        """Returns the 8 possible lines to win a tic-tac-toe game"""
        return [
            [tiles[0].get_move(), tiles[1].get_move(), tiles[2].get_move()],
            [tiles[3].get_move(), tiles[4].get_move(), tiles[5].get_move()],
            [tiles[6].get_move(), tiles[7].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[3].get_move(), tiles[6].get_move()],
            [tiles[1].get_move(), tiles[4].get_move(), tiles[7].get_move()],
            [tiles[2].get_move(), tiles[5].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[4].get_move(), tiles[8].get_move()],
            [tiles[2].get_move(), tiles[4].get_move(), tiles[6].get_move()]]

    def get_tile_index(self, line, index):
        """Returns the index of tile (0-8) based on its line and position."""
        # horizontal lines
        if line < 3:
            return line * 3 + index
        # vertical lines
        elif line < 6:
            return index * 3 + line % 3
        # diagonal lines
        elif line == 6:
            if index == 0:
                return 0
            elif index == 1:
                return 4
            else:
                return 8
        else:
            if index == 0:
                return 2
            elif index == 1:
                return 4
            else:
                return 6


class Tree:
    """Models a tree to determine possible outcomes for a tic-tac-toe game."""

    class Node:
        """Models a node of tree."""

        def __init__(self, board):
            """Initializes a node."""
            self.children = []
            self.board = board.copy()
            self.utility = 0

    def __init__(self, board):
        """Initializes a tree."""
        self.root = self.Node(board.copy())
        self.build_tree(self.root, 0)

    def build_tree(self, node, depth):
        """Recursively builds a tree with every possible game outcome based on first move."""
        # Check base case, set utilities
        if node.board.check_win() is Moves.PLAYER:
            node.utility = (-1 * (9 - depth))
        elif node.board.check_win() is Moves.COMPUTER:
            node.utility = (1 * (9 - depth))
        elif node.board.is_board_full():
            node.utility = 0
        else:
            # Find empty_tiles/possible next moves
            empty_tiles = []
            for tile in node.board.get_tiles():
                if tile.get_move() is Moves.NONE:
                    empty_tiles.append(tile)

            while len(node.children) != len(empty_tiles):
                child = Tree.Node(node.board.copy())

                empty_child_tiles = []
                for tile in child.board.get_tiles():
                    if tile.get_move() is Moves.NONE:
                        empty_child_tiles.append(tile)

                if not node.board.player_turn:
                    empty_child_tiles[len(node.children)].add_computer_move()
                    child.board.player_turn = True
                else:
                    empty_child_tiles[len(node.children)].add_player_move()
                    child.board.player_turn = False

                node.children.append(child)
                self.build_tree(child, depth + 1)

    def determine_utility(self, node):
        """Determines the overall utility of a given tree, starting at the node given."""
        utility = 0
        if len(node.children) == 0:
            return node.utility
        else:
            for child in node.children:
                utility += self.determine_utility(child)

        return utility


def is_same_state(state1, state2):
    """Returns True if the two states are the same, False otherwise."""
    index = 0
    for tile in state1.board.get_tiles():
        if tile.get_move() != state2.get_tiles()[index].get_move():
            return False
        index += 1

    return True


class InsaneComputer:
    """Models an unbeatable computer that uses a tree to determine moves."""

    def __init__(self):
        """Initializes a computer for the game."""
        self.tree = None
        self.state = None

    def get_computer_move(self, board):
        """Updates state based on most recent player move, determines and returns best move, and updates state again."""
        # Build tree if there isn't one.
        if self.tree is None:
            self.tree = Tree(board)
            self.state = self.tree.root
        else:
            # Update state to reflect last player move.
            for child in self.state.children:
                if is_same_state(child, board):
                    self.state = child

        # Determine index of the best computer move.
        utilities = []
        for child in self.state.children:
            utilities.append(self.tree.determine_utility(child))
        utility_index = utilities.index(max(utilities))

        print(utilities)

        # Update state to reflect computer move.
        i = 0
        for child in self.state.children:
            if i == utility_index:
                self.state = child
            i += 1

        # Determine move index relative to whole board.
        empties = -1
        index = -1
        for tile in board.get_tiles():
            if tile.get_move() is Moves.NONE:
                empties += 1
            index += 1

            if utility_index == empties:
                return index


class SecretComputer:
    """Models a 'human-like' computer player, but the player gets to move twice everytime."""

    def __init__(self):
        self.counter = 0

    def get_computer_move(self, board):
        """Returns a move to win, block the other player, or randomly, in that order."""
        if self.counter < 1:
            self.counter += 1
            return None

        self.counter = 0
        possibility_count = 0
        block_move = None
        for possibility in self.get_possibilities(board.get_tiles()):
            # create set of unique moves in line
            moves = set()
            for move in possibility:
                moves.add(move)

            # check for opportunity
            if len(moves) == 2 and possibility.count(Moves.NONE) == 1:
                move_index = possibility.index(Moves.NONE)
                # find exact tile number
                if Moves.COMPUTER in moves:
                    return self.get_tile_index(possibility_count, move_index)
                elif Moves.PLAYER in moves:
                    block_move = self.get_tile_index(possibility_count, move_index)

            possibility_count += 1

        if block_move is not None:
            return block_move
        return get_random_move(board)

    def get_possibilities(self, tiles):
        """Returns the 8 possible lines to win a tic-tac-toe game"""
        return [
            [tiles[0].get_move(), tiles[1].get_move(), tiles[2].get_move()],
            [tiles[3].get_move(), tiles[4].get_move(), tiles[5].get_move()],
            [tiles[6].get_move(), tiles[7].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[3].get_move(), tiles[6].get_move()],
            [tiles[1].get_move(), tiles[4].get_move(), tiles[7].get_move()],
            [tiles[2].get_move(), tiles[5].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[4].get_move(), tiles[8].get_move()],
            [tiles[2].get_move(), tiles[4].get_move(), tiles[6].get_move()]]

    def get_tile_index(self, line, index):
        """Returns the index of tile (0-8) based on its line and position."""
        # horizontal lines
        if line < 3:
            return line * 3 + index
        # vertical lines
        elif line < 6:
            return index * 3 + line % 3
        # diagonal lines
        elif line == 6:
            if index == 0:
                return 0
            elif index == 1:
                return 4
            else:
                return 8
        else:
            if index == 0:
                return 2
            elif index == 1:
                return 4
            else:
                return 6
