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

def test_GameClock():
    '''Тест проверки работы времени'''
    clock = GameClock()
    clock.update()
    assert clock.frameTick == 1

def test_MainBoard():
    '''Тест проверки счета'''
    board = MainBoard(blockSize, boardPosX, boardPosY, boardColNum, boardRowNum, boardLineWidth, blockLineWidth, scoreBoardWidth)
    board.updateScores()
    assert board.score == 0

def test_MovingPiece():
    key = GameKeyInput()
    piece = MovingPiece(boardColNum, boardRowNum, 'uncreated')
    board = MainBoard(blockSize, boardPosX, boardPosY, boardColNum, boardRowNum, boardLineWidth, blockLineWidth, scoreBoardWidth)
    key.down.status = 'pressed'
    key.xNav.status = 'right'
    piece.movCollisionCheck('down')
    piece.move(board.blockMat)
    assert piece.status == 'moving'

if __name__ == '__main__':
    pytest.main()