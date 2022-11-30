  import  Button from 'react-bootstrap/Button';

  const Pagination = ({page, setPage, videos}) => {
    var selectors = []
      const pages =Array.from({length: Math.ceil(videos.length/16)}, (_, i) => i + 1)
      pages.slice(Math.max(0,page-5), Math.min(pages.length, page+6)).map(j => selectors.push(<Button disabled={j-1 === page} onClick={() => setPage(j-1)} key={`page-forward${j}`}>{j}</Button>))
      
    return (
      <div className='mx-auto' style={{width: 37 * selectors.length + 'px'}}>
      {selectors}
      </div>
    )
  }

  export default Pagination