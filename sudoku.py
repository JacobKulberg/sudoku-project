#main file
import pygame
from sudoku_generator import *
import sys
import copy

class Board:
	def __init__(self, width, height, screen):
		self.width = 64 * 9
		self.height = 64 * 10
		self.screen = screen
# Constructor for the Board class.
# screen is a window from PyGame.
# difficulty is a variable to indicate if the user chose easy medium, or hard.

	def draw_board(self,gameboard):
		big_font = pygame.font.Font(None, 80)
		small_font = pygame.font.Font(None, 50)

		one_surf = small_font.render("1", 0, "black")
		two_surf = small_font.render("2", 0, "black")
		three_surf = small_font.render("3", 0, "black")
		four_surf = small_font.render("4", 0, "black")
		five_surf = small_font.render("5", 0, "black")
		six_surf = small_font.render("6", 0, "black")
		seven_surf = small_font.render("7", 0, "black")
		eight_surf = small_font.render("8", 0, "black")
		nine_surf = small_font.render("9", 0, "black")


		for i in range(10):
			pygame.draw.line(self.screen, "black", (0, i * 64), (576, i * 64))
			pygame.draw.line(self.screen, "black", (i * 64, 0), (i * 64, 576))
		for i in range(4):
			pygame.draw.line(self.screen,"black",(0,i*192),(576,i*192),3)
			pygame.draw.line(self.screen, "black", (i*192, 0), (i*192,576), 3)

		for row in range(9):
			for col in range(9):

				if gameboard[row][col] == 1:
					one_rect = one_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(one_surf, one_rect)

				if gameboard[row][col] == 2:
					two_rect = two_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(two_surf, two_rect)

				if gameboard[row][col] == 3:
					three_rect = three_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(three_surf, three_rect)

				if gameboard[row][col] == 4:
					four_rect = four_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(four_surf, four_rect)

				if gameboard[row][col] == 5:
					five_rect = five_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(five_surf, five_rect)

				if gameboard[row][col] == 6:
					six_rect = six_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(six_surf, six_rect)

				if gameboard[row][col] == 7:
					seven_rect = seven_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(seven_surf, seven_rect)

				if gameboard[row][col] == 8:
					eight_rect = eight_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(eight_surf, eight_rect)

				if gameboard[row][col] == 9:
					nine_rect = nine_surf.get_rect(
						center=(col * 64 + 64 / 2, row * 64 + 64 / 2))
					self.screen.blit(nine_surf, nine_rect)

	def draw_sketch(self,sketchboard):
		big_font = pygame.font.Font(None, 80)
		small_font = pygame.font.Font(None, 50)

		one_surf = small_font.render("1", 0, "slategray")
		two_surf = small_font.render("2", 0, "slategray")
		three_surf = small_font.render("3", 0, "slategray")
		four_surf = small_font.render("4", 0, "slategray")
		five_surf = small_font.render("5", 0, "slategray")
		six_surf = small_font.render("6", 0, "slategray")
		seven_surf = small_font.render("7", 0, "slategray")
		eight_surf = small_font.render("8", 0, "slategray")
		nine_surf = small_font.render("9", 0, "slategray")

		for row in range(9):
			for col in range(9):

				if sketchboard[row][col] == 1:
					one_rect = one_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(one_surf, one_rect)

				if sketchboard[row][col] == 2:
					two_rect = two_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(two_surf, two_rect)

				if sketchboard[row][col] == 3:
					three_rect = three_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(three_surf, three_rect)

				if sketchboard[row][col] == 4:
					four_rect = four_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(four_surf, four_rect)

				if sketchboard[row][col] == 5:
					five_rect = five_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(five_surf, five_rect)

				if sketchboard[row][col] == 6:
					six_rect = six_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(six_surf, six_rect)

				if sketchboard[row][col] == 7:
					seven_rect = seven_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(seven_surf, seven_rect)

				if sketchboard[row][col] == 8:
					eight_rect = eight_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(eight_surf, eight_rect)

				if sketchboard[row][col] == 9:
					nine_rect = nine_surf.get_rect(
						topleft=(col * 64 + 5 , row * 64 + 5))
					self.screen.blit(nine_surf, nine_rect)
	# Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	# Draws every cell on this board.
def check_full(board):
	for i in range(9):
		if 0 in board[i]:
			return False
	return True

def main():

	try:
		pygame.init()
		screen = pygame.display.set_mode((576, 640))
		clock = pygame.time.Clock()
		running = True
		screen1 = True
		screen2 = True
		screen3 = True
		difficulty = None
		usery=0
		userx=0
		big_font = pygame.font.Font(None, 80)
		small_font = pygame.font.Font(None, 50)
		smaller_font = pygame.font.Font(None,30)
		board = Board((64 * 9), (64 * 10), screen)
		startbuttons = display_start(screen)

		sketchboard =[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
		pygame.display.flip()

		while running:
			while screen1:
				screen2 = True
				screen3 = True
				for event in pygame.event.get():

					if event.type == pygame.QUIT:
						running = False
						pygame.quit()
						sys.exit()

					elif event.type == pygame.MOUSEBUTTONDOWN:
						x,y = event.pos
						for button_rect, mode in startbuttons:
							if button_rect.collidepoint(x,y):

								difficulty = mode
								print(f"Difficulty selected: {mode}")
								screen.fill("white")
								board = Board((64 * 9), (64 * 10), screen)
								sudoku = SudokuGenerator()
								sudoku.fill_values()
								sudoku.remove_cells(difficulty)
								baseboard = sudoku.baseboard
								playerboard = sudoku.board
								moves = []
								board.draw_board(sudoku.board)
								screen1 = False

			while screen2:
				status = check_full(sudoku.board)
				gamebuttons = game_in_progress(screen)
				if status == True :
					screen2 = False

				for event in pygame.event.get():

					if event.type == pygame.QUIT:
						running = False
						pygame.quit()
						sys.exit()

					elif event.type == pygame.MOUSEBUTTONDOWN:
						x, y = event.pos
						userx = x//64
						usery = y//64
						if usery > 8:
							screen.fill("white")
							board.draw_board(sudoku.board)
							board.draw_sketch(sketchboard)
						else:
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						for button_rect, mode in gamebuttons:
							if button_rect.collidepoint(x,y):
								choice = mode
								if choice == "Reset":
									sketchboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
									for i,j in moves:
										sudoku.board[j][i] = 0
									moves = []
									screen.fill("white")
									board.draw_board(sudoku.board)
									board.draw_sketch(sketchboard)


								elif choice == "Restart":
									screen1 = True
									screen2 = False
									screen3 = False
									difficulty = None
									big_font = pygame.font.Font(None, 80)
									small_font = pygame.font.Font(None, 50)
									smaller_font = pygame.font.Font(None, 30)
									board = Board((64 * 9), (64 * 10), screen)
									startbuttons = display_start(screen)

									sketchboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0],
									               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

								elif choice == "Exit":
									running = False
									pygame.quit()
									sys.exit()



					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_1 and sudoku.board[usery][userx] == 0:
							sketched_value = 1
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx*64, usery*64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_2 and sudoku.board[usery][userx] == 0:
							sketched_value = 2
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_3 and sudoku.board[usery][userx] == 0:
							sketched_value = 3
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_4 and sudoku.board[usery][userx] == 0:
							sketched_value = 4
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_5 and sudoku.board[usery][userx] == 0:
							sketched_value = 5
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_6 and sudoku.board[usery][userx] == 0:
							sketched_value = 6
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_7 and sudoku.board[usery][userx] == 0:
							sketched_value = 7
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_8 and sudoku.board[usery][userx] == 0:
							sketched_value = 8
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_9 and sudoku.board[usery][userx] == 0:
							sketched_value = 9
							sketchboard[usery][userx] = sketched_value
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_RETURN:
							if sketchboard[usery][userx] != 0:
								sudoku.board[usery][userx] = sketchboard[usery][userx]
							moves.append([userx,usery])
							screen.fill("white")
							board.draw_board(sudoku.board)
							sketchboard[usery][userx] = 0
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_UP:
							usery -= 1
							if usery < 0:
								usery = 0
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_DOWN:
							usery += 1
							if usery > 8:
								usery = 8
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_LEFT:
							userx -= 1
							if userx < 0:
								userx=0
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

						elif event.key == pygame.K_RIGHT:
							userx += 1
							if userx > 8:
								userx=8
							screen.fill("white")
							board.draw_board(sudoku.board)
							pygame.draw.rect(screen, "red", pygame.Rect(userx * 64, usery * 64, 64, 64), 2)
							board.draw_sketch(sketchboard)

				pygame.display.flip()
				clock.tick(60)

			while screen3:
				winner = sudoku.check_win()
				if winner == True:
					winbutton = game_win(screen)

					for event in pygame.event.get():

						if event.type == pygame.QUIT:
							running = False
							pygame.quit()
							sys.exit()

						if event.type == pygame.MOUSEBUTTONDOWN:
							x, y = event.pos
							if winbutton.collidepoint(x, y):
								running = False
								pygame.quit()
								sys.exit()

				else:
					lossbutton = game_over(screen)
					for event in pygame.event.get():

						if event.type == pygame.QUIT:
							running = False
							pygame.quit()
							sys.exit()

						if event.type == pygame.MOUSEBUTTONDOWN:
							x, y = event.pos
							if lossbutton.collidepoint(x, y):
								screen1 = True
								screen2 = True
								screen3 = False
								difficulty = None
								big_font = pygame.font.Font(None, 80)
								small_font = pygame.font.Font(None, 50)
								smaller_font = pygame.font.Font(None, 30)
								board = Board((64 * 9), (64 * 10), screen)
								startbuttons = display_start(screen)

								sketchboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0],
								               [0, 0, 0, 0, 0, 0, 0, 0, 0]]


				pygame.display.flip()
				clock.tick(60)
				

	finally:
		pygame.quit()

#variables


if __name__ == "__main__":
	main()