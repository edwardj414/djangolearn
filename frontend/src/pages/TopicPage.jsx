// src/pages/TopicPage.jsx
import { useEffect, useState } from 'react'
import { useParams, Navigate, Link } from 'react-router-dom'
import { getTopics } from '../api'
import Sidebar from '../components/Sidebar'
import { BookOpen, ArrowRight, Sparkles } from 'lucide-react'

export default function TopicPage() {
  const { topicSlug } = useParams()
  const [topics, setTopics] = useState([])
  const [topic, setTopic] = useState(null)
  const [loading, setLoading] = useState(true)

  // State for the countdown timer
  const [timeLeft, setTimeLeft] = useState(50)

  // Fetch data
  useEffect(() => {
    setLoading(true)
    getTopics().then(({ data }) => {
      setTopics(data)
      const t = data.find(t => t.slug === topicSlug)
      setTopic(t)
      setLoading(false)
    }).catch(() => setLoading(false))
  }, [topicSlug])

  // Timer logic
  useEffect(() => {
    // Only start the countdown if it's done loading and there are no lessons
    if (!loading && (!topic?.lessons || topic.lessons.length === 0)) {
      if (timeLeft <= 0) return; // Stop at 0

      const timer = setInterval(() => {
        setTimeLeft((prev) => prev - 1)
      }, 1000)

      // Cleanup the interval when the component unmounts
      return () => clearInterval(timer)
    }
  }, [loading, topic, timeLeft])

  // Redirect to first lesson if topic found and lessons exist
  if (topic?.lessons?.length > 0) {
    return <Navigate to={`/topic/${topicSlug}/${topic.lessons[0].slug}`} replace />
  }

  return (
    <div className="flex min-h-[calc(100vh-56px)] bg-[#0F0A1F]">
      <Sidebar topics={topics} />

      <main className="flex-1 flex flex-col items-center justify-center bg-[#0F0A1F]">
        {loading ? (
          <div className="flex flex-col items-center gap-5">
            <div className="relative w-12 h-12">
              <div className="absolute inset-0 border-4 border-purple-900/20 rounded-full"></div>
              <div className="absolute inset-0 border-4 border-t-purple-500 rounded-full animate-spin"></div>
            </div>
            <p className="text-purple-400/80 font-mono text-xs animate-pulse tracking-[0.3em] uppercase">
              Loading Topic...
            </p>
          </div>
        ) : (
          /* Upgraded "Empty State" with Dynamic Timer & Easter Egg */
          <div className="flex flex-col items-center text-center max-w-md p-8 bg-white/[0.03] border border-white/5 rounded-2xl backdrop-blur-sm shadow-2xl transition-all duration-500">
            <div className="p-4 bg-purple-500/10 rounded-full mb-4">
              {timeLeft > 0 ? (
                <BookOpen size={32} className="text-purple-400" />
              ) : (
                <Sparkles size={32} className="text-indigo-400 animate-pulse" />
              )}
            </div>

            {/* NEW: Conditional UI based on the timer hitting 0 */}
            {timeLeft > 0 ? (
              <>
                <h2 className="text-2xl font-bold text-white mb-2 font-mono">
                  Coming in <span className="text-purple-400">{timeLeft}</span>s
                </h2>
                <p className="text-slate-400 mb-8 leading-relaxed">
                  The lessons for <span className="text-purple-300 font-semibold">{topic?.title || 'this topic'}</span> are currently being written. Check back soon!
                </p>
              </>
            ) : (
              <>
                <h2 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-400 mb-2 animate-bounce">
                  Time's Up! 🚀
                </h2>
                <p className="text-slate-400 mb-8 leading-relaxed animate-in fade-in duration-700">
                  Just kidding! Writing top-tier Django lessons takes a <i className="text-slate-300">little</i> longer than 50 seconds. We're working hard on <span className="text-purple-300 font-semibold">{topic?.title || 'this topic'}</span> right now!
                </p>
              </>
            )}

            <Link 
              to="/" 
              className="bg-purple-600 text-white font-bold px-6 py-2.5 rounded-xl hover:bg-purple-500 transition shadow-lg shadow-purple-900/20 flex items-center gap-2"
            >
              Browse All Topics <ArrowRight size={16} />
            </Link>
          </div>
        )}
      </main>
    </div>
  )
}