import { useState, type FormEvent } from "react"

import Header from "./components/Header"
import SearchGame from "./components/SearchGame"
import GameList from "./components/GameList"
import Pagination from "./components/Pagination"
import GameSkeleton from "./components/GameSkeleton"
import FilterModal from "./components/FilterModal"

import { useGames } from "./hooks/useGames"

function App() {
    const [page, setPage] = useState(1)
    const [isFilterOpen, setIsFilterOpen] = useState(false)

    const { games, totalPage, loading, maxDiscountedPrice } = useGames(page)

    function onSetPage(action: number) {
        if (page + action > 0 && page + action < totalPage / 59) {
            setPage(page + action)
            window.scrollTo({ top: 0, left: 0, behavior: "smooth" })
        }
    }

    function handlerSubmit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
    }

    function toggleFilters() {
        setIsFilterOpen(!isFilterOpen)
    }

    return (
        <>
            <Header page={page}/>
            <SearchGame
                toggleFilters={toggleFilters}
                handlerSubmit={handlerSubmit}
            />

            {loading ? <GameSkeleton /> : <GameList games={games} />}

            <Pagination
                onSetPage={onSetPage}
                page={page}
                totalPage={totalPage}
            />

            <FilterModal
                isOpen={isFilterOpen}
                handlerSubmit={handlerSubmit}
                toggleFilter={toggleFilters}
                maxDiscountedPrice={maxDiscountedPrice}
            />
        </>
    )
}

export default App
