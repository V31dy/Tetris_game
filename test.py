import pytest

from tetris import *


def test_color():
    '''Тест проверки цвета'''
    assert BLACK != WHITE

def test_moving_block():
    '''Тест проверки движения блока'''
    block = MovingBlock()
    block.nextPos.col = 1
    block.nextPos.row = 1
    assert block.nextPos.row == 1 and block.nextPos.col == 1




if __name__ == '__main__':
    pytest.main()
