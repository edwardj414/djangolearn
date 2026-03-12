// src/pages/Home.jsx
import { useEffect, useState } from 'react'
import { Link, useLocation } from 'react-router-dom' // ADDED: useLocation
import { getTopics } from '../api'
import { BookOpen, Code2, Zap, ArrowRight, Users, Star } from 'lucide-react'

// Animated Number Component
function AnimatedNumber({ value, suffix = '' }) {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const target = parseInt(value, 10);
    if (isNaN(target)) return;

    let start = 0;
    const duration = 2000;
    const increment = target / (duration / 16);

    const timer = setInterval(() => {
      start += increment;
      if (start >= target) {
        setCount(target);
        clearInterval(timer);
      } else {
        setCount(Math.ceil(start));
      }
    }, 16);

    return () => clearInterval(timer);
  }, [value]);

  if (isNaN(parseInt(value, 10))) {
    return <>{value}{suffix}</>;
  }
  return <>{count}{suffix}</>;
}

// Updated badge colors for dark theme
const DIFF_BADGE = {
  beginner: 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20',
  intermediate: 'bg-amber-500/10 text-amber-400 border border-amber-500/20',
  advanced: 'bg-rose-500/10 text-rose-400 border border-rose-500/20',
}

export default function Home() {
  const [topics, setTopics] = useState([])
  const [loading, setLoading] = useState(true)

  // NEW: Get current route location to read the hash
  const location = useLocation();

  // NEW: Scroll to the topics section if the URL has #topics
  useEffect(() => {
    if (location.hash === '#topics') {
      const element = document.getElementById('topics');
      if (element) {
        // Adding a slight delay ensures the DOM has painted before scrolling
        setTimeout(() => {
          element.scrollIntoView({ behavior: 'smooth' });
        }, 100);
      }
    }
  }, [location]);

  useEffect(() => {
    getTopics().then(({ data }) => { setTopics(data); setLoading(false) })
      .catch(() => setLoading(false))
  }, [])

  return (
    // The main wrapper is now relative to hold the layers properly
    <div className="min-h-screen bg-[#0F0A1F] text-slate-200 relative selection:bg-purple-500/30">

      {/* FULL PAGE DYNAMIC BACKGROUND */}
      <div className="fixed inset-0 w-full h-full pointer-events-none z-0 flex justify-center items-center overflow-hidden">
        {/* Top Left Purple Glow */}
        <div className="absolute top-[-5%] left-[5%] w-[30rem] h-[30rem] bg-purple-600/30 rounded-full mix-blend-screen blur-[120px] animate-blob"></div>

        {/* Top Right Indigo Glow */}
        <div className="absolute top-[10%] right-[5%] w-[30rem] h-[30rem] bg-indigo-600/30 rounded-full mix-blend-screen blur-[120px] animate-blob animation-delay-2000"></div>

        {/* Bottom Left Fuchsia Glow */}
        <div className="absolute bottom-[10%] left-[20%] w-[35rem] h-[35rem] bg-fuchsia-600/20 rounded-full mix-blend-screen blur-[120px] animate-blob animation-delay-4000"></div>

        {/* Bottom Right Violet Glow so the bottom of the page isn't dark */}
        <div className="absolute bottom-[-10%] right-[10%] w-[30rem] h-[30rem] bg-violet-600/20 rounded-full mix-blend-screen blur-[120px] animate-blob animation-delay-2000"></div>
      </div>

      {/* ALL PAGE CONTENT (wrapped in z-10 so it sits ABOVE the floating background) */}
      <div className="relative z-10">

        {/* Hero Section */}
        <div className="max-w-5xl mx-auto px-6 py-24 text-center">
          <div className="inline-flex items-center gap-2 bg-purple-500/10 border border-purple-500/30 rounded-full px-4 py-1.5 text-sm mb-6 text-purple-300">
            <Zap size={14} /> Learn Django Interactively
          </div>
          <h1 className="text-5xl md:text-6xl font-extrabold mb-6 leading-tight text-white">
            Master Django,<br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-300">
                One Lesson at a Time
            </span>
          </h1>
          <p className="text-lg text-slate-400 max-w-xl mx-auto mb-10">
            Interactive tutorials with live code execution. No setup needed — write and run Python code right in your browser.
          </p>

          <div className="flex gap-4 justify-center">
            <Link
              to="/topic/getting-started"
              className="bg-purple-600 text-white font-bold px-8 py-3 rounded-xl hover:bg-purple-500 transition shadow-lg shadow-purple-900/20 flex items-center gap-2 hover:-translate-y-1 duration-300 ease-out"
            >
              Start Learning <ArrowRight size={16} />
            </Link>

            <Link
              to="/compiler"
              className="bg-white/5 border border-purple-500/30 text-purple-300 font-bold px-8 py-3 rounded-xl hover:bg-white/10 hover:border-purple-400 transition flex items-center gap-2 hover:-translate-y-1 duration-300 ease-out backdrop-blur-sm"
            >
              <Code2 size={16} /> Open Playground
            </Link>
          </div>

          {/* Stats Section */}
          <div className="flex justify-center gap-12 mt-16 text-center border-t border-white/5 pt-12">
            {[
              {
                icon: <BookOpen size={18} />,
                stat: topics.reduce((a, t) => a + t.lessons.length, 0) || 25,
                label: 'Lessons'
              },
              { icon: <Code2 size={18} />, stat: 'Python', label: 'Language' },
              { icon: <Users size={18} />, stat: 'Free', label: 'Forever' },
              { icon: <Star size={18} />, stat: 100, suffix: '%', label: 'Interactive' },
            ].map(({ icon, stat, label, suffix }, index) => (
              <div
                key={label}
                className="flex flex-col items-center gap-1 animate-in fade-in slide-in-from-bottom-4 duration-700 fill-mode-both"
                style={{ animationDelay: `${index * 150}ms` }}
              >
                <div className="text-purple-400 mb-1.5">{icon}</div>
                <span className="text-3xl font-extrabold text-white tracking-tight">
                  <AnimatedNumber value={stat} suffix={suffix} />
                </span>
                <span className="text-slate-400 text-sm font-medium uppercase tracking-wider">{label}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Topics Grid: Glassmorphism */}
        {/* ADDED: id="topics" so the scroll function can find it */}
        <div id="topics" className="max-w-5xl mx-auto px-6 py-20">
          <h2 className="text-3xl font-bold text-white mb-2">All Topics</h2>
          <p className="text-purple-200/60 mb-10">Structured from beginner to advanced — start anywhere.</p>

          {loading ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {[...Array(6)].map((_, i) => (
                <div key={i} className="bg-white/[0.02] rounded-2xl p-6 border border-white/5 animate-pulse h-52" />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {topics.map((topic) => (
                <Link
                  key={topic.slug}
                  to={`/topic/${topic.slug}/${topic.lessons[0]?.slug || ''}`}
                  className="group flex flex-col bg-white/[0.03] backdrop-blur-md rounded-2xl p-6 border border-white/5
                             hover:border-purple-500/30 hover:bg-white/[0.06]
                             hover:-translate-y-2 hover:shadow-2xl hover:shadow-purple-900/40
                             transition-all duration-500 ease-out"
                >
                  <div className="text-4xl mb-4 grayscale opacity-70 group-hover:grayscale-0 group-hover:opacity-100 transition-all duration-500 group-hover:scale-110 origin-left">
                    {topic.icon}
                  </div>

                  <h3 className="font-bold text-xl text-white group-hover:text-purple-300 transition-colors duration-300 mb-2">
                    {topic.title}
                  </h3>

                  <p className="text-sm text-purple-50/60 mb-6 line-clamp-2 leading-relaxed group-hover:text-purple-50/80 transition-colors duration-300">
                    {topic.description}
                  </p>

                  <div className="flex items-center justify-between mt-auto pt-4 border-t border-white/10 group-hover:border-purple-500/20 transition-colors duration-300">
                    <span className="text-xs font-medium text-purple-200/50 group-hover:text-purple-200/80 transition-colors duration-300">
                      {topic.lessons.length} lessons
                    </span>
                    <div className="flex gap-1">
                      {[...new Set(topic.lessons.map(l => l.difficulty))].map(d => (
                        <span key={d} className={`text-[10px] px-2 py-0.5 rounded-full font-bold uppercase tracking-wider ${DIFF_BADGE[d]}`}>
                          {d[0]}
                        </span>
                      ))}
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>

        {/* Dark Theme Features Section */}
        <div className="border-t border-white/5 py-24">
          <div className="max-w-5xl mx-auto px-6 text-center">
            <h2 className="text-3xl font-bold text-white mb-12">Why DjangoLearn?</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {[
                { icon: '⚡', title: 'Live Code Editor', desc: 'Run Python code directly in your browser. No installation required.' },
                { icon: '📚', title: 'Structured Content', desc: 'From installation to deployment — everything in a logical order.' },
                { icon: '️‍⛓️‍💥', title: 'Completely Free', desc: 'Open source and free forever. No account needed to start learning.' },
              ].map(f => (
                <div key={f.title} className="bg-white/[0.03] backdrop-blur-md rounded-2xl p-8 border border-white/5 hover:border-purple-500/30 transition-colors duration-300">
                  <div className="text-5xl mb-6">{f.icon}</div>
                  <h3 className="font-bold text-xl text-white mb-3">{f.title}</h3>
                  <p className="text-purple-200/60 leading-relaxed">{f.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}