// LessonContent.jsx
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'

export default function LessonContent({ content }) {
  return (
    <div className="prose prose-invert max-w-none prose-purple">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          code({ node, inline, className, children, ...props }) {
            const match = /language-(\w+)/.exec(className || '')
            const textContent = String(children).replace(/\n$/, '')

            // 1. Detect Lifecycle Flow (Plain block with ↓ arrows)
            if (!inline && !match && textContent.includes('↓')) {
              const lines = textContent.split('\n')
              return (
                <div className="flex flex-col items-center my-8 w-full max-w-md font-mono text-sm">
                  {lines.map((line, index) => {
                    const text = line.trim()
                    if (!text) return null
                    if (text === '↓') {
                      return <div key={index} className="text-purple-500 font-bold text-2xl my-2 animate-pulse">↓</div>
                    }
                    return (
                      <div key={index} className="w-full bg-purple-900/40 text-purple-200 border border-purple-500/30 px-4 py-3 rounded-xl shadow-lg text-center">
                        {text}
                      </div>
                    )
                  })}
                </div>
              )
            }

            // 2. Multi-line Code Blocks (e.g., ```bash, ```python, or plain ``` for folder trees)
            if (!inline) {
              return (
                <div className="relative group my-6 w-full">
                  <div className="absolute -inset-0.5 bg-gradient-to-r from-purple-500 to-indigo-500 rounded-lg blur opacity-20"></div>
                  <SyntaxHighlighter
                    style={oneDark}
                    // Defaults to 'text' for folder structures so it doesn't apply wrong colors
                    language={match ? match[1] : 'text'}
                    PreTag="div"
                    className="!rounded-lg !text-sm !m-0 !bg-[#1A122E] border border-white/10"
                    codeTagProps={{ style: { backgroundColor: 'transparent', border: 'none', padding: 0 } }}
                    {...props}
                  >
                    {textContent}
                  </SyntaxHighlighter>
                </div>
              )
            }

            // 3. Inline Code (Single backticks inside paragraphs like `settings.py`)
            return (
              <code
                // THE FIX: !inline-block forces it to stay inline with the text
                className="!inline-block bg-purple-500/10 text-purple-300 border border-purple-500/20 px-1.5 py-0.5 mx-0.5 rounded-md font-mono text-[0.9em] leading-tight"
                {...props}
              >
                {children}
              </code>
            )
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}