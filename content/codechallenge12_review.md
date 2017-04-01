Title: Code Challenge 12 - Build a Tic-tac-toe Game - Review
Date: 2017-04-01 17:00
Category: Challenges
Tags: codechallenges, learning, game, tictactoe, AI
Slug: codechallenge12_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge12.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Build a Tic-tac-toe Game](http://pybit.es/codechallenge12.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## Our solution and learning

You can find our solution [here](https://github.com/pybites/challenges/blob/solutions/12/tictactoe.py). This was great learning! Here are some highlights:

* We went for the AI opponent to play against. Not sure if it is unbeatable, but it has some 'intelligence' because it knows when to win, block you or take the next best moves (more on this later). We need to know a score for each position which we calculate by counting the number of times each position is in a winning combination:

		WINNING_COMBINATIONS = (
			(7, 8, 9), (4, 5, 6), (1, 2, 3),
			(7, 4, 1), (8, 5, 2), (9, 6, 3),
			(1, 5, 9), (7, 5, 3),
		)

		POSITION_VALUES = Counter(
			itertools.chain(*WINNING_COMBINATIONS)
		)

* Like Hangman, you have to keep state, so a class worked best for us and it is important to use a suitable data structure: a list of key numbers in the order of a typical key pad:

		VALID_POSITIONS = list(range(1, 10))
		...

		class TicTacToe:

			def __init__(self):
				self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0


		'''Simple tictactoe game, board positions are like keyboard
						7 8 9
						4 5 6
						1 2 3
		'''

		@clear_screen
		def __str__(self):
			return '''
				{} | {} | {}
				{} | {} | {}
				{} | {} | {}
			'''.format(*(self.board[7:] + self.board[4:7] + self.board[1:4]))

	The decorator is probably overkill but we use print(game) in two places so we did not want to duplicate code nor did we feel it was pure to clear the screen as part of \_\_str\_\_ (OK maybe we exaggerated, but the [decorator](https://en.wikipedia.org/wiki/Decorator_pattern) is a useful feature you probably end up using!)

* Probably the most important method is to determine if there is a win state. is_win() loops over all winning combinations and if there is not a DEFAULT (_) in the 3 positions and they are of the same ('O' or 'X') we have a win:

		def is_win(self):
			for combo in WINNING_COMBINATIONS:
				a, b, c = combo
				combo_vals = set([self.board[a], self.board[b], self.board[c]])
				if DEFAULT not in combo_vals and len(combo_vals) == 1:
					return True
			return False

* Under main we drive the interface. It is one of the few times we choose a "for / else" construct, which some advice against. However here we liked it because there is a clear use case: if we break out of the for loop we have a win, else we ended performing all max 9 turns/moves, so we enter the for's else = game ends in 'draw'. The advantage of this approach is that we did not have to calculate the 'draw' scenario. We separated computer vs manual into 2 methods: ai_move() and manual_move():

		while True:
			game = TicTacToe()

			turns = itertools.cycle([first, second])
			print(game)
			for _ in VALID_POSITIONS:
				player = next(turns)
				if player == COMPUTER:
					game.ai_move()
				else:
					game.manual_move()
				print(game)
				if game.is_win():
					print('Player {} wins'.format(player))
					break
			else:  # for / else is frowned upon, I do like it here though!
				print('Draw')

* The AI bit was the most interesting part. We went not as far as the full 8 steps in [tictactoe's strategy](https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy), yet this will give you a bit of challenge. The computer checks first if it can win (end) the game, then if the player can win, if so prevent (block) that. If none of these two situations, it takes the best next move based on the before mentioned POSITION_VALUES which is a counter so its most_common() method returns most valuable positions first. Splitting this in multiple methods makes it easier maintainable.

		def ai_move(self):
			self._win_or_block() or self._take_best_next_free_pos()

		def _win_or_block(self):
			for combo in WINNING_COMBINATIONS:
				a, b, c = combo
				combo_vals = [self.board[a], self.board[b], self.board[c]]
				# can only use unitiated positions
				if DEFAULT not in combo_vals:
					continue
				if combo_vals.count(COMPUTER) == 2:
					return self._update_board(combo, combo_vals)
				if combo_vals.count(PLAYER) == 2:
					return self._update_board(combo, combo_vals)
			return False

		def _take_best_next_free_pos(self):
			for pos, _ in POSITION_VALUES.most_common():
				if self.board[pos] == DEFAULT:
					self.board[pos] = COMPUTER
					return True
			return False

Again our full solution is [here](https://github.com/pybites/challenges/blob/solutions/12/tictactoe.py). Let us know if you have any questions or if you spot anything we could have done better.

## Community 

Here are some other ways to do it: from our [community branch](https://github.com/pybites/challenges/blob/community/12/tictactoe-atakume.py) (remember you can submit code by PR!) and [via reddit comment](https://redd.it/61o56j)). Reading other solutions to the same problem (as well as coding styles) is a great way to learn.

## Stay tuned

Next week you will train your data analysis skills by parsing a movie data set. It will be fun :)

We hope you are enjoying these challenges, learning along the way. Let us know [if you have any issue](https://github.com/pybites/challenges/issues/new) and/or [contact us](mailto:pybitesblog@gmail.com) if you want to submit a cool challenge. See you next week ...
