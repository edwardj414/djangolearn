// src/components/Sidebar.jsx
import { Link, useParams } from 'react-router-dom'
import { ChevronDown, ChevronRight, Circle, CheckCircle } from 'lucide-react'
import { useState } from 'react'

const DIFFICULTY_COLOR = {
  beginner: 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20',
  intermediate: 'bg-amber-500/10 text-amber-400 border border-amber-500/20',
  advanced: 'bg-rose-500/10 text-rose-400 border border-rose-500/20',
}

export default function Sidebar({ topics }) {
  const { topicSlug, lessonSlug } = useParams()
  const [collapsed, setCollapsed] = useState({})

  if (!topics?.length) return (
    <aside className="w-64 shrink-0 bg-[#0F0A1F] border-r border-white/5 p-4">
      <div className="animate-pulse space-y-3">
        {[...Array(8)].map((_, i) => (
          <div key={i} className="h-10 bg-white/5 rounded-lg" />
        ))}
      </div>
    </aside>
  )

  const toggle = (slug) => setCollapsed(c => ({ ...c, [slug]: !c[slug] }))

  return (
    <aside className="w-64 shrink-0 bg-[#0F0A1F] border-r border-white/5 overflow-y-auto sidebar-scroll sticky top-14 h-[calc(100vh-56px)]">
      <div className="p-5">
        <p className="text-[10px] font-bold text-slate-500 uppercase tracking-[0.2em] mb-4">
          Curriculum
        </p>
        {topics.map((topic) => {
          const isActive = topic.slug === topicSlug
          const isOpen = isActive || !collapsed[topic.slug]

          return (
            <div key={topic.slug} className="mb-2">
              <button
                onClick={() => toggle(topic.slug)}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-left text-sm font-medium transition-all
                  ${isActive ? 'bg-purple-600/10 text-purple-400 border border-purple-500/20' : 'text-slate-400 hover:bg-white/5'}`}
              >
                <span className="text-lg grayscale group-hover:grayscale-0">{topic.icon}</span>
                <span className="flex-1 truncate">{topic.title}</span>
                {isOpen
                  ? <ChevronDown size={14} className="opacity-40" />
                  : <ChevronRight size={14} className="opacity-40" />
                }
              </button>

              {isOpen && (
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
              )}
            </div>
          )
        })}
      </div>
    </aside>
  )
}