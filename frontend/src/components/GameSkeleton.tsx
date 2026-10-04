import '../styles/gameSkeleton.css'

function GameSkeleton() {
    const el = []

    for (let i = 0; i <  60; i++) {
        el.push(<li></li>)
    }

    return (
        <ul className='skeleton-list'>{el}</ul>
    )
}

export default GameSkeleton