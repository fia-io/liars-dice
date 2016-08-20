#Liar's Dice Game Interface

##Setup (pre-game)
###create
  - IN: player_count, player1_name, player2_name... playerX_name
  - OUT: game_id, game_status, (optional) round_number
  
  __Rules:__
     - Maximum X players. 
     - game_status will be one of 'not_started', 'playing', 'ended'
     - if game_status is 'playing', round_number will indicate the current round of the game.
     - the player calling create is always player1
  
###game_list
  - IN: player_name
  - OUT: game_ids()
  
  __Rules:__
    - Array game_ids contains list of games that a) contain player name and b) have game status of 'not_started'
    - If no games available for player_name, game_ids() will be empty.

###join_game
  - IN: player_name, game_id
  - OUT: game_id, game_status, (optional) round_number
  
  __Rules:__
     - Same return values as create
     - If all players specified in create have joined the game, game_status is 'playing' and the game has begun.
     
##Game Play

###start_game
  - IN: game_id
  - OUT: game_id, game_status(='playing'), round_number(=1)
  
  __Rules:__
     - Returns error if only 1 player has joined the game.
     - Client may enforce whether only player 1 can call start_game
     

###roll_dice
  - IN: player_name, game_id
  - OUT: dice(), game_id, player_name

__Rules:__
     - Returns error if this player has already rolled this round

###game_status
  - IN: game_id, player_name
  - OUT: game_id, game_status, round_number, player_turn(bool), dice(), bids()
  
  __Rules:__
     - player_turn returns true if it is player_name's turn, false otherwise
     - dice() contains current dice for player_name
     - bids() contains current bids for other players

###bid
  - IN: game_id, player_name, bid_die, bid_count
  - OUT: game_id, game_status, round_number, player_turn(bool=false), dice(), bids()

__Rules:__
     - Returns error if not player_name's turn
     - Return is otherwise the same as game_status
     
###challenge
  - IN: game_id, challenger_name, challengee_name
  - OUT: game_id, game_status, round_number, player_turn(bool=false), dice(), bids()
  
  __Rules:__
     - Returns error if not player_name's turn
     - Return is otherwise the same as game_status
