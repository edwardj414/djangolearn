import { useEffect, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { getTopics, getLesson } from '../api'
import Sidebar from '../components/Sidebar'
import LessonContent from '../components/LessonContent'
import CodeEditor from '../components/CodeEditor'
import { ChevronLeft, ChevronRight, Clock, BarChart2 } from 'lucide-react'

// Updated colors for Dark/Purple Theme
const DIFF_COLOR = {
  beginner: 'text-emerald-400 bg-emerald-500/10 border border-emerald-500/20',
  intermediate: 'text-amber-400 bg-amber-500/10 border border-amber-500/20',
  advanced: 'text-rose-400 bg-rose-500/10 border border-rose-500/20',
}

export default function LessonPage() {
  const { topicSlug, lessonSlug } = useParams()
  const navigate = useNavigate()
  const [topics, setTopics] = useState([])
  const [lesson, setLesson] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    Promise.all([getTopics(), getLesson(topicSlug, lessonSlug)])
      .then(([{ data: topicsData }, { data: lessonData }]) => {
        setTopics(topicsData)
        setLesson(lessonData)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [topicSlug, lessonSlug])

  // Build flat lesson list for prev/next navigation
  const allLessons = topics.flatMap(t =>
    t.lessons.map(l => ({ ...l, topicSlug: t.slug, topicTitle: t.title }))
  )
  const currentIdx = allLessons.findIndex(
    l => l.slug === lessonSlug && l.topicSlug === topicSlug
  )
  const prev = currentIdx > 0 ? allLessons[currentIdx - 1] : null
  const next = currentIdx < allLessons.length - 1 ? allLessons[currentIdx + 1] : null

  return (
    <div className="flex min-h-[calc(100vh-56px)] bg-[#0F0A1F]">
      <Sidebar topics={topics} />

      <main className="flex-1 overflow-auto bg-[#0F0A1F]">
        {loading ? (
          <div className="max-w-3xl mx-auto p-10 animate-pulse space-y-4">
            <div className="h-8 bg-white/5 rounded w-2/3" />
            <div className="h-4 bg-white/5 rounded w-full" />
            <div className="h-4 bg-white/5 rounded w-5/6" />
            <div className="h-64 bg-white/5 rounded" />
          </div>
        ) : lesson ? (
          <div className="max-w-3xl mx-auto px-8 py-10">
            {/* Breadcrumb - Softened for Dark Mode */}
            <div className="flex items-center gap-2 text-sm text-slate-500 mb-6">
              <Link to="/" className="hover:text-purple-400 transition-colors">Home</Link>
              <span>/</span>
              <Link to={`/topic/${topicSlug}`} className="hover:text-purple-400 transition-colors capitalize">
                {lesson.topic_title}
              </Link>
              <span>/</span>
              <span className="text-slate-300 font-medium">{lesson.title}</span>
            </div>

            {/* Lesson header */}
            <div className="mb-10">
              <div className="flex items-center gap-3 mb-4">
                <span className={`text-[10px] font-bold uppercase tracking-widest px-2.5 py-1 rounded-md ${DIFF_COLOR[lesson.difficulty]}`}>
                  <BarChart2 size={10} className="inline mr-1 mb-0.5" />
                  {lesson.difficulty}
                </span>
                <span className="text-xs text-slate-500 flex items-center gap-1">
                  <Clock size={12} /> ~5 min read
                </span>
              </div>
              <h1 className="text-4xl font-extrabold text-white tracking-tight">{lesson.title}</h1>
            </div>

            {/* Content - Passing down the theme context */}
            <div className="prose prose-invert prose-purple max-w-none text-slate-300">
              <LessonContent content={lesson.content} />
            </div>

            {/* Architecture Visualization for High-Level Understanding */}


            {/* Code Editor - Glass Container */}
            {lesson.code_example && (
              <div className="mt-12 p-1 rounded-2xl bg-gradient-to-br from-purple-500/20 to-indigo-500/20 border border-white/10">
                <div className="bg-[#1A122E]/80 backdrop-blur-md p-6 rounded-xl">
                  <h2 className="text-lg font-bold text-white mb-1 flex items-center gap-2">
                    <span className="p-1 bg-purple-500 rounded text-xs italic">🧪</span> Try it Yourself
                  </h2>
                  <p className="text-sm text-slate-400 mb-4">
                    Edit the code below and click <strong className="text-purple-300">Run Code</strong> to see results instantly.
                  </p>
                  <CodeEditor defaultCode={lesson.code_example} />
                </div>
              </div>
            )}

            {/* Prev / Next Navigation */}
            <div className="flex items-center justify-between mt-16 pt-8 border-t border-white/5">
              {prev ? (
                <Link
                  to={`/topic/${prev.topicSlug}/${prev.slug}`}
                  className="flex items-center gap-3 text-sm text-slate-400 hover:text-purple-400 font-medium group transition-all"
                >
                  <div className="p-2 bg-white/5 rounded-lg group-hover:bg-purple-500/20 transition-colors">
                    <ChevronLeft size={18} />
                  </div>
                  <div>
                    <div className="text-[10px] uppercase tracking-wider text-slate-600">Previous</div>
                    <div className="text-slate-300 group-hover:text-white">{prev.title}</div>
                  </div>
                </Link>
              ) : <div />}

              {next ? (
                <Link
                  to={`/topic/${next.topicSlug}/${next.slug}`}
                  className="flex items-center gap-3 text-sm text-slate-400 hover:text-purple-400 font-medium group text-right transition-all"
                >
                  <div>
                    <div className="text-[10px] uppercase tracking-wider text-slate-600">Next</div>
                    <div className="text-slate-300 group-hover:text-white">{next.title}</div>
                  </div>
                  <div className="p-2 bg-white/5 rounded-lg group-hover:bg-purple-500/20 transition-colors">
                    <ChevronRight size={18} />
                  </div>
                </Link>
              ) : (
                <Link to="/" className="text-sm text-purple-400 font-bold hover:bg-purple-500/10 px-4 py-2 rounded-lg transition-all">
                  Finish Course →
                </Link>
              )}
            </div>
          </div>
        ) : (
          <div className="flex items-center justify-center h-full text-slate-600">
            Lesson not found.
          </div>
        )}
      </main>
    </div>
  )
}
