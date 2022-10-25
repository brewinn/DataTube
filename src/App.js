import { useState, useEffect } from 'react'
import Video from './components/Video'
import Notification from './components/notification'
import blogService from './services/videos'
import loginService from './services/login'

const App = () => {
  const [videos, setVideos] = useState([])
  const [user, setUser] = useState(null)
  const [errorMessage, setErrorMessage] = useState(null)
  const [username, setUsername] = useState('') 
  const [password, setPassword] = useState('')
  const [newTitle, setNewTitle] = useState('')
  const [newAuthor, setNewAuthor] = useState('')
  const [newUrl, setNewUrl] = useState('')

  useEffect(() => {
    blogService
      .getAll()
      .then(initialVideos => {
        setVideos(initialVideos)
      })
  }, [])

  useEffect(() => {
    const loggedUserJSON = window.localStorage.getItem('loggedBlogappUser')
    if (loggedUserJSON) {
      const user = JSON.parse(loggedUserJSON)
      setUser(user)
      blogService.setToken(user.token)
    }
  }, [])

  const userForm = () => (
      <form onSubmit={logoutUser}>{user.name} logged in 
        <button type="submit">logout</button>
      </form>
  )

  const handleBlogCreation = async (event) => {
    event.preventDefault()
    try {
      await blogService.setToken(user.token)
      
      const res = await blogService.create(
        {title:newTitle, author:newAuthor, url:newUrl})
        setErrorMessage(`New video: "${newTitle}",\nWritten by ${newAuthor} added`)
        setTimeout(() => {
          setErrorMessage(null)
        }, 5000)
      setVideos(videos.concat(res))
      setNewTitle('')
      setNewAuthor('')
      setNewUrl('')
    } catch (exception) {
      setErrorMessage('Invalid Field(s)')
      setTimeout(() => {
        setErrorMessage(null)
      }, 5000)
    }
  }

  const creatBlogForm = () => (
    <div>
      <p>
        Search:
      </p>
      <form onSubmit={handleBlogCreation}>
        <div>
          Title
          <input
            type="text"
            value={newTitle}
            name="newTitle"
            onChange={({ target }) => setNewTitle(target.value)}
            />
        </div>
        <div>
          Channel
          <input
            type="text"
            value={newAuthor}
            name="newAuthor"
            onChange={({ target }) => setNewAuthor(target.value)}
            />
        </div>
        <div>
          Url
          <input
            type="text"
            value={newUrl}
            name="newUrl"
            onChange={({ target }) => setNewUrl(target.value)}
            />
        </div>
        <button type="submit">submit</button>
      </form>
    </div>
  )

  const videoForm = () => (
    videos.map(video =>
      <Video key={video.id} video={video} />
    )
  )

  const loginForm = () => (
    <form onSubmit={handleLogin}>
      <div>
        username
        <input
          type="text"
          value={username}
          name="Username"
          onChange={({ target }) => setUsername(target.value)}
        />
      </div>
      <div>
        password
        <input
          type="password"
          value={password}
          name="Password"
          onChange={({ target }) => setPassword(target.value)}
        />
      </div>
      <button type="submit">login</button>
    </form>
  )

  const handleLogin = async (event) => {
    event.preventDefault()
    try {
      const user = await loginService.login({
        username, password,
      })
      setUser(user)
      blogService.setToken(user.token)
      window.localStorage.setItem(
        'loggedBlogappUser', JSON.stringify(user)
      ) 
      setUsername('')
      setPassword('')
    } catch (exception) {
      setErrorMessage('wrong credentials')
      setTimeout(() => {
        setErrorMessage(null)
      }, 5000)
    }
  }
  
  const logoutUser = (event) => {
    event.preventDefault()
    window.localStorage.removeItem('loggedBlogappUser')
    blogService.setToken(null)
    setUser(null)
  }

  return (
    <div>
      <h1>DataTube</h1>
      <div>
        {user === null ?
          [loginForm(),
            <Notification message={errorMessage} />]:
          [userForm(),
            creatBlogForm(),
            <Notification message={errorMessage} />,
            videoForm()]
          }
      </div>
    </div>
  )
}

export default App
