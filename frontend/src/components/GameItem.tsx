import '../styles/gameItem.css'
import fallbackImage from '../assets/fallbackImage.jpeg'
import type { Game } from "../types/game"

function GameItem({ steam_app_id, name, price, discounted_price}: Game) {
	return (
		<li>
			<img 
				src={`https://cdn.cloudflare.steamstatic.com/steam/apps/${steam_app_id}/capsule_616x353.jpg`} 
				onError={(e) => {
					const target = e.currentTarget
					target.onerror = null
					target.src = fallbackImage
				}}
			/>
			<div className='info'>
				<div className='name'>{name}</div>

				<div className='container-price'>
					<span>{discounted_price}$</span>
					<del>{price}$</del>
				</div>
			</div>
		</li>
	)
}

export default GameItem
