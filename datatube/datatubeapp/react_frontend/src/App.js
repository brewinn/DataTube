import { useState, useEffect } from 'react'
import SearchForm from './components/searchForm'
import Pagination from './components/Pagination'
import Notification from './components/notification'
import VideoForm from './components/VideoForm'
import Channel from './components/Channel'
import videoService from './services/videos'
import 'bootstrap/dist/css/bootstrap.min.css';


const App = () => {
  const [videos, setVideos] = useState([])
  const [channel, setChannel] = useState(null)
  const [errorMessage, setErrorMessage] = useState(null)
  const [searchText, setSearchText] = useState('')
  const [page, setPage] = useState(0)
  const [embed, setEmbed] = useState(true)

  useEffect(() => {
    window.scrollTo(0, 0)
  }, [page])

  const handleChannel = async (event) =>{
    setPage(0)
    const response = await videoService.getChannel(event)
    if(response[0].model === "datatubeapp.channel"){
      setChannel(response[0])
      setVideos(response.slice(1))
    }
    else{
      setChannel(event)
      setVideos(response)
    }
  }

  const getData = async (event) => {
    event.preventDefault()
    if(searchText === ''){
      setErrorMessage('invalid search')
      setTimeout(() => {
        setErrorMessage(null)
      }, 5000)
      return
    }
    setPage(0)
    const response = await videoService.loadPage([searchText,event.target[1].checked, event.target[2].checked, event.target[3].checked, event.target[4].checked, event.target[5].firstChild.data])
    setVideos(response)
    setChannel(null)
  }

  return (
    <div>
      <h1 className='ms-2 ps-1'>DataTube</h1>
      <div>
        {channel ? <Channel channel={channel}/>: <></>}
        {videos.length === 0 ? [<SearchForm searchText={searchText} setSearchText={setSearchText} getData={getData}/>,
          <Notification message={errorMessage} />]: 
          [<SearchForm searchText={searchText} setSearchText={setSearchText} getData={getData} embed={embed} setEmbed={setEmbed}/>,
          <Notification message={errorMessage} />,
          <VideoForm key={'videoForm'} videos={videos} page={page} setChannel={handleChannel} embed={embed}/>,
          <Pagination videos={videos} setPage={setPage} page={page}/>]
          }
      </div>
    </div>
  )
}

export default App
