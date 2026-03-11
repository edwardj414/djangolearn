import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import TopicPage from './pages/TopicPage'
import LessonPage from './pages/LessonPage'
import Compiler from './pages/Compiler'

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gradient-to-tr from-violet-500 to-purple-900">
        <Navbar />
        <div className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/topic/:topicSlug" element={<TopicPage />} />
            <Route path="/topic/:topicSlug/:lessonSlug" element={<LessonPage />} />
            <Route path="/Compiler" element={<Compiler />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  )
}
