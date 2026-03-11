import { Link, useParams } from 'react-router-dom'
import { ChevronDown, ChevronRight, ChevronLeft, Circle, CheckCircle, PanelLeftClose } from 'lucide-react'
import { useState } from 'react'

const DIFFICULTY_COLOR = {
  beginner: 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20',
  intermediate: 'bg-amber-500/10 text-amber-400 border border-amber-500/20',
  advanced: 'bg-rose-500/10 text-rose-400 border border-rose-500/20',
}

export default function Sidebar({ topics }) {
  const { topicSlug, lessonSlug } = useParams()
  const [collapsed, setCollapsed] = useState({})
  const [sidebarOpen, setSidebarOpen] = useState(true)

  const toggle = (slug) => setCollapsed(c => ({ ...c, [slug]: !c[slug] }))

  return (
    <div className="relative flex shrink-0">

      {/* ── Sidebar Panel ───────────────────────────────────── */}
      <aside
        className={`
          transition-all duration-300 ease-in-out overflow-hidden
          bg-[#0F0A1F] border-r border-white/5
          sticky top-14 h-[calc(100vh-56px)]
          ${sidebarOpen ? 'w-64' : 'w-0'}
        `}
      >
        <div className={`
          w-64 h-full flex flex-col overflow-y-auto sidebar-scroll
          transition-opacity duration-200
          ${sidebarOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'}
        `}>

          {/* Header */}
          <div className="flex items-center justify-between px-5 pt-5 pb-2 shrink-0">
            <p className="text-[10px] font-bold text-slate-500 uppercase tracking-[0.2em]">
              Curriculum
            </p>
            <button
              onClick={() => setSidebarOpen(false)}
              className="p-1 rounded-md text-slate-600 hover:text-slate-300 hover:bg-white/5 transition-colors"
              title="Collapse sidebar"
            >
              <PanelLeftClose size={14} />
            </button>
          </div>

          {/* Loading skeleton */}
          {!topics?.length
            ? <div className="px-5 pt-2 space-y-3">
                {[...Array(8)].map((_, i) => (
                  <div key={i} className="h-10 bg-white/5 rounded-lg animate-pulse" />
                ))}
              </div>

            /* Topic list */
            : <div className="px-5 pb-5 pt-2">
                {topics.map((topic) => {
                  const isActive = topic.slug === topicSlug
                  const isOpen = isActive || !collapsed[topic.slug]

                  return (
                    <div key={topic.slug} className="mb-2">

                      {/* Topic toggle button */}
                      <button
                        onClick={() => toggle(topic.slug)}
                        className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-left text-sm font-medium transition-all
                          ${isActive
                            ? 'bg-purple-600/10 text-purple-400 border border-purple-500/20'
                            : 'text-slate-400 hover:bg-white/5'
                          }`}
                      >
                        <span className="text-lg grayscale group-hover:grayscale-0">{topic.icon}</span>
                        <span className="flex-1 truncate">{topic.title}</span>
                        <span className={`transition-transform duration-200 ${isOpen ? 'rotate-0' : '-rotate-90'}`}>
                          <ChevronDown size={14} className="opacity-40" />
                        </span>
                      </button>

                      {/* Lessons — animated expand/collapse */}
                      <div className={`
                        overflow-hidden transition-all duration-200 ease-in-out
                        ${isOpen ? 'max-h-[600px] opacity-100' : 'max-h-0 opacity-0'}
                      `}>
                        <div className="ml-4 mt-2 space-y-1 border-l border-white/5 pl-2">
                          {topic.lessons.map((lesson) => {
                            const isCurrent = lesson.slug === lessonSlug && topic.slug === topicSlug
                            return (
                              <Link
                                key={lesson.slug}
                                to={`/topic/${topic.slug}/${lesson.slug}`}
                                className={`flex items-center gap-3 px-3 py-2 rounded-lg text-xs transition-all
                                  ${isCurrent
                                    ? 'bg-purple-600 text-white font-semibold shadow-lg shadow-purple-900/40'
                                    : 'text-slate-500 hover:text-slate-300 hover:bg-white/5'
                                  }`}
                              >
                                {isCurrent
                                  ? <CheckCircle size={12} />
                                  : <Circle size={12} className="opacity-30" />
                                }
                                <span className="flex-1 truncate">{lesson.title}</span>
                                {!isCurrent && (
                                  <span className={`text-[9px] px-1.5 py-0.5 rounded-md font-bold uppercase border ${DIFFICULTY_COLOR[lesson.difficulty]}`}>
                                    {lesson.difficulty[0]}
                                  </span>
                                )}
                              </Link>
                            )
                          })}
                        </div>
                      </div>

                    </div>
                  )
                })}
              </div>
          }
        </div>
      </aside>

      {/* ── Toggle Tab (always visible on the edge) ─────────── */}
      <button
        onClick={() => setSidebarOpen(o => !o)}
        title={sidebarOpen ? 'Collapse sidebar' : 'Expand sidebar'}
        className={`
          absolute top-6 z-20
          flex items-center justify-center
          w-5 h-10 rounded-r-lg
          bg-purple-600 hover:bg-purple-500 active:bg-purple-700
          text-white shadow-lg shadow-purple-900/50
          transition-all duration-300
          ${sidebarOpen ? 'left-64' : 'left-0'}
        `}
      >
        {sidebarOpen
          ? <ChevronLeft size={13} />
          : <ChevronRight size={13} />
        }
      </button>

    </div>
  )
}
