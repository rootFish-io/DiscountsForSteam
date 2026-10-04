import '../styles/gameList.css'
import type { Game } from "../types/game"
import GameItem from "./GameItem"

interface GameListProps {
	games: Game[]
}

function GameList({ games }: GameListProps) {
	return (
		<ul className="game-list">
		{
			games.map((game) => (
				<GameItem 
					key={game.steam_app_id}
					name={game.name}
					price={game.price}
					discounted_price={game.discounted_price}
					url={game.url}
					discount_percent={game.discount_percent}
				/>
			))
		}  
		</ul>
	)
}

export default GameList
