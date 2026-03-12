import { useState, useRef, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Search, X, BookOpen } from 'lucide-react'
import { searchLessons } from '../api'

export default function Navbar() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  const [open, setOpen] = useState(false)
  const navigate = useNavigate()
  const ref = useRef(null)

  useEffect(() => {
    const handler = (e) => { if (!ref.current?.contains(e.target)) setOpen(false) }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  const handleSearch = async (e) => {
    const q = e.target.value
    setQuery(q)
    if (q.length > 1) {
      try {
        const { data } = await searchLessons(q)
        setResults(data)
        setOpen(true)
      } catch { setResults([]) }
    } else {
      setResults([])
      setOpen(false)
    }
  }

  return (
    <nav className="bg-[#0F0A1F]/80 backdrop-blur-md border-b border-white/5 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 h-14 flex items-center gap-6">
        {/* Logo - Matches Sidebar Purple */}
        <Link to="/" className="flex items-center gap-2 font-bold text-xl text-purple-400 shrink-0">
          <BookOpen size={24} className="text-purple-500" />
          <span className="tracking-tight text-white">Django<span className="text-purple-400">Learn</span></span>
        </Link>

        {/* Search - Glass Effect */}
        <div ref={ref} className="relative flex-1 max-w-md">
          <div className="flex items-center bg-white/5 border border-white/10 rounded-xl px-3 gap-2 focus-within:border-purple-500/50 transition-all">
            <Search size={16} className="text-slate-500" />
            <input
              className="bg-transparent py-2 w-full text-sm outline-none text-slate-200 placeholder-slate-500"
              placeholder="Search topics, lessons..."
              value={query}
              onChange={handleSearch}
              onFocus={() => results.length > 0 && setOpen(true)}
            />
            {query && (
              <button onClick={() => { setQuery(''); setResults([]); setOpen(false) }}>
                <X size={14} className="text-slate-500 hover:text-white" />
              </button>
            )}
          </div>

          {/* Search Results - Glassmorphism Dropdown */}
          {open && results.length > 0 && (
            <div className="absolute top-full mt-2 w-full bg-[#1A122E] border border-white/10 rounded-xl shadow-2xl overflow-hidden z-50 backdrop-blur-xl">
              {results.map((r, i) => (
                <button
                  key={i}
                  /* Added 'group' class here to control hover states of children */
                  className="group w-full text-left px-4 py-3 hover:bg-purple-600/20 flex flex-col border-b border-white/5 last:border-0 transition-colors"
                  onClick={() => { navigate(r.url); setOpen(false); setQuery('') }}
                >
                  <span className="text-sm font-medium text-slate-200 group-hover:text-white transition-colors">{r.title}</span>
                  <span className="text-[10px] uppercase tracking-wider font-bold text-purple-400/60 group-hover:text-purple-400/90 transition-colors">{r.topic}</span>
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Nav Links */}
        <div className="hidden md:flex items-center gap-6 ml-auto">
          {/* UPDATED: changed to="/#topics" */}
          <Link to="/#topics" className="text-sm text-slate-400 hover:text-purple-400 font-medium transition-colors">
            Tutorials
          </Link>
          <a
            href="https://docs.djangoproject.com"
            target="_blank"
            rel="noreferrer"
            className="text-sm text-slate-400 hover:text-purple-400 font-medium transition-colors flex items-center gap-1"
          >
            Official Docs <span className="text-[10px] opacity-50">↗</span>
          </a>
        </div>
      </div>
    </nav>
  )
}