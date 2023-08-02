from pyscript import Element  # type: ignore
import asyncio


class NoughtsAndCrosses:
    def __init__(self):
        self.turn = 1

    async def reveal_board(self):
        await asyncio.sleep(1)
        Element("overlay").element.style.display = "none"
        Element("board").element.style.display = "flex"

        await asyncio.sleep(0.1)
        Element("board").element.style.opacity = 1

    def start_game(self):
        Element("overlay").element.style.opacity = 0
        asyncio.ensure_future(self.reveal_board())

    def make_move(self, id):
        cell = Element(id)

        if self.turn % 2 == 1:
            cell.element.innerText = "o"

        else:
            cell.element.innerText = "x"

        self.turn += 1


game = NoughtsAndCrosses()
