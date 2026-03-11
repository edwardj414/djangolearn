import { useEffect, useState } from 'react'
import { useParams, Navigate } from 'react-router-dom'
import { getTopics } from '../api'
import Sidebar from '../components/Sidebar'
import { BookOpen, ArrowRight } from 'lucide-react'
import { Link } from 'react-router-dom'

export default function TopicPage() {
  const { topicSlug } = useParams()
  const [topics, setTopics] = useState([])
  const [topic, setTopic] = useState(null)

  useEffect(() => {
    getTopics().then(({ data }) => {
      setTopics(data)
      const t = data.find(t => t.slug === topicSlug)
      setTopic(t)
    })
  }, [topicSlug])

  // Redirect to first lesson if topic found
  if (topic?.lessons?.length > 0) {
    return <Navigate to={`/topic/${topicSlug}/${topic.lessons[0].slug}`} replace />
  }

  return (
    <div className="flex">
      <Sidebar topics={topics} />
      <main className="flex-1 p-10 flex items-center justify-center text-gray-500">
        {topic ? 'No lessons yet.' : 'Loading...'}
      </main>
    </div>
  )
}
