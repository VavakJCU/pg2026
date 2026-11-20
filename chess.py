from abc import ABC, abstractmethod
#import z knihovny abc funkci ABC (umožňuje vytvořit abstraktní třídu) a abstractmethod (umožňuje označit metodu jako abstraktní)
#ABC = Abstract Base Class


class Piece(ABC): #obecná figura
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.

        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        #dvě podtržítka znamenají, že atribut je určen jako interní (tj pouze pro používaní uvnitř třídy)
        self.__color = color
        self.__position = position

    @abstractmethod #zajistí/vynutí aby tato metoda byla implementována ve všech třídách vycházejících z této třídy
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.

        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod #metoda, která je stejná pro všechny objekty dané třídy
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property #umožňuje používat metodu jako běžný atribut
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter #slouží ke změně atributu objektu
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self): #definuje, co má vypsat příkaz print() pro náš objekt
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece): #pěšák
    def possible_moves(self):
        """
        Vrací možné tahy pěšáka (pouze pohyb o jedno pole vpřed, bez braní).
        Bílý pěšák jde nahoru (řádek se zvyšuje), černý dolů (řádek se snižuje).

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position

        if self.color == "white":
            move = (row + 1, col)
        else:
            move = (row - 1, col)

        final_moves = []
        if self.is_position_on_board(move):
            final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece): #jezdec
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece): #střelec
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce (diagonálně všemi čtyřmi směry).

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        # směry jako (změna řádku, změna sloupce)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
            while self.is_position_on_board((new_row, new_col)):
                final_moves.append((new_row, new_col))
                new_row += d_row
                new_col += d_col
        return final_moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece): #věž
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže (vodorovně a svisle).

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
            while self.is_position_on_board((new_row, new_col)):
                final_moves.append((new_row, new_col))
                new_row += d_row
                new_col += d_col
        return final_moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece): #dáma
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy (jako věž + střelec).

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),    # jako věž
            (1, 1), (1, -1), (-1, 1), (-1, -1)   # jako střelec
        ]
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
            while self.is_position_on_board((new_row, new_col)):
                final_moves.append((new_row, new_col))
                new_row += d_row
                new_col += d_col
        return final_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece): #král
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále (o jedno pole libovolným směrem).

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    figurka =  Rook("white", (1, 1))
        #Pawn("white", (2, 1))
        #Pawn("black", (7, 1))
        #Knight("black", (1, 2))
        #Bishop("white", (1, 3))
        #Queen("white", (1, 4))
        #King("white", (1, 5))

    print(figurka)
    print("Možné kroky:", figurka.possible_moves())