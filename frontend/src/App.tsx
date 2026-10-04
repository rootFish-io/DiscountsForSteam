import { useEffect, useState } from "react"
import Header from "./components/Header"
import SearchGame from "./components/SearchGame"

import type { GamesResponse, Game } from "./types/game"
import GameList from "./components/GameList"
import Pagination from './components/Pagination'

function App() {
	const [games, setGames] = useState<Game[]>([])
	const [page, setPage] = useState(1)
	const [totalPage, setTotalPage] = useState(0)

	async function fetchGames(page: number, limit: number): Promise<GamesResponse> {
		const response = await fetch(`http://127.0.0.1:8000/games?page=${page}&limit=${limit}`)

			return response.json()
	}

	useEffect(() => {
		async function loadGames() {
			const data = await fetchGames(page, 60)
			setGames(data.games)
			setTotalPage(data.total)
		}

		loadGames()
	}, [page])

	function onSetPage(action: number) {
		if (page + action > 0 && page + action < totalPage / 59) {
			setPage(page + action)		
			window.scrollTo({top: 0, left: 0, behavior: 'smooth'})
		}

	}

	return (
		<>
			<Header />
			<SearchGame />
			<GameList games={games} />
			<Pagination onSetPage={onSetPage} page={page} totalPage={totalPage}/>
		</>
	)
}

export default App
