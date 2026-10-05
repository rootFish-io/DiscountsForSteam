import { useState } from "react"

import Header from "./components/Header"
import SearchGame from "./components/SearchGame"
import GameList from "./components/GameList"
import Pagination from "./components/Pagination"
import GameSkeleton from "./components/GameSkeleton"

import { useGames } from './hooks/useGames'

function App() {
    const [page, setPage] = useState(1)
    const { games, totalPage, loading } = useGames(page)

    function onSetPage(action: number) {
        if (page + action > 0 && page + action < totalPage / 59) {
            setPage(page + action)
            window.scrollTo({ top: 0, left: 0, behavior: "smooth" })
        }
    }

    return (
        <>
            <Header />
            <SearchGame />
            {loading ? <GameSkeleton /> : <GameList games={games} />}
            <Pagination
                onSetPage={onSetPage}
                page={page}
                totalPage={totalPage}
            />
        </>
    )
}

export default App
