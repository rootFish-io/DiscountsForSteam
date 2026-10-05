import "../styles/gameItem.css"
import fallbackImage from "../assets/fallbackImage.png"
import type { Game } from "../types/game"

function GameItem({
    name,
    price,
    discounted_price,
    url,
    discount_percent,
}: Game) {
    return (
        <li>
            <img
                src={url}
                onError={(e) => {
                    const target = e.currentTarget
                    target.onerror = null
                    target.src = fallbackImage
                }}
            />
            <div className="info">
                <div className="name">{name}</div>

                <div className="container-price">
                    <div className="price">
                        <span>{discounted_price}$</span> <del>{price}$</del>
                    </div>
                    <span className="save">-{discount_percent}%</span>
                </div>
            </div>
        </li>
    )
}

export default GameItem
